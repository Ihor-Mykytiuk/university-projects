<? require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/config.php'; ?>
<?php
session_start(); // створюємо нову сесію 
// або відновлюємо поточну 

if (!isset($_GET['go'])){
    echo "<form>
    Login: <input type=text name=login>
    Password: <input type=password name=passwd>
    <input type=submit name=go value=Go>
    </form>";
}else {
    $sql = "SELECT * FROM user_for_session WHERE login='".$_GET['login']."' AND password='".$_GET['passwd']."'";
    $result = $db_server->query($sql);
    if ($result->num_rows > 0) {
        $_SESSION['login'] = $_GET['login'];
        $_SESSION['passwd'] = $_GET['passwd'];
        header("Location: secret_info.php");
    } else {
        echo "Неправильний логін або пароль";
    }
}
print_r($_SESSION); // виводимо усі змінні сесії
?>
<?php 
    if (!isset($_SESSION['login'])) {
      echo "<p>Ви увійшли як гість</p>";
    } else {
      echo "<p>Ви увійшли як користувач ".$_SESSION['login']."</p>";
    }
?>