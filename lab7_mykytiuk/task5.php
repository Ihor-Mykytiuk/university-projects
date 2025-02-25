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
        // Завдання 5

        // Клас для виведення таблиці множення для вказаного числа 
        class MultiplicationTable {
            public $number;

            // Конструктор
            public function __construct($number) {
                $this->number = $number;
            }

            // Метод для обчислення
            public function calculate() {
                $result = [];
                for ($i = 1; $i <= 10; $i++) {
                    $result[] = $this->number * $i;
                }
                return $result;
            }

            // Метод для виведення таблиці
            public function showTable() {
                $result = $this->calculate();
                echo "<table border='1'>";
                echo "<tr><th colspan='2'>Таблиця множення на $this->number</th></tr>";
                for ($i = 0; $i < 10; $i++) {
                    echo "<tr><td>$this->number * " . ($i + 1) . "</td><td>$result[$i]</td></tr>";
                }
                echo "</table><br>";
            }
        }

        // Кілька об'єктів для демонстрації працездатності класу
        $table1 = new MultiplicationTable(2);
        $table2 = new MultiplicationTable(3);
        $table3 = new MultiplicationTable(4);

        $table1->showTable();
        $table2->showTable();
        $table3->showTable();
        ?>
        <h3 class="back"><a href="lab7.php">Назад</a></h3>
    </body>
</html>

        