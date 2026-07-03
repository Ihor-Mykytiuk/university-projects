<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 2</title>
    </head>
    <body>
        <h3>Завдання 2</h3>
        <?php
            $names["Бойчук"]="Іван";
            $names["Мельник"]="Борис"; 
            $names["Швець"]="Антон";
            foreach ($names as $key => $value) {
            echo "<b>$value $key</b><br>";}
            ?>
        <h3 class='back'><a href='lab4.php'>Назад</a></h3>
    </body>
</html>