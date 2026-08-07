<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class AddStudentFieldsToEmployeesTable extends Migration
{
    public function up()
    {
        Schema::table('employees', function (Blueprint $table) {
            if (!Schema::hasColumn('employees', 'student_class')) {
                $table->string('student_class')->nullable()->after('position');
            }
            if (!Schema::hasColumn('employees', 'contact_number')) {
                $table->string('contact_number')->nullable()->after('student_class');
            }
        });
    }

    public function down()
    {
        Schema::table('employees', function (Blueprint $table) {
            if (Schema::hasColumn('employees', 'contact_number')) {
                $table->dropColumn('contact_number');
            }
            if (Schema::hasColumn('employees', 'student_class')) {
                $table->dropColumn('student_class');
            }
        });
    }
}
