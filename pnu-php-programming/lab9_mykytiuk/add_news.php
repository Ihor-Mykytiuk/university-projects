<?php
    require '../config.php';
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Отримання даних з форми
        $theme = $_POST['theme'];
        $title = $_POST['title'];
        $content = $_POST['content'];
        $date_published = date("Y-m-d H:i:s");
    
        // Підготовка SQL-запиту для додавання новини в базу даних
        $sql = "INSERT INTO mykytiuk_ihor_news (theme, title, content, date_published) VALUES ('$theme', '$title', '$content', '$date_published')";
        
        // Виконання SQL-запиту
        if ($db_server->query($sql) === TRUE) {
            // Перенаправлення на попередню сторінку
            
            header("Location: {$_SERVER['HTTP_REFERER']}");
            exit;
        } else {
            echo "Помилка: " . $sql . "<br>" . $db_server->error;
        }

        // Закриття з'єднання з сервером БД
        mysqli_close($db_server);

    }else{
        echo "Помилка доступу";
    }
    ?>