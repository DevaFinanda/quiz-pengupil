<?php
    // Untuk Docker environment, gunakan environment variables
    $host     = getenv('DB_HOST') ?: 'localhost';
    $user     = getenv('DB_USER') ?: 'root'; 
    $password = getenv('DB_PASS') ?: '';                  
    $db       = getenv('DB_NAME') ?: 'quiz_pengupil';

    $con = mysqli_connect($host, $user, $password, $db);
    if (!$con) { 
        die("Connection failed: " . mysqli_connect_error());    
    }
?>
