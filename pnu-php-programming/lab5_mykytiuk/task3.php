<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 3</title>
    </head>
    <body>
        <h3>Завдання 3</h3>
        <p>Зчитування даних з файлу та виведення у вигляді таблиці</p>
        <?php
            $file = fopen("files/tag1.txt", "r") or die("Неможливо відкрити файл");
            echo "<table border='1'>";
            while (!feof($file)) {
                echo "<tr>";

                echo "<td>";
                echo "&lt<b>".trim(fgets($file))."</b>&gt";
                echo "</td>";

                echo "<td>";
                echo fgets($file);
                echo "</td>";
                
                echo "</tr>";
            }
            echo "</table>";
            fclose($file);
        ?>
        <h3 class="back"><a href="lab5.php">Назад</a></h3>
    </body>
</html>