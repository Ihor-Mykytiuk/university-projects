<?php
    require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/config.php';
?>
<html>
    <head>
        <title>
            Зареєстровані користувачі
        </title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <link rel="stylesheet" href="http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/styles/style.css">
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
            <main class="page">
                <div class="page__registered-users registered-users">
                    <div class="registered-users__container">
                        <h2 class="registered-users__title">Зареєстровані користувачі</h2>
                        <table class="registered-users__table">
                            <tr>
                                <th>Ім'я</th>
                                <th>Прізвище</th>
                                <th>Email</th>
                                <th>Пароль</th>
                                <th>Роль</th>
                            </tr>
                            <?php
                            $sql = "SELECT * FROM mykytiuk_users";
                            $result = $db_server->query($sql);
                            while ($row = $result->fetch_assoc()) {
                                echo "<tr>";
                                echo "<td>" . $row['name'] . "</td>";
                                echo "<td>" . $row['lastname'] . "</td>";
                                echo "<td>" . $row['email'] . "</td>";
                                echo "<td>" . $row['password'] . "</td>";
                                echo "<td>" . $row['role'] . "</td>";
                                echo "</tr>";
                            }
                            ?>
                        </table>
                    </div>
                </div>
            </main>
            <div class="form-container"></div><div id="overlay" class="hidden"></div>
        </div>
        <script src="../scripts/script.js"></script>
    </body>
</html>
