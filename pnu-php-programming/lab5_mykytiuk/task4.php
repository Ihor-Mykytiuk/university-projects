<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 4</title>
    </head>
    <body>
        <h3>Завдання 4</h3>
        <p>Зчитування даних з файлу та виведення у вигляді таблиці</p>
        <?php
            $file_tags = fopen("files/tag2.txt", "r") or die("Неможливо відкрити файл");
            echo "<table border='1'>";
            $count_tags = 0;
            while (!feof($file_tags)) {
                $line = fgets($file_tags);
                $line_elem = explode(" ", $line);
                $tag = $line_elem[0];
                $text_description = implode(" ", array_slice($line_elem, 1));

                $text_description_elem = explode("-", $text_description);
                $text = $text_description_elem[0];
                $description = $text_description_elem[1];

                echo "<tr>";

                echo "<td>";
                echo "<b>" . htmlspecialchars($tag) . "</b>"; // Виведення назви тегу
                echo "</td>";

                echo "<td>";
                echo $text; // Виведення опису тегу
                echo "</td>";

                echo "<td>";
                echo $description; // Виведення опису тегу
                echo "</td>";

                echo "</tr>"; 

                $count_tags++; // Підрахунок кількості тегів
            }
            echo "</table>";
            fclose($file_tags);

            // Відкрити файл для запису (Якщо даний файл відсутній, створити його для читання і запису) та вивести кількість тегів
            $file_count = fopen("files/out.txt", "w+") or die("Неможливо відкрити файл");
            fwrite($file_count, "Всього у файлі tag2.txt описано тегів: " . $count_tags);

            // Зчитати вміст цього файлу і вивести під таблицею
            fseek($file_count, 0);
            echo "<p>" . fread($file_count, filesize("files/out.txt")) . "</p>";
            fclose($file_count); 
        ?>
        <h3 class="back"><a href="lab5.php">Назад</a></h3>
    </body>
</html>