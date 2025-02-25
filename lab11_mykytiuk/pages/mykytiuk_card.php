<?php
session_start();
?>
<div class="cart__items">
    <h2 class="cart__title">Кошик</h2>
    <?php
    if (isset($_SESSION['cart']) && !empty($_SESSION['cart'])) {
        require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/config.php'; // Підключення до бази даних
        foreach ($_SESSION['cart'] as $id => $quantity) {
            $sql = "SELECT * FROM mykytiuk_storage WHERE id = '$id'";
            $result = $db_server->query($sql);
            if ($result && $row = $result->fetch_assoc()) {
                echo "<div class='cart__item cart-item'>";
                    echo "<img src='http://mykytiukihor.infinityfreeapp.com/lab11_mykytiuk/" . $row['image'] . "' alt='product image' class='cart-item__image'>";
                    echo "<div class='cart-item__info'>";
                        echo "<h3 class='cart-item__name'>" . $row['name'] . "</h3>";
                        echo "<p class='cart-item__id'>ID: " . $row['id'] . "</p>";
                        echo "<p class='cart-item__price'>Ціна: " . $row['price'] . " грн</p>";
                    echo "</div>";
                    echo "<div class='cart-item__quantity-info info-quantity'>";
                        echo "<p class='info-quantity__title'>К-СТЬ</p>";
                        echo "<p class='info-quantity__quantity'>" . $quantity . "</p>";
                    echo "</div>";
                    echo "<div class='cart-item__remove-button' data-id='" . $row['id'] . "'>X</div>";
                    echo "<hr>";
                echo "</div>";
            }
        }
        
        echo "<div class='cart__total-price'>";
        
        $total_price = 0;
        foreach ($_SESSION['cart'] as $id => $quantity) {
            $sql = "SELECT * FROM mykytiuk_storage WHERE id = '$id'";
            $result = $db_server->query($sql);
            if ($result && $row = $result->fetch_assoc()) {
                $total_price += $row['price'] * $quantity;
            }
        }
        echo "<p>Загальна вартість: " . $total_price . " грн</p>";
        echo "</div>";
    } else {
        echo "<p>Ваш кошик порожній.</p>";
    }     
      
    ?>
    <div class="cart__close-button">X</div>
</div>