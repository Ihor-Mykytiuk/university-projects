<?php
require '../config.php';
?>
<html>
    <title>Температура</title>
<body>
<h3>Меню</h3>
<div>
Введіть номер завдання:<br>
1 - обчислення максимальної температури;<br>
2 - обчислення мінімальної температури;<br>
3 - обчислення середньої температури;<br>
<?
$zm = floatval($_GET['zm']);
$random_zm = floatval($_GET['random_zm']);
echo "<br>Значення переданої змінної zm=$zm";
echo '<br>Значення переданої змінної zm=$zm';
echo "<br>Значення переданої змінної random_zm=".$random_zm;
?>
<form action='task7.php?zm=<?php echo $_GET['zm']; ?>&random_zm=<?php echo $_GET['random_zm']; ?>' method='post'>
    <label for="temperature1">Температура 1</label>
    <input type='text' name='temperature1'><br>
    <label for="temperature2">Температура 2</label>
    <input type='text' name='temperature2'><br>
    <label for="temperature3">Температура 3</label>
    <input type='text' name='temperature3'><br>
    <label for="choice">Виберіть завдання</label>
    <input type='text' name='choice'><br>
    <input type='submit' value='Показати'>
    
</form>


<?php

if (!empty($_POST["temperature1"]) && !empty($_POST["temperature2"]) && !empty($_POST["temperature3"]) && !empty($_POST["choice"])) {
    $temperature1=floatval($_POST['temperature1']);
    $temperature2=floatval($_POST['temperature2']);
    $temperature3=floatval($_POST['temperature3']);
    $choice=$_POST['choice'];
    echo "<br>Значення переданої змінної zm=".$zm;
    echo "<br>Значення переданої змінної random_zm=".$random_zm;
    echo "<br>Сума всіх змінних: ".($temperature1+$temperature2+$temperature3 + $zm + $random_zm)."<br>";
    

    switch ($choice) {
        case '1':
            echo "Максимальна температура: ".max($temperature1, $temperature2, $temperature3);
            break;
        case '2':
            echo "Мінімальна температура: ".min($temperature1, $temperature2, $temperature3, $zm, $random_zm);
            break;
        case '3':
            echo "Середня температура: ".(($temperature1+$temperature2+$temperature3 + $zm + $random_zm)/5);
            break;
        default:
            echo "Некоректно введені дані, повторіть спробу";
            break;
    }
}
?>


</div>