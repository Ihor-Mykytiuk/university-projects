<?php
// login.php
require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/lab11_mykytiuk/includes/db.php';
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $password = $_POST['password'];
    $role = $_POST['role'];
    
    $sql = "SELECT * FROM mykytiuk_users WHERE email = '$email' AND password = '$password' AND role = '$role'";
    $result = $db_server->query($sql);
    
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        session_start();
        $_SESSION['login'] = $row['email'];
        $_SESSION['role'] = $row['role'];
        echo "success";
    } else {
        echo "Введено невірний логін чи пароль";
    }
}