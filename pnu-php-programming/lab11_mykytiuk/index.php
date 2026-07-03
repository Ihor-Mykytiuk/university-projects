<? require '../config.php';
/*require 'settings/initialization_db.php';*/ ?>
<html>
    <head>
        <title>
            Інтернет-магазин
        </title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <link rel="stylesheet" href="styles/style.css">
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
                            } elseif ($_SESSION['role'] == 'Buyer') {
                                echo "<button class='menu__button' id='cart-button'>Кошик</button>";
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
            <main class="page">
                <div class="page__welcome welcome-page">
                    <div class="welcome-page__container">
                        <div class="welcome-page__titles">
                            <h1 class="welcome-page__title">Інтернет-магазин</h1>
                            <h2 class="welcome-page__name">Микитюк Ігор Вікторович</h2>
                            <h2 class="welcome-page__theme">Косметика</h2>
                        </div>
                    </div>
                </div>
                <div class="page__user-info user-info">
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
                <div class="page__main-content">
                    <div class="page__products products">
                        <div class="products__container">
                            <?php
                            if (isset($_SESSION['login'])) {
                                $sql = "SELECT * FROM mykytiuk_storage";
                                $result = $db_server->query($sql);

                                if ($result->num_rows > 0) {
                                    while ($row = $result->fetch_assoc()) {
                                        echo "<div class='products__item product-item'>";
                                        echo "<a href='pages/mykytiuk_product_info.php?id=" . $row['id'] . "'>";
                                        echo "<div class='product-item__image-container'>";
                                        echo "<img src='" . $row['image'] . "' alt='" . $row['name'] . "' class='product-item__image'>";
                                        echo "</div>";
                                        echo "</a>";
                                        echo "<a class='product-item__link' href='pages/mykytiuk_product_info.php?id=" . $row['id'] . "'>";
                                        echo "<h3 class='product-item__name'>" . $row['name'] . "</h3>";
                                        echo "</a>";
                                        echo "<p class='product-item__price'>" . $row['price'] . " грн</p>";
                                        echo "</div>";
                                    }
                                }
                            } else {
                            
                                $sql = "SELECT * FROM mykytiuk_storage LIMIT 4";
                                $result = $db_server->query($sql);
                            
                                if ($result->num_rows > 0) {
                                    while ($row = $result->fetch_assoc()) {
                                        echo "<div class='products__item product-item'>";
                                        echo "<div class='product-item__image-container'>";
                                        echo "<img src='" . $row['image'] . "' alt='" . $row['name'] . "' class='product-item__image'>";
                                        echo "</div>";
                                        echo "<h3 class='product-item__name'>" . $row['name'] . "</h3>";
                                        echo "<p class='product-item__price'>" . $row['price'] . " грн</p>";
                                        echo "</div>";
                                    }
                                }
                            }
                            
                            ?>
                        </div>
                    </div>
                </div>
            </main>
            <div class="form-container"></div>
            <div class="cart-container">
                <div class="cart"></div>
            </div>
            <div id="overlay" class="hidden"></div>
        </div>
        <script src="scripts/script.js"></script>
    </body>
</html>