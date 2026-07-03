<?php
require '../config.php';
?>
<html>
    <title>Приклад оператора for</title>
<body>
<?php
//створення матриці у вигляді таблиці певного розміру
echo "<h3>Створення матриці у вигляді таблиці певного розміру</h3>";
if (!empty($_POST["rows"]) && !empty($_POST["cols"])) {
    $rows=$_POST['rows'];
    $cols=$_POST['cols'];
    echo "<table border='1'>";
    for ($i=1; $i<=$rows; $i++) {
        echo "<tr>";
        for ($j=1; $j<=$cols; $j++) {
            echo "<td>".$i.$j."</td>";
        }
        echo "</tr>";
    }
    echo "</table>";
}


echo "<div> Введіть кількість рядків:<br>
<form action='example1_1_21.php' method='post'>
<input type='text' name='rows'><br>
Введіть кількість стовпців:<br>
<input type='text' name='cols'><br>
<input type='submit' value='Показати'>
</form></div>
";
echo "<h3 class='back'><a href='lab1.php'>Назад</a></h3>";
?>
</body>
</html>