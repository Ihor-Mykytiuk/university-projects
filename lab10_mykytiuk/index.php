<? require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/config.php'; ?>
<html>
<head><title>My home page</title></head>
<body>
  
<p> Привіт всім! Мене звуть Василь Василенко і це моя домашня сторінка.</p>
<a href="authorize.php">Для Петра</a> <br>
</body>

<?php
session_start();
unset($_SESSION['passwd']); // знищуємо пароль
unset($_SESSION['login']); // знищуємо логін
print_r($_SESSION); // виводимо глобальні змінні сесії
?>
<?php 
    if (!isset($_SESSION['login'])) {
      echo "<p>Ви увійшли як гість</p>";
    } else {
      echo "<p>Ви увійшли як користувач ".$_SESSION['login']."</p>";
    }
  ?>
  <a href="register_page.php">Реєстрація</a>
  <a href="cookies_tasks.php">Реалізація прикладів з cookie</a>

<hr>
</html>
<?
session_start(); // ініціалізували сесію
$test = "Змінна сесії";
$_SESSION['test']= $test; // реєструємо змінну 
	 // $test. якщо register_globals=on, то можна
 // використати session_register('test');
print_r($_SESSION);// виводимо усі глобальні змінні 
echo session_id();// виводимо ідентифікатор сесії
echo "<hr>";
session_unset();// знищуємо глобальні змінні сесії
print_r($_SESSION);
echo session_id();
echo "<hr>";
session_destroy(); // знищуємо сесію
print_r($_SESSION);
echo session_id();
?>

