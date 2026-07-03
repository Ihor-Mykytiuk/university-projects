<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 4</title>
    </head>
    <body>
        <h3>Завдання 4</h3>
        <?php
            // Багатовимірний асоціативний масив з даними по трьох країнах
            $country["Germany"] = array("name" => "Німеччина", "capital" => "Берлін", "popul" => "83");
            $country["Japan"] = array("name" => "Японія", "capital" => "Токіо", "popul" => "126");
            $country["Italy"] = array("name" => "Італія", "capital" => "Рим", "popul" => "60");
            
            //Вивести як таблицю
            echo "<table border='1'>";
            echo "<tr><th>Країна</th><th>Столиця</th><th>Населення, млн.ч.</th></tr>";
            foreach ($country as $value) {
                echo "<tr>";
                // Вкладення однієї конструкції foreach в іншу
                foreach ($value as $value2) {
                    echo "<td>$value2</td>";
                }
                echo "</tr>";
            }
            echo "</table><br>";

            // три речення, типу «Столиця України — Київ, населення —45 млн. ч.
            foreach ($country as $key => $value) {
                echo "Столиця $value[name] — $value[capital], населення — $value[popul] млн. ч.<br>";
            }
            echo "<br>";

            // Посортувати елементи масиву $country
            asort($country);
            // Вивести ключі першого та другого рівнів та їх значення 
            foreach ($country as $key => $value) {
                echo "$key:<br>";
                foreach ($value as $key2 => $value2) {
                    echo "$key2=>$value2";
                    if ($key2 === array_key_last($value)) { // Змінено $myArray на $value
                        echo ";"; // Змінено $value на $value2
                    }
                    else {
                        echo "<br>"; // Змінено $value на $value2
                    }
                }
                echo "<br>";
            }

            // Виведення за допомогою функції print_r
            echo "<pre>";
            print_r($country);
            echo "</pre>";
        ?>
        <h3 class='back'><a href='lab4.php'>Назад</a></h3>
    </body>
</html>

