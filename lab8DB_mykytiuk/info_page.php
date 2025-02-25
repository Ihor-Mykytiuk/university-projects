<?php
session_start(); // Початок сесії

require '../config.php';
?>
<html>
<head>
    <title>Інформаційна сторінка</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway&display=swap">
    <style>
        form {
            padding: 0;
            margin: 0;
        }
        body {
            background: #faf8f5;
            font-family: 'Raleway', sans-serif;
        }
        [class*="__container"] {
            width: 1200px;
            margin: 0 auto;
            padding: 0 15px;
        }
        .info {
            display: flex;
            align-items: center;
            height: 82vh;
        }
        .info__content {
            display: flex;
            align-items: center;
            justify-content: space-around;
            
        }
        .info__description {
            display: flex;
            flex-direction: column;
        }
        .info__image {
            width: 500px;
            height: auto;                
        }
        .info__title {
            font-size: 34px;
            margin: 0 0 40px 0;
            color: #000;
            font-weight: 800;
        }
        .buy-block {
            display: flex;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-top: 20px;
            padding: 15px;
            align-items: center;
            gap: 30px;
        }
        .buy-block__price {
            font-weight: 700;
            font-size: 26px;
            color: #817A68;
        }
        .buy-block__select-quantity {
            flex-grow: 1;
        }
        .buy-block__buy-button, .buy-block__add-button {
            background-color: #FFD700;
            color: #000;
            font-weight: 700;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
            transition: background-color 0.3s;
            margin-left: 10px;
        }
        .buy-block__buy-button:hover {
            background-color: #FFD700;
        }
        
        .buy-block__add-button:hover {
            background-color: #FFD700;
        }
        .message {
            font-size: 18px;
            font-weight: bold;
            margin-top: 10px;
            color: green;
        }
        input[type="number"] {
            width: 50px;
            padding: 5px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <section class="info">
        <div class="info__container">
            <div class="info__content">
                <?php
                    if(isset($_GET['id']) && is_numeric($_GET['id'])) {
                        $id = $_GET['id'];
                        $query_res = mysqli_query($db_server, "select * from warehouse where id = $id");
                        if (mysqli_num_rows($query_res) > 0) {
                            $row = mysqli_fetch_assoc($query_res);
                            echo "<img class='info__image' src='files/{$row['image_name']}' alt='{$row['title']}'>";
                            echo "<div class='info__description'>";
                                echo "<div class='info__id'>ID: {$row['id']}</div>";
                                echo "<h3 class='info__title'>{$row['name']}</h3>";
                                echo "<div class='info__amount'>Залишилось на складі: {$row['amount']} шт</div>";     
                                echo "<div class='info__buy-block buy-block'>";
                                    echo "<div class='buy-block__price'>Ціна: {$row['price']} грн</div>";
                                    echo "<form action='info_page.php?id={$row['id']}' method='post'>";
                                        echo "<input type='number' name='quantity' min='1' required>";
                                        echo "<input class='buy-block__buy-button' type='submit' name='buy' value='Купити'>";
                                        echo "<input class='buy-block__add-button' type='submit' name='add' value='Поповнити склад'>";
                                    echo "</form>";
                                echo "</div>";
                                if (isset($_SESSION['message'])) {
                                    echo "<div class='message'>{$_SESSION['message']}</div>";
                                    unset($_SESSION['message']);
                                }
                            echo "</div>";
                            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                                if (isset($_POST['buy'])) {
                                    $id = $_GET['id'];
                                    $quantity = $_POST['quantity'];
                                    $newAmount = $row['amount'] - $quantity;
                                    if ($newAmount < 0) {
                                        $_SESSION['message'] = "На складі недостатньо товару!";
                                        header("Location: {$_SERVER['PHP_SELF']}?id=$id");
                                        exit(); // Після перенаправлення слід зупинити виконання скрипту
                                    }
                                    mysqli_query($db_server, "UPDATE warehouse SET amount = $newAmount WHERE id = $id");
                                    $_SESSION['message'] = "Товар успішно куплено!";
                                    header("Location: {$_SERVER['PHP_SELF']}?id=$id");
                                    exit(); 
                                }
                                elseif (isset($_POST['add'])) {
                                    $id = $_GET['id'];
                                    $quantity = $_POST['quantity'];
                                    $newAmount = $row['amount'] + $quantity;
                                    mysqli_query($db_server, "UPDATE warehouse SET amount = $newAmount WHERE id = $id");
                                    $_SESSION['message'] = "Склад успішно поповнено!";
                                    header("Location: {$_SERVER['PHP_SELF']}?id=$id");
                                    exit(); 
                                }
                                
                            }
                        } else {
                            echo "<p>Товар не знайдено</p>";
                        }
                    }
                ?>
            </div>
        </div>
    </section>
    <h3 class='back'><a href='task5-6.php'>Назад</a></h3>
</body>
</html>
