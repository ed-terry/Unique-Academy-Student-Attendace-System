<?php

namespace App\Http\Requests;

use Illuminate\Foundation\Http\FormRequest;

class EmployeeRec extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize()
    {
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array
     */
    public function rules()
    {
        return [
            'name' => 'required|string|min:3|max:64',
            'position' => 'required|string|min:3|max:64',
            'student_class' => 'required|string|min:2|max:64',
            'contact_number' => 'nullable|string|min:7|max:20',
            'email' => 'nullable|email|max:128',
            'schedule' => 'required|exists:schedules,slug',
            'classroom_id' => 'nullable|integer|exists:classrooms,id',
        ];
    }
}
