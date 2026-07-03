<?php
require '../config.php';
include_once 'function.php';
?>
<html>
    <head>
        <title>Завдання 7</title>
    </head>
    <body>
        <h3>Завдання 7</h3>
        <?php
            $random = mt_rand(1, 6);
            echo "<a href='task7.php?random=$random'>Передати число $random</a><br>"; // Посилання на на самого себе з get параметром
            if (isset($_GET['random'])) {
                $random = $_GET['random'];
                switch ($random) {
                    case 1:
                        echo "Викликати функцію func1";
                        break;
                    case 2:
                        echo "Викликати функцію func2";
                        break;
                    case 3:
                        echo "Викликати функцію func3";
                        break;
                    default:
                        echo "Некоректні дані";
                }
            }
        ?>
        <h3 class='back'><a href="lab3.php">Назад</a></h3>
    </body>
</html>
