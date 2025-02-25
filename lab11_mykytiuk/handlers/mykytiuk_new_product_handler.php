<?php
require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/lab11_mykytiuk/includes/db.php';
session_start();

$targetDirectory = '../images/';

if (!file_exists($targetDirectory)) {
    mkdir($targetDirectory, 0777, true);
}

if ($_POST) {
    $name = $_POST['name'];
    $price = $_POST['price'];
    $quantity = $_POST['quantity'];
    
    if ($_FILES) {
        $file = $_FILES['file'];
        $fileName = $file['name'];
        $baseName = basename($fileName);
        $targetPath = $targetDirectory . $baseName;

        if (move_uploaded_file($file['tmp_name'], $targetPath)) {
            $sql = "INSERT INTO mykytiuk_storage (name, price, quantity, image) VALUES ('$name', '$price', '$quantity', 'images/$baseName')";
            if ($db_server->query($sql) === TRUE) {
                echo "success";
            } else {
                echo "Помилка: " . $sql . "<br>" . $db_server->error;
            }
        }
    }
    else {
        echo "файлу немає";
    }

    
}