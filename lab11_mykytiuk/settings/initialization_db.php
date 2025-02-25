<?php
// initialization_db.php
$sql_storage = "CREATE TABLE IF NOT EXISTS mykytiuk_storage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL,
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";
$sql_users = "CREATE TABLE IF NOT EXISTS mykytiuk_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('Seller', 'Buyer') NOT NULL
)";

if ($db_server->query($sql_storage) === TRUE) {
    echo "Таблиця товарів створена успішно<br>";
} else {
    echo "Помилка: " . $db_server->error . "<br>";
}

if ($db_server->query($sql_users) === TRUE) {
    echo "Таблиця користувачів створена успішно<br>";
} else {
    echo "Помилка: " . $db_server->error . "<br>";
}
// таблиці в utf8_general_ci
$db_server->query("ALTER TABLE mykytiuk_storage CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci");
$db_server->query("ALTER TABLE mykytiuk_users CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci");

$sql_storage_count = "SELECT COUNT(*) FROM mykytiuk_storage";
$sql_users_count = "SELECT COUNT(*) FROM mykytiuk_users";

$result_storage = $db_server->query($sql_storage_count);
$result_users = $db_server->query($sql_users_count);

if ($result_storage->fetch_row()[0] == 0) {
    $sql_insert_storage = "INSERT INTO mykytiuk_storage (name, image, price, quantity) VALUES 
    ('Chanel Ultra Le Teint', 'images/chanel-ultra-le-teint.webp', 3100, 10),
    ('Chanel Ombre Première', 'images/chanel-ombre-premiere.webp', 1560, 5),
    ('Chanel Joues Contraste Powder Blush', 'images/chanel-joues-contraste-powder-blush.webp', 1810, 7),
    ('Chanel La Palette Sourcils', 'images/chanel-la-palette-sourcils.webp', 1930, 3),
    ('Chanel Les 4 Ombres', 'images/chanel-les-4-ombres.webp', 2370, 4),
    ('Chanel Les Beiges Eyeshadow Palette', 'images/chanel-les-beiges-eyeshadow-palette.webp', 2940, 6)";

    if ($db_server->query($sql_insert_storage) === TRUE) {
        echo "Товари додані успішно<br>";
    } else {
        echo "Помилка: " . $db_server->error . "<br>";
    }
} 
?>