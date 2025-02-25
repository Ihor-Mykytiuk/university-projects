<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 1-7</title>
    </head>
    <body>
        <h3>Завдання 1-7</h3>
        <?php
        // Завдання 1

        // 1.1 створити клас Student з властивостями name, suname, group; 
        class Student {
            public $name;
            public $surname;
            public $group;

            //2.1 в класі Student потрібно описати метод getInfo ();
            //2.2 метод getInfo () повинен виводити значення властивостей об'єкта;
            public function getInfo() {
                echo "Ім'я: $this->name, Прізвище: $this->surname, Група: $this->group<br>";
            }

            //3.1 в класі Student необхідно описати конструктор;
            //3.2 конструктор повинен задавати початкові значення властивостей name, suname, group;
            public function __construct($name = 'Ім\'я', $surname = 'Прізвище', $group = 'Група') {
                $this->name = $name;
                $this->surname = $surname;
                $this->group = $group;
            }

            //4.1 в класі Student описати метод __clone ();
            //4.2 метод __clone повинен задавати початкові значення властивостей за замовчуванням при копіюванні об'єктів;
            public function __clone() {
                $this->name = 'Ім\'я';
                $this->surname = 'Прізвище';
                $this->group = 'Група';
            }
        }

        //1.2 створити три об'єкти класу Student; 
        $student1 = new Student();
        $student2 = new Student();
        $student3 = new Student();

        //1.3 задати довільні значення властивостям для кожного з об'єктів. 
        $student1->name = 'Віталій';
        $student1->surname = 'Ковальчук';
        $student1->group = 'ІПЗ-21';
        $student2->name = 'Петро';
        $student2->surname = 'Петренко';
        $student2->group = 'ІПЗ-22';
        $student3->name = 'Іван';
        $student3->surname = 'Іваненко';
        $student3->group = 'ІПЗ-23';

        // Завдання 2
        //2.3 викликати метод getInfo () для кожного з об'єктів.
        echo '<p>Завдання 2</p>';
        $student1->getInfo();
        $student2->getInfo();
        $student3->getInfo();

        // Завдання 3
        //3.3 створити крім існуючих трьох об’єктів класу Student, додатково ще три об'єкти з використання конструктора.
        $student4 = new Student('Василь', 'Васильчук', 'ІПЗ-24');
        $student5 = new Student('Олена', 'Оленчук', 'ІПЗ-21');
        $student6 = new Student('Марія', 'Марійчук', 'ІПЗ-22');

        // Завдання 4 
        //4.3 створити сьомий об'єкт, скопіювавши один з наявних об'єктів.
        $student7 = clone $student1;

        // Завдання 5
        echo '<p>Завдання 5</p>';

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
        
        // Завдання 7
        echo '<p>Завдання 7</p>';
        
        // Створити клас користувача, з полями: прізвище, ім'я, вік і e-mail.
        class User {
            public $surname;
            public $name;
            public $age;
            public $email;
            public function __construct($surname, $name, $age, $email) {
                $this->surname = $surname;
                $this->name = $name;
                $this->age = $age;
                $this->email = $email;
            }
            public function getInfo() {
                echo "Прізвище: $this->surname, Ім'я: $this->name, Вік: $this->age, E-mail: $this->email<br>";
            }
        }

        // Форма для введення даних
        echo '<form method="post" action="task.php">';
        echo '<input type="text" name="surname" placeholder="Прізвище"><br>';
        echo '<input type="text" name="name" placeholder="Ім\'я"><br>';
        echo '<input type="text" name="age" placeholder="Вік"><br>';
        echo '<input type="text" name="email" placeholder="E-mail"><br>';
        echo '<input type="submit" value="Відправити">';
        echo '</form>';
        
        // Виведення даних користувача
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $surname = $_POST['surname'];
            $name = $_POST['name'];
            $age = $_POST['age'];
            $email = $_POST['email'];
            if ($surname && $name && $age && $email) {
                $user = new User($surname, $name, $age, $email);
                $user->getInfo();
            } else {
                echo 'Заповніть всі поля';
            }
        }
        ?>
    <h3 class="back"><a href="lab7.php">Назад</a></h3>