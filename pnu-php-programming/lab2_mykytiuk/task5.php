<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 5</title>
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
<h3>Завдання 5</h3>
<?php
    // Масив з назвами ягід, які також відповідають назвам файлів
    $berries = array("Blackberry", "Cranberry", "Raspberry", "Currant", "Strawberry", "Gooseberry");
    shuffle($berries); // Перемішати масив
    // Ягоди українською мовою (словник)
    $berriesUkr = array("Blackberry" => "Ожини", "Cranberry" => "Журавлини",  "Raspberry" => "Малини", "Strawberry" => "Полуниці", "Currant" => "Смородини", "Gooseberry" => "Аґрусу");

    $selectedBerries = array_rand($berries, 4); // Вибираємо випадково 4 ягоди
    $berry = $berries[$selectedBerries[0]]; // З цих чотирьох для перевірки вибираємо першу
    $berryUkr = $berriesUkr[$berry];

    echo "Натисніть, будь ласка, на зображення $berryUkr<br>";

    shuffle($selectedBerries); // Перемішати вибрані ягоди перед виведенням

    // Вивести зображення циклом
    foreach ($selectedBerries as $key) {
        $value = $berries[$key];
        echo "<a href='task5.php?berry=$berry&answer=$value'><img src='images/$value.jpg' alt='$value'></a>";
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