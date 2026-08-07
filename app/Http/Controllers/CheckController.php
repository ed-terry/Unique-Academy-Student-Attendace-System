<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Employee;
use App\Models\Attendance;
use App\Models\Leave;

class CheckController extends Controller
{
    public function index()
    {
        return view('admin.check')->with(['employees' => Employee::all()]);
    }

    public function CheckStore(Request $request)
    {
        $date = $request->input('date', today()->format('Y-m-d'));

        if ($request->filled('attendance')) {
            foreach ($request->input('attendance') as $employeeId => $status) {
                $employee = Employee::find($employeeId);
                if (! $employee) {
                    continue;
                }

                $attendance = Attendance::firstOrNew([
                    'emp_id' => $employeeId,
                    'attendance_date' => $date,
                    'type' => 0,
                ]);

                $attendance->attendance_time = $employee->schedules->first()->time_in ?? date('H:i:s');
                $attendance->status = $status === 'present' ? 1 : ($status === 'late' ? 0 : 0);
                $attendance->save();
            }
        }

        flash()->success('Success', 'Attendance has been recorded successfully!');
        return back();
    }
    public function sheetReport()
    {

    return view('admin.sheet-report')->with(['employees' => Employee::all()]);
    }
}
