<? require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/config.php'; ?>
<?php
session_start(); // створюємо нову сесію
// або відновлюємо поточну
print_r($_SESSION); // виводимо усі змінні сесії
if (!($_SESSION['login'])) {
    Header("Location: authorize.php");
}
?>
<html>
    <head>
        <title>Secret info</title>
    </head>
    <body>
        <p>Тут я хочу ділитися секретами з другом Петром.</p>
        <a href="index.php">На головну</a>
        <?php
        if (isset($_SESSION['login'])) {
            echo "<a href='secret_other.php'>Перейти на secret_other.php</a>";
        }
        ?>
    </body>
    <?php 
    if (!isset($_SESSION['login'])) {
        echo "<p>Ви увійшли як гість</p>";
    } else {
        echo "<p>Ви увійшли як користувач ".$_SESSION['login']."</p>";
    }
    ?>
</html>
