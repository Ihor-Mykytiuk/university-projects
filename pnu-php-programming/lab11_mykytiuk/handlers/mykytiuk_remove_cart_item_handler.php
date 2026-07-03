<?php 
session_start();
if (isset($_POST['product_id'])) {
    $id = $_POST['product_id'];
    unset($_SESSION['cart'][$id]);
    echo "success";
} else {
    echo "Product ID is missing";
}
?>
