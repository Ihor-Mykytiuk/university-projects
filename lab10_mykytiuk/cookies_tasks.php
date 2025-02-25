<? require '/home/vol9_5/infinityfree.com/if0_35997431/htdocs/config.php'; ?>
<html>
    <head>
        <title>Реалізація прикладів з cookies</title>
    </head>
    <body>
        <h1>Реалізація прикладів з cookies</h1>
        <?php
        // Встановлюємо Cookie до кінця сесії:
        SetCookie("Test","Value");
        // Встановлюємо Cookie на одну годину 
        //після установки:
        SetCookie("My_Cookie","Value",time()+3600);
        ?>

        <?php
        // Cookies встановити не вдасться, оскільки
        // перед відправкою заголовка Cookie ми виводимо
        // у браузер рядок 'Hello':
        echo "Hello";
        // Функція SetCookie поверне FALSE:
        if(SetCookie("Test","Value")) 
        echo "<h3>Cookie успішно встановлено!</h3>";
        else echo "<h3>Cookie встановити не вдалося!</h3>";
        ?>

        <?php
        echo $_COOKIE['my_cookie'];
        // Виводить значення встановленою
        // Cookie 'My_Cookie'
        ?>
        
        <?php
        // Встановлюємо Cookie 'test' зі значенням 
        // 'Hello' на одну годину:
        setcookie("test", " Hello world!", time()+3600);
        // При наступному запиті скрипта виводить ' Hello world!':
        echo @$_COOKIE['test'];
        ?>

        <?php
        // Перевіряємо, чи був вже встановлений 
        // Cookie 'Mortal'. Якщо так, то читаємо його
        // значення і збільшуємо значення 
        // лічильника звернень до сторінки:
        if (isset($_COOKIE['Mortal']))
        $cnt=$_COOKIE['Mortal']+1;
        else $cnt=0;
        // Встановлюємо Cookie 'Mortal' із значенням
        // лічильника p часом "життя" до 18/07/29,
        // Тобто на дуже довгий час:
        setcookie("Mortal",$cnt, 0x6FFFFFFF);
        // Виводить число відвідувань цієї сторінки :
        echo "<p>Ви відвідували цю сторінку <b>". @$_COOKIE['Mortal']. "</b> раз</p>";
        ?>

        <?php
        // Видаляємо Cookie 'Test ':
        SetCookie("Test","");
        ?>

        <?php
        // Встановлюємо масив Cookies :
        setcookie("cookie[1]","Перший");
        setcookie("cookie[2]","Другий");
        setcookie("cookie[3]","Третій");
        // Після перезавантаження сторінки ми відобразимо
        // Склад масиву Cookies 'cookie ':
        if (isset($_COOKIE['cookie'])){
            foreach ($_COOKIE['cookie'] as $name => $value) {
                echo "$name: $value <br>";
            }
        }
    ?>
    <h3 class="back"><a href="index.php">Назад</a></h3>
    </body>

</html>