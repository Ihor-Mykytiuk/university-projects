<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 5</title>
    </head>
    <body>
        <h3>Завдання 5</h3>
        <?php
        $postcode_pattern = "/^\d{5}-\d{4}$/";
        echo "<form action='task5.php' method='post'>";
        echo "Поштовий індекс (Сполучені Штати Америки)<br>";
        echo "Числовий код з дев’ятьма цифрами. Після п’ятої дефіс<br>";
        echo "Приклад: 12345-6789<br>";
        if (isset($_POST['postcode'])) {
            if (preg_match($postcode_pattern, $_POST['postcode'])) {
                echo "<input type='text' id='postcode' name='postcode' value='".$_POST['postcode']."'>
                <span>Дані введено коректно</span><br>";
            } else {
                echo "<input type='text' id='postcode' name='postcode' value='".$_POST['postcode']."'>
                <span>Некоректно введено дані. Введіть повторно</span><br>";
            }
        } else {
            echo "<input type='text' id='postcode' name='postcode'><br>";
        }
        echo "<input type='submit' value='Відправити'>";
        ?>
        <h3 class='back'><a href="lab6.php">Назад</a><br></h3>
    </body>
</html>
