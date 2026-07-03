<?php
// Підключення до бази даних
$mysqli = new mysqli("sql200.infinityfree.com", "if0_35997431", "7hjCwdxiYx", "if0_35997431_test_db");
$mysqli->query("ALTER DATABASE if0_35997431_test_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci");
$tables = $mysqli->query("SHOW TABLES");
while ($row = $tables->fetch_row()) {
    $table = $row[0];
    $mysqli->query("ALTER TABLE $table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci");
}
// Перевірка з'єднання
if($mysqli === false){
    die("Помилка: Неможливо підключитися. " . $mysqli->connect_error);
}
$visitor_ip = $_SERVER['REMOTE_ADDR'];

// Додавання IP-адреси відвідувача до бази даних
$insert_query = "INSERT INTO visitor_ips (ip_address) VALUES ('$visitor_ip')";
if($mysqli->query($insert_query) === true){
    //echo "IP-адреса відвідувача збережена успішно.";
} else{
    //echo "Помилка: Не вдалося виконати $insert_query. " . $mysqli->error;
}
// Обробка введеної форми реєстрації
if($_SERVER["REQUEST_METHOD"] == "POST"){
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Перевірка, чи існує користувач з таким іменем
    $stmt = $mysqli->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        echo "Вибачте, користувач з іменем " . $user['username'] . " вже існує. ";
        echo "Його пароль:";
        
        echo $user['password'];
    } else {
        // Перевірка, чи існує користувач з таким паролем
        $stmt = $mysqli->prepare("SELECT * FROM users WHERE password = ?");
        $stmt->bind_param("s", $password);
        $stmt->execute();
        $result = $stmt->get_result();

        if($result->num_rows > 0) {
            $user = $result->fetch_assoc();
            echo "Вибачте, такий пароль вже зайнятий користувачем " . $user['username'] . ".";
        } else {
            // Додавання користувача до бази даних
            $stmt = $mysqli->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
            $stmt->bind_param("ss", $username, $password);
            if($stmt->execute()){
                echo "Користувач зареєстрований успішно.";
            } else{
                echo "Помилка: Не вдалося виконати запит. " . $mysqli->error;
            }
        }
    }

    // Закриття з'єднання
    $mysqli->close();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Реєстрація</title>
    <style>
        form {
            display: flex;
            flex-direction: column;
            width: 300px;

            margin: 0 auto;

            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            gap: 10px
        }

        label {
            margin-bottom: 5px;
        }

        input {
            padding: 5px;
            margin-bottom: 10px;
        }

        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
            border: none;
            padding: 10px 20px;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }

        h2 {
            text-align: center;
        }
        
    </style>
</head>
<body>
    <h2>Реєстрація</h2>
    <form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
        <label for="username">Ім'я користувача:</label>
        <input type="text" id="username" name="username" required>
        <label for="password">Пароль:</label>
        <input type="password" id="password" name="password" required>
        <input type="submit" value="Зареєструватися">
    </form>
    <?php
    // Асоціативний масив
        $arr_ass1 = array("a" => 1, "b" => 2, "c" => 3);
        $arr_ass2 = array("c" => 4, "d" => 5, "e" => 6);
        // Індексований масив
        $arr1 = array(1, 2, 3);
        $arr2 = array(4, 5, 6);
        // Об'єднання масивів різними способами
        $result_ass_plus = $arr_ass1 + $arr_ass2;
        $result_ass_merge = array_merge($arr_ass1, $arr_ass2);
        $result_ass_recursive_merge = array_merge_recursive($arr_ass1, $arr_ass2);

        $result_plus = $arr1 + $arr2;
        $result_merge = array_merge($arr1, $arr2);
        $result_merge_recursive = array_merge_recursive($arr1, $arr2);

        echo "<pre>";
        echo print_r($result_ass_plus);
        echo "<br>";
        echo print_r($result_ass_merge);
        echo "<br>";
        echo print_r($result_ass_recursive_merge);
        echo "<br>";
        echo print_r($result_plus);
        echo "<br>";
        echo print_r($result_merge);
        echo "<br>";
        echo print_r($result_recursive_merge);
        echo "<br>";
        echo "</pre>";

        echo phpversion();
        $text = "Вітаю всіх відвідув_чів! Ви вирішили зайти в наш магазин.";
preg_match_all('/\bв\p{L}*\b/ui', $text, $matches);
print_r($matches[0]);
    ?>
</body>
</html>
