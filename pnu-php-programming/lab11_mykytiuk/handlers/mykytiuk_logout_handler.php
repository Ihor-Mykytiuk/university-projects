<?php
require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/lab11_mykytiuk/includes/db.php';
// logout.php
session_start();

// Закінчення сесії
session_unset();
session_destroy();
?>
