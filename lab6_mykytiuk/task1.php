<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 1</title>
    </head>
    <body>
        <h3>Завдання 1</h3>
        <?php
            echo "<p>a)</p>";
            // Вивести текст з файлу 
            $file = fopen("files/text.txt", "r") or die("Неможливо відкрити файл");
            // Виводити текст рядками
            while (!feof($file)) {
                echo htmlspecialchars(fgets($file)) . "<br>";
            }
            fclose($file);

            echo "<p>b)</p>";
            $file = fopen("files/text.txt", "r") or die("Неможливо відкрити файл");
            // Вивести назви відкриючих тегів з тексту
            while (!feof($file)) {
                $line = fgets($file);
                // Знайти відкриваючі теги
                preg_match_all("/<[^\/].*?>/", $line, $matches); 

                // Виводити назви без кутових дужок
                foreach ($matches[0] as $match) {
                    echo substr($match, 1, -1) . "<br>";
                }
            }
            fclose($file);

            echo "<p>c)</p>";
            $file = fopen("files/text.txt", "r") or die("Неможливо відкрити файл");
            while (!feof($file)) {
                $line = fgets($file);
                // Знайти відкриваючі теги
                preg_match_all("/<[^\/].*?>/", $line, $matches);
                
                // Виводити назви з кутовими дужками
                foreach ($matches[0] as $match) {
                    echo htmlspecialchars($match) . "<br>";
                }
            }
            fclose($file);
        ?>
        <h3 class='back'><a href="lab6.php">Назад</a><br></h3>
    </body>
</html>

