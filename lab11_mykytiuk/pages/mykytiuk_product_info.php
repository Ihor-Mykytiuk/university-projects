<?php
if (!$_SERVER['REQUEST_METHOD'] == 'GET') {
    header('Location: ../index.php');
}
require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/config.php';
?>
<html>
    <head>
        <title>
            Інформація про товар
        </title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <link rel="stylesheet" href="../styles/style.css">
    </head>
    <body>
        <div class="wrapper">
            <header class="header">
                <div class="header__container">
                    <div class="header__menu menu">
                        <?php
                        session_start();
                        
                        if (isset($_SESSION['login'])) {
                            echo "<button class='menu__button' id='logout-button'>Вихід</button>";
                            if ($_SESSION['role'] == 'Seller') {
                                echo "<button class='menu__button' id='new-product-button'>Додати товар</button>";
                                echo "<button class='menu__button' id='audit-button'>Аудит</button>";
                            }
                        } else {
                            echo "<button class='menu__button' id='registration-button'>Реєстрація</button>";
                            echo "<button class='menu__button' id='login-button'>Вхід</button>";
                            echo "<button class='menu__button' id='password-recovery-button'>Забули пароль</button>";
                        }
                        ?>
                        
                        <a href="http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/pages/mykytiuk_registered_users.php" class="menu__button" id="registred-users-button">Зареєстровані користувачі</a>
                        <a href="#" class="menu__storage">
                            Склад
                        </a>
                    </div>
                </div>
            </header>
            <main class="product-info-page">
                <div class="product-info-page__user-info user-info">
                    <div class="user-info__container">
                        <?php 
                        if (isset($_SESSION['login'])) {
                            echo "<h3 class='user-info__title'>Ви увійшли як ";
                            if ($_SESSION['role'] == 'Seller') {
                                echo "продавець";
                            } elseif ($_SESSION['role'] == 'Buyer') {
                                echo "покупець";
                            }
                            $sql = "SELECT * FROM mykytiuk_users WHERE email = '" . $_SESSION['login'] . "' AND role = '" . $_SESSION['role'] . "'";
                            $result = $db_server->query($sql);
                            $row = $result->fetch_assoc();
                            //
                            echo " під іменем " . $row['name'] . " " . $row['lastname'] . "</h3>";
                        } else {
                            echo "<h3 class='user-info__title'>Ви увійшли як гість</h3>";
                        }
                        ?>
                    </div>
                </div>
                <div class="product">
                    <div class="product__container">
                        <?php
                        session_start();
                        if ($_SERVER["REQUEST_METHOD"] == "GET") {
                            $id = $_GET['id'];
                            $sql = "SELECT * FROM mykytiuk_storage WHERE id = '$id'";
                            $result = $db_server->query($sql);
                            $row = $result->fetch_assoc();
                            echo "<img src='../" . $row['image'] . "' alt='product image' class='product__image'>";
                            echo "<div class='product__info'>";
                                echo "<div class='product__id'>ID: " . $row['id'] . "</div>";
                                echo "<h2 class='product__name'>" . $row['name'] . "</h2>";
                                echo "<div class='product__quantity'>Залишок на складі: " . $row['quantity'] . " шт</div>";
                                echo "<div class='product__price'>Ціна: " . $row['price'] . " грн</div>";
                                echo "<form action='../handlers/mykytiuk_product_quantity_handler.php?id={$row['id']}' method='post' class='product__form form-product'>";
                                    echo "<input class='form-product__input' type='number' name='quantity' min='1' required>";
                                    if ($_SESSION['role'] == 'Seller') {
                                        echo "<input class='form-product__submit' type='submit' name='add' value='Додати на склад'>";
                                    } elseif ($_SESSION['role'] == 'Buyer'){
                                        echo "<input class='form-product__submit' type='submit' name='buy' value='Додати в кошик'>";
                                        echo "<a href='../index.php' class='form-product__submit'>Продовжити покупки</a>";
                                    }
                                echo "</form>";
                            echo "</div>";
                        }
                        ?>
                    </div>
                </div>
            </main>
            <div class="form-container"></div><div id="overlay" class="hidden"></div>
        </div>
        <script src="../scripts/script.js"></script>
    </body>
</html>