<? require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/config.php'; ?>
<html>
    <head>
        <title>My register page</title>
    </head>
    <body>
    <?php
    session_start(); 
        if (!isset($_SESSION['login'])) {
        echo "<p>Ви увійшли як гість</p>";
        } else {
        echo "<p>Ви увійшли як користувач ".$_SESSION['login']."</p>";
        }
        ?>
    <form action="register.php" method="post">
        Введіть логін: <br><input type="text" name="login"><br>
        Введіть електронну пошту: <br><input type="text" name="email"><br>
        Введіть пароль: <br><input type="password" name="passwd"><br>
        <input type="submit" value="Зареєструватися">
    </form>
    <?php
        // Виведення зареєстрованих користувачів з бази даних
        $sql = "SELECT * FROM user_for_session";

        $result = $db_server->query($sql);
        
        // Виведення у вигляді таблиці 
        echo "<h4>Зареєстровані користувачі</h4>";
        echo "<table border='1'>";
        echo "<tr><td>id</td><td>login</td><td>email</td><td>password</td></tr>";
        while ($row = $result->fetch_assoc()) {
            echo "<tr><td>".$row['id']."</td><td>".$row['login']."</td><td>".$row['email']."</td><td>".$row['password']."</td></tr>";
        }
        echo "</table>";
        $result->free();
        $db_server->close();
    ?>
    <h3 class='back'><a href="index.phpx">Назад</a></h3>
    </body>
</html>