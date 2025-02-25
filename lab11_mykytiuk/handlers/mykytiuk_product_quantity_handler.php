<?php
require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/lab11_mykytiuk/includes/db.php';
session_start();
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $id = $_GET['id'];
    $quantity = $_POST['quantity'];
    $sql = "SELECT * FROM mykytiuk_storage WHERE id = '$id'";
    $result = $db_server->query($sql);
    $row = $result->fetch_assoc();
    $currentQuantity = $row['quantity'];
    
    if ($_POST['add']) {
        $newQuantity = $currentQuantity + $quantity;
    } elseif ($_POST['buy']) {
        $newQuantity = $currentQuantity - $quantity;
        if ($newQuantity < 0) {
            $newQuantity = $currentQuantity;
        } else {
            $id = $_GET['id'];
            if (isset($_SESSION['cart'][$id])) {
                $_SESSION['cart'][$id] += $quantity;
            } else {
                $_SESSION['cart'][$id] = $quantity;
            }
        }
    }
    
    $sql = "UPDATE mykytiuk_storage SET quantity = $newQuantity WHERE id = '$id'";
    if ($db_server->query($sql) === TRUE) {
        echo "success";
    } else {
        echo "Помилка: " . $sql . "<br>" . $db_server->error;
    }
    
    header("Location: " . $_SERVER['HTTP_REFERER']);
}
?>