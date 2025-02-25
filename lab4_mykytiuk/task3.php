<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 3</title>
    </head>
    <body>
        <h3>Завдання 3</h3>
        <?php
            // Створення масиву згідно теми мого варіанту (ягоди)
            $my_topic = array(2 => "Blackberry", 3 => "Cranberry", 4 => "Raspberry", 5 => "Strawberry");

            echo "<p>Виведення масиву</p>";
            // Спочатку індекси, потім члени масиву
            foreach ($my_topic as $key => $value) {
                echo "$key => $value<br>";
            }

            // Поміняти місцями індекси та члени масиву
            $my_topic = array_flip($my_topic);
            echo "<p>Виведення масиву після зміни місцями індексів та членів масиву</p>";
            foreach ($my_topic as $key => $value) {
                echo "$key => $value<br>";
            }
        ?>
        <h3 class='back'><a href='lab4.php'>Назад</a></h3>
    </body>
</html>