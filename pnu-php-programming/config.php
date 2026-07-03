<?php
include_once("db.php");
$LastModified_unix = strtotime(date("D, d M Y H:i:s", filectime($_SERVER['SCRIPT_FILENAME']))); 
$LastModified = gmdate("D, d M Y H:i:s \G\M\T", $LastModified_unix); 
echo "Файл був змінений: $LastModified"."<br>";
/*
$path = __DIR__;
echo "path to config.php=".$path."<br>";*/
?>
<html>
<head>
<meta http-equiv='Content-Type' content='text/html' charset='utf-8'>
<link rel='stylesheet' href='http://mykytiukihor.infinityfreeapp.com//css/style.css' type='text/css' media='screen, projection'/>
<script type='text/javascript' src='http://mykytiukihor.infinityfreeapp.com//js/jquery-3.6.0.min.js'></script>
<script type='text/javascript' src='http://mykytiukihor.infinityfreeapp.com//js/my.js'></script>

</head>
<body>
<p id="main"> <a href='http://mykytiukihor.infinityfreeapp.com/'>На головну</a> </p>

</body>
<?php
?>
