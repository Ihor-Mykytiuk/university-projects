<? require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/config.php'; ?>
<?php
    session_start(); 
    if (!isset($_SESSION['login'])) {
        echo "<p>Ви увійшли як гість</p>";
    } else {
        echo "<p>Ви увійшли як користувач ".$_SESSION['login']."</p>";
    }
    ?>
    
<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $login = $_POST['login'];
        $email = $_POST['email'];
        $passwd = $_POST['passwd'];
        
        $sql = "SELECT * FROM user_for_session WHERE login = '$login'";
        $result = $db_server->query($sql);
        
        if ($result->num_rows > 0) {
            die("Користувач з таким логіном вже існує");
        } else {
            $sql = "INSERT INTO user_for_session (login, email, password) VALUES ('$login', '$email', '$passwd')";
            if ($db_server->query($sql) === TRUE) {
                echo "Реєстрація пройшла успішно";
            } else {
                echo "Помилка реєстрації, спробуйте ще раз";
            }
            header("Location: register_page.php");
        }
    }
?>