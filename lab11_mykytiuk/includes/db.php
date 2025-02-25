<?php
$db_name = 'if0_35997431_mykytiuk';
$db_host = 'sql200.infinityfree.com';
$db_user = 'if0_35997431';
$db_pass = '7hjCwdxiYx';

$db_server = mysqli_connect("$db_host", "$db_user", "$db_pass", "$db_name");
if (!$db_server) {
    die ("db.php: Error connect to db_server = $db_host, $db_user, $db_name"); 
}
