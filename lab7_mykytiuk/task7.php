<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 7</title>
    </head>
    <body>
        <h3>Завдання 7</h3>
        <?php
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
        echo '<form method="post" action="task7.php">';
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
    </body>
</html>