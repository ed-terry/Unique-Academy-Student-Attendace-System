<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\User;
use App\Models\Role;
use Hash;
use Spatie\Permission\Traits\HasRoles;
use DB;
class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        $user = User::create([
            'name' => 'Unique Academy Admin',
            'email' => 'admin@uniqueacademy.local',
            'password' => Hash::make('password123'),
        ]);

        $role = Role::create([
            'slug' => 'admin',
            'name' => 'Administrator',
        ]);

        $user->roles()->sync([$role->id]);
    }
}
