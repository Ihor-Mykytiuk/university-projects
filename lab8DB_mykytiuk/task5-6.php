<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 5-6</title>
        <style>
            body {
                background: #faf8f5;
            }
            [class*="__container"] {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 15px;
            }
            .warehouse__items {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                gap: 30px;
            }
            .warehouse__item {
                padding: 15px;
                background-color: #fff;
            }
            .item-warehouse__image {
                width: 100%;
                height: auto;
            }
            .item-warehouse__id {
                font-size: 14px;
                color: #666;
            }
            .item-warehouse__title {
                font-size: 26px;
                margin: 15px 0;
                color: #000;
            }
            .item-warehouse__price-quantity {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin: 10px 0;
            }
            .item-warehouse__price {
                font-weight: 700;
                font-size: 22px;
                color: #817A68;
            }
            .item-warehouse__quantity {
                font-size: 16px;
                color: #666;
            }
            

        </style>
    </head>
    <body>
        <h3>Завдання 5-6</h3>
        <section class="warehouse"> 
            <div class="warehouse__container">
                <h2 class="warehouse__title">Склад кондитерських виробів</h2>
                <div class="warehouse__items">
                    <?php
                    /*
                    mysqli_query($db_server, "DROP TABLE warehouse");
                    mysqli_query($db_server, "CREATE TABLE IF NOT EXISTS warehouse(id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(250), image_name VARCHAR(250), price DECIMAL(10, 2), amount INTEGER)");
                    mysqli_query($db_server, "ALTER TABLE warehouse CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci");

                    mysqli_query($db_server, "INSERT INTO warehouse (name, image_name, price, amount) VALUES ('Торт Київський', 'kyiv.png', 493.65, 10)");
                    mysqli_query($db_server, "INSERT INTO warehouse (name, image_name, price, amount) VALUES ('Торт Золотий Ключик', 'golden_key_cake.png', 288.75, 5)");
                    mysqli_query($db_server, "INSERT INTO warehouse (name, image_name, price, amount) VALUES ('Торт Грильяж', 'grilyazh_cake.png', 439.85, 15)");
                    mysqli_query($db_server, "INSERT INTO warehouse (name, image_name, price, amount) VALUES ('Торт Трюфельний', 'truffle_cake.png', 298.25, 7)");
                    mysqli_query($db_server, "INSERT INTO warehouse (name, image_name, price, amount) VALUES ('Торт Медовик', 'medovik_cake.jpg', 199.99, 20)");
                    */
                        $query_res = mysqli_query($db_server, "select * from warehouse");
                        if (mysqli_num_rows($query_res) > 0) {
                            while($row = mysqli_fetch_assoc($query_res)) {
                                echo "
                                <div class='warehouse__item item-warehouse'>
                                    <a href='info_page.php?id={$row['id']}'><img src='files/{$row['image_name']}' alt='{$row['name']}' class='item-warehouse__image'></a>
                                    <div class='item-warehouse__id'>ID: {$row['id']}</div>
                                    <a href='info_page.php?id={$row['id']}'><h3 class='item-warehouse__title'>{$row['name']}</h3></a>
                                    <div class=item-warehouse__price-quantity>
                                        <div class='item-warehouse__price'>Ціна: {$row['price']} грн</div>
                                        <div class='item-warehouse__quantity'>Кількість: {$row['amount']} шт</div>
                                    </div>
                                </div>";
                            }
                        } else {
                            echo "0 results";
                        }
                    ?>
                </div>
            </div>
        </section>
        <h3 class='back'><a href='lab8_DB.php'>Назад</a></h3>
    </body>
</html>