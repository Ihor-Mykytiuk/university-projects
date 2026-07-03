<? require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/config.php'; ?>
<?php
session_start(); 
    if (!isset($_SESSION['login'])) {
        echo "<p>Ви увійшли як гість</p>";
    } else {
        echo "<p>Ви увійшли як користувач ".$_SESSION['login']."</p>";
    }
    echo "<a href='index.php'>На головну</a>";
    echo "<a href='secret_info.php'>Перейти на secret_info.php</a>";
?>