<?php
require '../config.php';
include_once 'function.php';
?>
<html>
    <head>
        <title>Завдання 5</title>
    </head>
<body>
    <h3>Завдання 5</h3>
    <?php
        echo "<p>5.1</p>";
        // Генерація масиву
        $arr = array();
        for ($i = 0; $i < 10; $i++) {
            $arr[$i] = mt_rand(1, 20);
        }
        print_array($arr);  // Функція для виведення масиву (з файлу function.php) 

        echo "<p>5.2</p>";
        $a = 11; // Варіант
        $N = ($a % 10 + 1) * 2; // Розмір масиву NxN

        // Генерація двовимірного масиву
        $matrix = array();
        for ($i = 0; $i < $N; $i++) {
            for ($j = 0; $j < $N; $j++) {
                $matrix[$i][$j] = mt_rand(1, 100);
            }
        }
        echo "Двовимірний масив розміром $N x $N діапазону від 1 до 100:<br>";
        print_table($matrix); // Функція для виведення двовимірного масиву (з файлу function.php)
    ?>
    <h3 class='back'><a href="lab3.php">Назад</a></h3>
</body>
</html>