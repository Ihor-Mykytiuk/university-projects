<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 4</title>
        <style>
            input[type="image"] {
                width: 100px;
                height: 100px;
         }
            img {
                width: 200px;
                height: 200px;
            }
        </style>
    </head>
<body>
<h3>Завдання 4</h3>
<?php
    //Масив з назвами ягід, які також відповідають назвам файлів
    $berries = array("Blackberry", "Cranberry", "Raspberry", "Strawberry");
    //Ягоди українською мовою (словник)
    $berriesUkr = array("Blackberry" => "Ожини", "Cranberry" => "Журавлини",  "Raspberry" => "Малини", "Strawberry" => "Полуниці"); 

    //Вибираємо випадково 1 ягодe
    $berry = $berries[rand(0, 3)];
    $berryUkr = $berriesUkr[$berry];
    echo "Натисніть, будь ласка, на зображення $berryUkr<br>";

    shuffle($berries); //перемішати масив

    //вивести зображення циклом
    foreach ($berries as $value) {
        echo "<a href='task4.php?berry=$berry&answer=$value'><img src='images/$value.jpg' alt='$value'></a>";
    }
    // Перевірка на правильність вибору
    if (!empty($_GET["berry"]) && !empty($_GET["answer"])) {
        echo "<br>Ви вибрали зображення " . $berriesUkr[$_GET["answer"]] . "<br>";
        echo "<img src='images/" . $_GET["answer"] . ".jpg' alt='" . $_GET["answer"] . "'>";
        if ($_GET["berry"] == $_GET["answer"]) {
            echo "<br>Це правильно";
        } else {
            echo "<br>Це неправильно";
        }

    }
?>
<h3 class='back'><a href='lab2.php'>Назад</a></h3>
</body>
</html>