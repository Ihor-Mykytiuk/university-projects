<?php
require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/lab11_mykytiuk/includes/db.php';
session_start();
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    
    $email = $_POST['email'];
    $roles = $_POST['role'];
    $sql = "SELECT email, password FROM mykytiuk_users WHERE email = '$email' AND role IN ('" . implode("','", $roles) . "')";

// Виконання запиту до бази даних
    $result = $db_server->query($sql);

    // Перевірка наявності результатів
    if ($result->num_rows > 0) {
        // Підготовка масиву для відповіді
        $response = array();
        while($row = $result->fetch_assoc()) {
            $response[] = $row;
        }
        
        // Відправка відповіді у форматі JSON
        header('Content-Type: application/json');
        echo json_encode($response);
    } else {
        // Якщо результати не знайдено, повертаємо порожній масив
        echo json_encode(array());
    }
}
?>