<?php
require '../config.php';
include_once 'function.php';
?>
<html>
<head>
<title>Завдання 3</title>
</head>
<body>
<h3>Завдання 3</h3>
<p>Виведення елементів масиву та їх квадратів</p>
<?php
$my_array = array(4, 7, 8, 3, 5, 1);
elements_and_squares($my_array);
?>
<h3 class='back'><a href="lab3.php">Назад</a></h3>
</body>
</html> 