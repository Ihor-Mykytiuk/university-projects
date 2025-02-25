<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 6</title>
    </head>
    <body>
        <h3>Завдання 6</h3>
        <?php
        // Завдання 6

        // Створіть клас країни в якому будуть поля: назва країни, населення і назва столиці.
        echo '<p>Завдання 6</p>';
        class Country {
            public $name;
            public $population;
            public $capital;
            public function __construct($name, $population, $capital) {
                $this->name = $name;
                $this->population = $population;
                $this->capital = $capital;
            }
            public function showTable() {
                echo "<table border='1'>";
                echo "<tr><td>Назва країни</td><td>$this->name</td></tr>";
                echo "<tr><td>Населення</td><td>$this->population</td></tr>";
                echo "<tr><td>Столиця</td><td>$this->capital</td></tr>";
                echo "</table><br>";
            }
        }

        // Масив об'єктів
        $countries = [
            new Country('Малайзія', 33000000, 'Куала-Лумпур'),
            new Country('Мальта', 518536, 'Валлетта'),
            new Country('Мексика', 126700000, 'Мехіко-Сіті'),
            new Country('Молдова', 2600000, 'Кишинів'),
            new Country('Монако', 38000, 'Монако')
        ];

        // Вивести кожну країну в таблицю в три рядки по дві комірки в кожному
        foreach ($countries as $country) {
            $country->showTable();
        }
        ?>
        <h3 class="back"><a href="lab7.php">Назад</a></h3>
    </body>
</html>