<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 6</title>
    </head>
    <body>
        <h3>Завдання 6</h3>
        <form action="task6.php" method="post">
            <label for="surname">Прізвище:</label>
            <input type="text" name="surname" id="surname"><br>
            <label for="name">Ім'я:</label>
            <input type="text" name="name" id="name"><br>
            <label for="email">E-mail:</label>
            <input type="email" name="email" id="email"><br>
            <label for="password">Пароль:</label>
            <input type="password" name="password" id="password"><br>
            <label for="password2">Підтвердження паролю:</label>
            <input type="password" name="password2" id="password2"><br>
            <input type="submit" value="Готово" name="Send">
        </form>
        <?php
        if (isset($_POST['Send'])) {
            // Отримання даних з форми
            $surname = $_POST['surname'];
            $name = $_POST['name'];
            $email = $_POST['email'];
            $password = $_POST['password'];
            $password2 = $_POST['password2'];

            // Перевірка на заповненість полів
            if ($surname == "" || $name == "" || $email == "" || $password == "" || $password2 == "") {
                echo "Заповніть всі поля!";
            }
            // Перевірка на співпадіння паролів
            else if ($password != $password2) {
                echo "Паролі не співпадають!";
            }
            else {
                // Запис даних у асоціативний масив
                $user = array("surname" => $surname, "name" => $name, "email" => $email, "password" => $password);
                // Виведення даних у вигляді таблиці
                echo "<table border='1'>";
                echo "<tr><th>Прізвище</th><th>Ім'я</th><th>E-mail</th><th>Пароль</th></tr>";
                // Виведення за допомогою foreach
                echo "<tr>";
                foreach ($user as $key => $value) {
                    echo "<td>$value</td>";
                }
                echo "</tr>";
                echo "</table>";
            }
        }
        ?>
        <h3 class='back'><a href='lab4.php'>Назад</a></h3>
    </body>
</html>