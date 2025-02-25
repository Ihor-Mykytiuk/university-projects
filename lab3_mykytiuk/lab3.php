<?php
require '../config.php';
include_once 'function.php';
if (!empty($_GET["zm"])) {echo "Значення переданої змінної zm=".$_GET["zm"];} else {echo "zminna zm not fount";}
$zm=$_GET["zm"];
?>
<html>
<H2>PHP. Робота з масивами</H2>
<?php
$my_array = array('Рядок 1', 'Рядок 2','Рядок 3');
create_table2($my_array,3,8,8);
?>
<a href="task2.php">Завдання 2</a><br>
    <a href="task3.php">Завдання 3</a><br>
    <a href="task4.php">Завдання 4</a><br>
    <a href="task5.php">Завдання 5</a><br>
    <a href="task6.php">Завдання 6</a><br>
    <a href="task7.php">Завдання 7</a><br>

<h3 class='back'><a href="../index.php">Повернутися в головне меню</a><br></h3>
</div>
</html>
