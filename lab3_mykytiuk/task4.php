<?php
require '../config.php';
include_once 'function.php';
?>
<html>
    <head>
        <title>Завдання 4</title>
    </head>
<body>
<h3>Завдання 4</h3>
<?php
echo "<p>4.11</p>";
// Формування рядку з 20 символів
$line = "";
for ($i = 1; $i <= 20; $i++) {
    if ($i % 3 == 0) {
        $line .= "?";
    } else {
        $line .= "*";
    }
}
echo $line;

echo "<p>4.12</p>";
// Виведення таблиці квадратних коренів чисел від 1 до 10
echo "<table border='1'>";
echo "<tr><th>Число</th><th>Квадратний корінь</th></tr>";
for ($i = 1; $i <= 10; $i++) {
    echo "<tr><td>$i</td><td>" . sqrt($i) . "</td></tr>";
}
echo "</table>";

echo "<p>4.13</p>";
$a = 3;
$b = 10;
$sum = 0;
$count = 0;
for ($i = $a; $i <= $b; $i++) {
    $sum += $i * $i;
    $count++;
}
echo "Середнє арифметичне квадратів усіх цілих чисел від $a до $b: " . $sum / $count;
?>
<h3 class='back'><a href="lab3.php">Назад</a></h3>
</body>
</html>