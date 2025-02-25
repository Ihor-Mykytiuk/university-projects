<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 2</title>
    </head>
<body>
    <h3>Завдання 2</h3>
    <div>
        <form action='task2.php' method='post'>
            <label for="numberX">x:</label>
            <input type='text' name='numberX'><br>
            <label for="numberY">y:</label>
            <input type='text' name='numberY'><br>
            <label for="numberZ">z:</label>
            <input type='text' name='numberZ'><br>
            <input type='submit' value='Submit'>
        </form>
        <?php    
        if (!empty($_POST["numberX"]) && !empty($_POST["numberY"]) && !empty($_POST["numberZ"])) {
            $numX = $_POST['numberX'];
            $numY = $_POST['numberY'];
            $numZ = $_POST['numberZ'];
            if (intval($numX) == $numX && intval($numY) == $numY && intval($numZ) == $numZ && $numX > 0 && $numY > 0 && $numZ > 0) {
                $result = $numX ** 6 + $numX ** 5 * $numY + 0.5 * $numZ + $numX ** 2;
                echo "x = $numX, y = $numY, z = $numZ<br>";
                echo "Результат: $result";
            } else {
                echo "Введіть натуральні числа";
            }
        }
        ?>
    </div>
    <h3 class='back'><a href='lab2.php'>Назад</a></h3>
</body>
</html>
