<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 1-4</title>
    </head>
    <body>
        <h3>Завдання 1-4</h3>
        <?php
        // Завдання 1

        // 1.1 створити клас Student з властивостями name, suname, group; 
        class Student {
            public $name;
            public $surname;
            public $group;

            // 2.1 в класі Student потрібно описати метод getInfo ();
            // 2.2 метод getInfo () повинен виводити значення властивостей об'єкта;
            public function getInfo() {
                echo "Ім'я: $this->name, Прізвище: $this->surname, Група: $this->group<br>";
            }

            // 3.1 в класі Student необхідно описати конструктор;
            // 3.2 конструктор повинен задавати початкові значення властивостей name, suname, group;
            public function __construct($name = 'Ім\'я', $surname = 'Прізвище', $group = 'Група') {
                $this->name = $name;
                $this->surname = $surname;
                $this->group = $group;
            }

            // 4.1 в класі Student описати метод __clone ();
            // 4.2 метод __clone повинен задавати початкові значення властивостей за замовчуванням при копіюванні об'єктів;
            public function __clone() {
                $this->name = 'Ім\'я';
                $this->surname = 'Прізвище';
                $this->group = 'Група';
            }
        }

        // 1.2 створити три об'єкти класу Student; 
        $student1 = new Student();
        $student2 = new Student();
        $student3 = new Student();

        // 1.3 задати довільні значення властивостям для кожного з об'єктів. 
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
        // 2.3 викликати метод getInfo () для кожного з об'єктів.
        $student1->getInfo();
        $student2->getInfo();
        $student3->getInfo();

        // Завдання 3
        // 3.3 створити крім існуючих трьох об’єктів класу Student, додатково ще три об'єкти з використання конструктора.
        $student4 = new Student('Василь', 'Васильчук', 'ІПЗ-24');
        $student5 = new Student('Олена', 'Оленчук', 'ІПЗ-21');
        $student6 = new Student('Марія', 'Марійчук', 'ІПЗ-22');

        // Завдання 4 
        // 4.3 створити сьомий об'єкт, скопіювавши один з наявних об'єктів.
        $student7 = clone $student1;
        ?>
    <h3 class="back"><a href="lab7.php">Назад</a></h3>
</body>
</html>