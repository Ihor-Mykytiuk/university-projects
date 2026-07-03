<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 3</title>
    </head>
<body>
<h3>Завдання 3</h3>
    <div>
        <form action='task3.php' method='post'>
            <label for="numberX">x:</label>
            <input type='text' name='numberX'><br>
            <label for="numberY">y:</label>
            <input type='text' name='numberY'><br>
            <input type='submit' value='Submit'>
        </form>
        <?php
        if (!empty($_POST["numberX"]) && !empty($_POST["numberY"])) {
            $numX = $_POST['numberX'];
            $numY = $_POST['numberY'];
            if (intval($numX) == $numX && intval($numY) == $numY) {
                if($numX > 0) {
                    $result = 3 * $numX * $numY;
                }
                elseif($numX < 0 && $numY > 3 / 2) {
                    $result = 2 * $numX / $numY;
                }
                else {
                    $result = $numX ** 2 + $numY ** 3;
                }
                echo "x = $numX, y = $numY<br>";
                echo "Результат: $result";
            } else {
                echo "Введіть цілі числа";
            }
        }
        ?>
    </div>
    <h3 class='back'><a href='lab2.php'>Назад</a></h3>
</body>
</html>
