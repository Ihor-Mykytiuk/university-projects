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
            $arr1 = [];
            $arr2 = [];
            // Заповнення першого масиву квадратами чисел від 10 до 20
            for ($i = 10; $i <= 20; $i++) {
                $arr1[] = $i ** 2;
            }
            // Заповнення другого масиву кубами чисел від 1 до 10
            for ($i = 1; $i <= 10; $i++) {
                $arr2[] = $i ** 3;
            }
            $arr3 = array_merge($arr1, $arr2); // Об'єднання масивів
            echo '<pre>';
            print_r($arr3);
            echo '</pre>';
        ?>
        <h3 class='back'><a href='lab4.php'>Назад</a></h3>
    </body>
</html>