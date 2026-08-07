<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>Unique Academy | Student Attendance</title>
        <meta content="Unique Academy student attendance portal" name="description" />
        <meta content="Unique Academy" name="author" />
        <link rel="shortcut icon" href="assets/images/unique-academy-logo.svg">
        @include('layouts.head')
  </head>
    <body class="pb-0" >
        @yield('content')
        @include('layouts.footer-script')    
        @include('includes.flash')
    </body>
</html>