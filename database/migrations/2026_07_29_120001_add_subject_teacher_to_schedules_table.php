<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class AddSubjectTeacherToSchedulesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('schedules', function (Blueprint $table) {
            if (!Schema::hasColumn('schedules', 'subject_name')) {
                $table->string('subject_name')->nullable()->after('slug');
            }
            if (!Schema::hasColumn('schedules', 'teacher_name')) {
                $table->string('teacher_name')->nullable()->after('subject_name');
            }
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('schedules', function (Blueprint $table) {
            if (Schema::hasColumn('schedules', 'teacher_name')) {
                $table->dropColumn('teacher_name');
            }
            if (Schema::hasColumn('schedules', 'subject_name')) {
                $table->dropColumn('subject_name');
            }
        });
    }
}
