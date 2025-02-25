<?php
require '../config.php';
include_once 'function.php';
?>
<html>
    <head>
        <title>Завдання 6</title>
    </head>
    <body>
        <h3>Завдання 6</h3>
        <form action='task6.php' method='post'>
        Введіть натуральне число:<br>
        <input type='text' name='number'><br>
        <input type='submit' value='Перевірити'>
        </form>
        <?php
            if (!empty($_POST["number"])) {
                $number = $_POST['number'];
                if ($number > 0 && intval($number) == $number) {
                    generate_array2($number); // Генерація та виведення масиву (з файлу function.php)
                } else {
                    echo "<p>Введене число не є натуральним</p>";
                }
            }
        ?>
        <h3 class='back'><a href="lab3.php">Назад</a></h3>
    </body>
</html>
<?php
// Завдання 7
include_once 'task7.php';
?>