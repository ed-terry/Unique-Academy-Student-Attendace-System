<?php

namespace App\Http\Controllers;

use DateTime;
use App\Models\Employee;
use App\Models\Latetime;
use App\Models\Attendance;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;
use App\Http\Requests\AttendanceEmp;

class AttendanceController extends Controller
{   
    public function index(Request $request)
    {
        $query = Attendance::with('employee');

        if ($request->filled('search')) {
            $search = $request->input('search');
            $query->whereHas('employee', function ($subquery) use ($search) {
                $subquery->where('name', 'like', "%{$search}%")
                    ->orWhere('email', 'like', "%{$search}%")
                    ->orWhere('student_class', 'like', "%{$search}%");
            })->orWhere('emp_id', $search);
        }

        if ($request->filled('attendance_date')) {
            $query->where('attendance_date', $request->input('attendance_date'));
        }

        $attendances = $query->orderBy('attendance_date', 'desc')->get();
        $summary = [
            'total_records' => $attendances->count(),
            'present' => $attendances->where('status', 1)->count(),
            'late' => $attendances->where('status', 0)->count(),
            'attendance_percentage' => $attendances->count() ? round(($attendances->where('status', 1)->count() / $attendances->count()) * 100, 2) : 0,
            'weekly_records' => Attendance::whereBetween('attendance_date', [now()->subDays(6)->format('Y-m-d'), now()->format('Y-m-d')])->count(),
        ];

        return view('admin.attendance')->with(['attendances' => $attendances, 'summary' => $summary]);
    }

    public function indexLatetime()
    {
        return view('admin.latetime')->with(['latetimes' => Latetime::all()]);
    }

    

    // public static function lateTime(Employee $employee)
    // {
    //     $current_t = new DateTime(date('H:i:s'));
    //     $start_t = new DateTime($employee->schedules->first()->time_in);
    //     $difference = $start_t->diff($current_t)->format('%H:%I:%S');

    //     $latetime = new Latetime();
    //     $latetime->emp_id = $employee->id;
    //     $latetime->duration = $difference;
    //     $latetime->latetime_date = date('Y-m-d');
    //     $latetime->save();
    // }

    public static function lateTimeDevice($att_dateTime, Employee $employee)
    {
        $attendance_time = new DateTime($att_dateTime);
        $checkin = new DateTime($employee->schedules->first()->time_in);
        $difference = $checkin->diff($attendance_time)->format('%H:%I:%S');

        $latetime = new Latetime();
        $latetime->emp_id = $employee->id;
        $latetime->duration = $difference;
        $latetime->latetime_date = date('Y-m-d', strtotime($att_dateTime));
        $latetime->save();
    }
  
}
