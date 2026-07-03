<?php 
require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/lab11_mykytiuk/includes/db.php';

// Загальна вартість товарів на складі
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $sql = "SELECT SUM(price * quantity) AS total FROM mykytiuk_storage";
    $result = $db_server->query($sql);
    $row = $result->fetch_assoc();
    $total = $row['total'];
    echo "<div class='total-sum-container'>";
    echo "<div class='total-sum'>Загальна вартість товарів на складі: $total</div>";
    echo "<button class='total-sum__close'>Приховати аудит</button>";
    echo "</div>";
}
?>