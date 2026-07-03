<?php
require 'config.php';
?>
<html>
<title> My PHP</title> 
<form action="lab1_mykytiuk/lab1.php">
<table border=0><tr><td>Login:</td><td><input type='text' name='ULogin'></td><tr>
<tr><td>Пароль:</td><td><input type='password' name='Passw'></td><tr>
<tr><td><input type='submit' value='Go' name='Send'></td><td>&nbsp</td></td></tr> </table>
</form>
<?php
$zm=10;
echo "<h2>Програмування мовою PHP</h2>
<h3>Перелік лабораторних робіт Микитюка Ігоря</h3>
<h4>Варіант №11</h4>
<div class=list>
<a href=lab1_mykytiuk/lab1.php?zm=$zm>lab1.php</a><br>
<a href=lab2_mykytiuk/lab2.php>lab2.php</a><br>
<a href=lab3_mykytiuk/lab3.php?zm=".$zm.">lab3.php</a><br>
<a href=lab4_mykytiuk/lab4.php>lab4.php</a><br>
<a href=lab5_mykytiuk/lab5.php>lab5.php</a><br>
<a href=lab6_mykytiuk/lab6.php>lab6.php</a><br>
<a href=lab7_mykytiuk/lab7.php>lab7.php</a><br>
<a href=lab9_mykytiuk/lab9.php>lab9.php</a><br>
<a href=lab10_mykytiuk/>lab10.php</a><br>
<a href=lab8DB_mykytiuk/lab8_DB.php>PHP+DB</a><br>
<a href=labJS_mykytiuk/labJS.php>PHP+JS</a><br>
<a href=lab11_mykytiuk/index.php>index.php</a><br>";

echo "<br>";
echo "<br>";
echo "<a href=test/test.php>test.php</a><br>";
echo "</div>";
echo "zm=$zm <br>";
echo "Zm=$Zm <br>";
echo 'zm=$zm <br>';

?>

</html>
