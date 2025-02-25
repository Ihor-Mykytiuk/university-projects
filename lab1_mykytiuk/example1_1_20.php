<?php
require '../config.php';
?>
<html>
    <title>Приклад оператора while</title>
<body>
<?php


//Таблиця множення для введеного числа
echo "<h3>Таблиця множення для введеного числа</h3>";
if (!empty($_POST["number"])) {
    $number=$_POST['number'];
    $i=1;
    while ($i<=10) {
        echo $number."*".$i."=".$number*$i."<br>";
        $i++;
    }
}
echo "<div> Введіть число:<br>
<form action='example1_1_20.php' method='post'>
<input type='text' name='number'><br>
<input type='submit' value='Показати'>
</form></div>
";


echo "<h3 class='back'><a href='lab1.php'>Назад</a></h3>";
?>
</body>
</html>