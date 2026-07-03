<?php

//тут вкажіть свої дані:
$db_name = 'if0_35997431_mykytiuk';
$db_host = 'sql200.infinityfree.com';
$db_user = 'if0_35997431';
$db_pass = '7hjCwdxiYx';


$db_server = mysqli_connect("$db_host", "$db_user", "$db_pass", "$db_name");
if (!$db_server) {
        die ("db.php: Error connect to db_server = $db_host, $db_user, $db_name <br>"); 
}
if ($db_server) {echo "db.php: good connect to db_server = $db_host, $db_user, $db_name <br>";}

if (!mysqli_set_charset($db_server, "utf8mb4")) {
        die("db.php: Error loading character set utf8mb4: " . mysqli_error($db_server));
} 
else {
        echo "db.php: Current character set: " . mysqli_character_set_name($db_server)."<br>";
}
    
?>