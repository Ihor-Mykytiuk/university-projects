<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 1</title>
    </head>
<body>
<h3>Завдання 1</h3>
<div>
    <form action='task1.php' method='post'>
        Введіть два числа:<br>
        <input type='text' name='number1'><br>
        <input type='text' name='number2'><br>
        <input type='submit' value='Submit'>
    </form>
    <?php
    if (!empty($_POST["number1"]) && !empty($_POST["number2"])) {
        $num1 = $_POST['number1'];
        $num2 = $_POST['number2'];
        echo "Число 1 = $num1, число 2 = $num2<br>";
        echo "Результат віднімання: $num1 - $num2 = " . ($num1 - $num2) . "<br>";
        echo "Результат множення: $num1 * $num2 = " . ($num1 * $num2) . "<br>";
        echo "Результат ділення: $num1 / $num2 = " . ($num1 / $num2) . "<br>";
        echo "Результат ділення по модулю: $num1 % $num2 = " . ($num1 % $num2) . "<br>";       
    }
    ?>
</div>
<h3 class='back'><a href='lab2.php'>Назад</a></h3>
</body>
</html>
    
    