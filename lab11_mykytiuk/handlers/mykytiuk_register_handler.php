<?php
require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/lab11_mykytiuk/includes/db.php';
session_start();
// register.php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $lastname = $_POST['surname'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $confirm_password = $_POST['password-confirm'];
    $role = $_POST['role'];    

    $sql = "SELECT * FROM mykytiuk_users WHERE email = '$email' AND role = '$role'";
    $result = $db_server->query($sql);

    if ($result->num_rows > 0) {
        echo "Користувач з таким email вже існує";
        die();
    }  
    $sql = "INSERT INTO mykytiuk_users (name, lastname, email, password, role) VALUES ('$name', '$lastname', '$email', '$password', '$role')";
    
    if ($db_server->query($sql) === TRUE) {
        echo "Реєстрація пройшла успішно";
    } else {
        echo "Помилка реєстрації, спробуйте ще раз";
    }
}
?>
