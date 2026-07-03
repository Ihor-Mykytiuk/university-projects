<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 4</title>
        <style>
            .valid {
            }
            .invalid {
                color: red;
                border: double 3px;
            }
        </style>
    </head>
    <body>
        <h3>Завдання 4</h3>
        <?php
            $name_pattern = "/^([A-ZА-ЯҐЄІЇ][a-zа-яґєії]+)$/u";
            $surname_pattern = "/^([A-ZА-ЯҐЄІЇ][a-zа-яґєії]+)$/u";
            //логін тільки латина малими літерами
            $login_pattern = "/^[a-z]+$/";
            // Пароль мінімум 6 символів, з яких мінімум по 1 букві і цифрі
            $password_pattern = "/^(?=.*[a-zA-Z])(?=.*[0-9]).{6,}$/";
            // Повторення паролю
            $repeat_password_pattern = $password_pattern;
            // Адреса електронної пошти
            $email_pattern = "/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/";
            echo "<form action='task4.php' method='post'>";
            echo "<label for='name'>Ім'я:</label><br>";
            if (isset($_POST['name'])) {
                if (preg_match($name_pattern, $_POST['name'])) {
                    echo "<input type='text' id='name' name='name' value='".$_POST['name']."' class='valid'>
                    <span>✓</span><br>";
                } else {
                    echo "<input type='text' id='name' name='name' value='".$_POST['name']."' class='invalid'>
                    <span>Неправильний формат</span><br>";
                }
            } else {
                echo "<input type='text' id='name' name='name'><br>";
            }
            echo "<label for='surname'>Прізвище:</label><br>";
            if (isset($_POST['surname'])) {
                if (preg_match($surname_pattern, $_POST['surname'])) {
                    echo "<input type='text' id='surname' name='surname' value='".$_POST['surname']."' class='valid'>
                    <span>✓</span><br>";
                } else {
                    echo "<input type='text' id='surname' name='surname' value='".$_POST['surname']."' class='invalid'>
                    <span>Неправильний формат</span><br>";
                }
            } else {
                echo "<input type='text' id='surname' name='surname'><br>";
            }
            echo "<label for='login'>Логін:</label><br>";
            if (isset($_POST['login'])) {
                if (preg_match($login_pattern, $_POST['login'])) {
                    echo "<input type='text' id='login' name='login' value='".$_POST['login']."' class='valid'>
                    <span>✓</span><br>";
                } else {
                    echo "<input type='text' id='login' name='login' value='".$_POST['login']."' class='invalid'>
                    <span>Неправильний формат</span><br>";
                }
            } else {
                echo "<input type='text' id='login' name='login'><br>";
            }
            echo "<label for='password'>Пароль:</label><br>";
            if (isset($_POST['password'])) {
                if (preg_match($password_pattern, $_POST['password'])) {
                    echo "<input type='password' id='password' name='password' value='".$_POST['password']."' class='valid'>
                    <span>✓</span><br>";
                } else {
                    echo "<input type='password' id='password' name='password' value='".$_POST['password']."' class='invalid'>
                    <span>Неправильний формат</span><br>";
                }
            } else {
                echo "<input type='password' id='password' name='password'><br>";
            }
            echo "<label for='repeat_password'>Повторіть пароль:</label><br>";
            if (isset($_POST['repeat_password'])) {
                if (preg_match($repeat_password_pattern, $_POST['repeat_password']) && $_POST['repeat_password'] == $_POST['password']) {
                    echo "<input type='password' id='repeat_password' name='repeat_password' value='".$_POST['repeat_password']."' class='valid'>
                    <span>✓</span><br>";
                } else {
                    echo "<input type='password' id='repeat_password' name='repeat_password' value='".$_POST['repeat_password']."' class='invalid'>
                    <span>Неправильний формат або паролі не співпадають</span><br>";
                }
            } else {
                echo "<input type='password' id='repeat_password' name='repeat_password'><br>";
            }
            echo "<label for='email'>Електронна пошта:</label><br>";
            if (isset($_POST['email'])) {
                if (preg_match($email_pattern, $_POST['email'])) {
                    echo "<input type='text' id='email' name='email' value='".$_POST['email']."' class='valid'>
                    <span>✓</span><br>";
                } else {
                    echo "<input type='text' id='email' name='email' value='".$_POST['email']."' class='invalid'>
                    <span>Неправильний формат</span><br>";
                }
            } else {
                echo "<input type='text' id='email' name='email'><br>";
            }
            echo "<input type='submit' value='Відправити'>";
        ?>
        <h3 class='back'><a href="lab6.php">Назад</a><br></h3>
    </body>
</html>

