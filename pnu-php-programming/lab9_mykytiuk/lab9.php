<?php
    require '../config.php';
?>
<html>
    <head>
        <title>Лабораторна робота 9</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 5px;
                text-align: left;
            }
            .news-title {
                font-size: 20px;
                font-weight: bold;
            }
            .news-item {
                font-size: 16px;
                font-weight: normal;
                color: #000;
            }
            .add-news-form-title {
                font-size: 20px;
                font-weight: bold;
            }
            .add-news-form {
                width: 50%;
                margin: 0 auto;
            }
            #add-news-theme, #add-news-title {
                width: 100%;
                padding: 12px 20px;
                margin: 8px 0;
                display: inline-block;
                border: 1px solid #ccc;
                box-sizing: border-box;
            }
            #add-news-content {
                width: 100%;
                padding: 12px 20px;
                margin: 8px 0;
                display: inline-block;
                border: 1px solid #ccc;
                box-sizing: border-box;
                height: 200px;
            }
            .submit-add-news {
                background-color: #4CAF50;
                color: white;
                padding: 14px 20px;
                margin: 8px 0;
                border: none;
                cursor: pointer;
                width: 100%;
            }
            .submit-add-news:hover {
                opacity: 0.8;
            }
        </style>
    </head>
    <body>
        <h1>Лабораторна робота 9</h1>
        <?php
            // Задвання 1
            // Видалення таблиці mykytiuk_ihor_news, якщо вона існує
            /*mysqli_query($db_server, "DROP TABLE IF EXISTS mykytiuk_ihor_news");

            // Видалення послідовності mykytiuk_ihor_news_seq, якщо вона існує
            //mysqli_query($db_server, "DROP SEQUENCE IF EXISTS mykytiuk_ihor_news_seq");

          
            // Створення таблиці mykytiuk_ihor_news з відповідними полями
            mysqli_query($db_server, "CREATE TABLE mykytiuk_ihor_news (
                id INT AUTO_INCREMENT PRIMARY KEY, -- Порядковий номер
                theme VARCHAR(100), -- Тематика
                title VARCHAR(250) UNIQUE, -- Заголовок (унікальний)
                content TEXT, -- Контент
                date_published DATETIME -- Дата публікації
            );            
            ");
            // Переведення до UTF-8
            mysqli_query($db_server, "ALTER TABLE mykytiuk_ihor_news CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci");*/

            // Задвання 2
            /*
            $file_path = 'files/news.txt';
            $file = fopen($file_path, 'r');
            $file_content = file_get_contents('files/news.txt');
            $file_content = trim($file_content); // видаляємо зайві пробіли з початку і кінця рядка

            $news = explode("&", $file_content);
            fclose($file);
            // Занести дані з файлу в таблицю
            foreach ($news as $news_item) {
                $news_item = explode("~", $news_item);
                $theme = trim($news_item[0]);
                $title = trim($news_item[1]);
                $content = trim($news_item[2]);
                $date_published = trim($news_item[3]);
                mysqli_query($db_server, "INSERT INTO mykytiuk_ihor_news (theme, title, content, date_published) VALUES ('$theme', '$title', '$content', '$date_published')");
            }*/

            // Задвання 3
            // Додати самостійно по 1 новині кожної тематики
/*
            // Політика
            $theme = mysqli_real_escape_string($db_server, 'Політика');
            $title = mysqli_real_escape_string($db_server, 'У Чехії кажуть, що в межах її ініціативи Україна потенціasdйно може отримати 1,5 млн снарядів');
            $content = mysqli_real_escape_string($db_server, 'Міністр закордонних справ Чехії Ян Ліпавський заявив, що очолювана Прагою ініціатива, яка передбачає закупівлю близько 800 тисяч снарядів за межами Євросоюзу, приносить свої плоди. Як пише "Європейська правда", про це повідомляє Bloomberg. "Ми можемо зробити набагато більше, ніж спочатку оголошена кількість (у 800 тисяч)", – сказав Ліпавський, назвавши як потенційний обсяг 1,5 мільйона снарядів. За його словами, чеська ініціатива сама по собі не буде достатньою для підтримки України, і фінансування перших поставок потрібно до того, як відправлять вантажі.');
            $date_published = mysqli_real_escape_string($db_server, '2024-03-26 16:52:00');

            mysqli_query($db_server, "INSERT INTO mykytiuk_ihor_news (theme, title, content, date_published) VALUES ('$theme', '$title', '$content', '$date_published')");
            
            //Економіка
            $theme = mysqli_real_escape_string($db_server, 'Економіка');
            $title = mysqli_real_escape_string($db_server, 'В Угорщині вирішили не забороняти імпорт українського меду');
            $content = mysqli_real_escape_string($db_server, 'Угорщина не запроваджуватиме нову заборону на ввезення меду з України, незважаючи на вимоги виробників меду, які розпочали протести, заявивши, що дешевий мед з України знизив ціни та погрожує їх бізнесу. Про це повідомляє Reuters. Минулого року уряд премєр-міністра Віктора Орбана ввів заборону на імпорт 24 аграрних продуктів з України, включаючи зерно, свинину, а також мед. 19 лютого він скасував заборону на імпорт меду, що викликало протести близько 22 тис. бджолярів країни.');
            $date_published = mysqli_real_escape_string($db_server, '2024-03-26 16:50:00');
            
            mysqli_query($db_server, "INSERT INTO mykytiuk_ihor_news (theme, title, content, date_published) VALUES ('$theme', '$title', '$content', '$date_published')");

            // Події
            $theme = mysqli_real_escape_string($db_server, 'Події');
            $title = mysqli_real_escape_string($db_server, 'СБУ затримали лідерів міжнародної банди, яка продавала наркотики до ЄС');
            $content = mysqli_real_escape_string($db_server, 'За допомогою спеціальної операції, проведеної в Києві та Запоріжжі, було затримано сім осіб, що входили до складу наркокартелю, включно з трьома основними організаторами. Лідери банди раніше переховувалися в одній з країн Балканського регіону, звідки вони й керували нелегальними операціями.Злочинці організували продаж великих партій метадону, який вони отримували від постачальників з різних областей України, до ЄС. Для транспортування наркотиків до Європи вони використовували мережу кур’єрів, які перевозили наркотики, зашиваючи їх у одяг або ховаючи серед особистих речей у багажі.Після перетину кордону, наркотики продавалися іноземним співучасникам для подальшого розповсюдження в Європі. Організатори наркобізнесу планували отримувати від цього доходи в розмірі 10-12 мільйонів гривень щомісяця.Однак, завдяки зусиллям СБУ, злочинців було затримано під час спроби контрабанди понад одного кілограма наркотиків за кордон.');
            $date_published = mysqli_real_escape_string($db_server, '2024-03-26 16:32:00');

            mysqli_query($db_server, "INSERT INTO mykytiuk_ihor_news (theme, title, content, date_published) VALUES ('$theme', '$title', '$content', '$date_published')");

            // Технології
            $theme = mysqli_real_escape_string($db_server, 'Технології');
            $title = mysqli_real_escape_string($db_server, 'Starlink для російських військ в Україні купують у США на eBay');
            $content = mysqli_real_escape_string($db_server, 'На офіційній мапі покриття вказано, що Starlink працює на тимчасово окупованих росією територіях Херсонської, Запорізької областей, так само як і в окупованих частинах Донецької та Луганської областей. Онлайн-магазини відкрито рекламують систему. На сайті навіть розміщено списки людей з американських штатів Огайо та Нью-Джерсі, які продають термінали Starlink на eBay. Крім того, постачання в Росію, а також в інші зони бойових дій, наприклад Судан і Ємен, йдуть через ОАЕ, країни Центральної Азії та Африки, де посередники закуповують їх на чорному ринку, зясувала WSJ.');
            $date_published = mysqli_real_escape_string($db_server, '2024-04-13 12:41:00');

            mysqli_query($db_server, "INSERT INTO mykytiuk_ihor_news (theme, title, content, date_published) VALUES ('$theme', '$title', '$content', '$date_published')");
            */
            // Вивести у вигляді таблиці
            $result = mysqli_query($db_server, "SELECT * FROM mykytiuk_ihor_news");
            echo "<table border='1'>";
            echo "<tr><th>id</th><th>theme</th><th>title</th><th>content</th><th>date_published</th></tr>";
            while ($row = mysqli_fetch_array($result)) {
                echo "<tr>";
                echo "<td>".$row['id']."</td>";
                echo "<td>".$row['theme']."</td>";
                echo "<td>".$row['title']."</td>";
                echo "<td>".$row['content']."</td>";
                echo "<td>".$row['date_published']."</td>";
                echo "</tr>";
            }
            echo "</table>";

            echo "<br>";
            echo "<h3>Завдання 4</h3>";

            // Вивести спочатку три найновіші новини
            $result = mysqli_query($db_server, "SELECT * FROM mykytiuk_ihor_news ORDER BY date_published DESC LIMIT 3");
            echo "<a href='#' class='news-title'>Головне</a><br>";
            while ($row = mysqli_fetch_array($result)) {
                echo "<a class='news-item' href='news.php?id=".$row['id']."'>".$row['title']."</a> Дата публікації: ".$row['date_published']."<br> ";
            }
            
            //Виводити решту тем, по темах
            $result = mysqli_query($db_server, "SELECT DISTINCT theme FROM mykytiuk_ihor_news");
            while ($row = mysqli_fetch_array($result)) {
                $theme = $row['theme'];
                echo "<a class='news-title' href='theme.php?theme=".$row['theme']."'>".$row['theme']."</a><br>";
                $result_news = mysqli_query($db_server, "SELECT * FROM mykytiuk_ihor_news WHERE theme='$theme' ORDER BY date_published DESC LIMIT 2");
                while ($row_news = mysqli_fetch_array($result_news)) {
                    echo "<a class='news-item' href='news.php?id=".$row_news['id']."'>-".$row_news['title']."</a> Дата публікації: ".$row_news['date_published']."<br> ";
                }
            }
            // Записати кількість новин в файл out.txt
            $result = mysqli_query($db_server, "SELECT COUNT(*) as total FROM mykytiuk_ihor_news");
            $row = mysqli_fetch_assoc($result);
            $total = $row['total'];
            file_put_contents('files/out.txt', $total);

            // Завдання 5
            // Запит, який би видалив з таблиці m_news новину, яка має порядковий номер 5. 
            //mysqli_query($db_server, "DELETE FROM mykytiuk_ihor_news WHERE id=5");
            
            // Вивести на сторінку всі записи із таблиці ihor_mykytiuk_news
            echo "<br>";
            $result = mysqli_query($db_server, "SELECT * FROM mykytiuk_ihor_news");
            echo "<table border='1'>";
            echo "<tr><th>id</th><th>theme</th><th>title</th><th>date_published</th></tr>";
            while ($row = mysqli_fetch_array($result)) {
                echo "<tr>";
                echo "<td>".$row['id']."</td>";
                echo "<td>".$row['theme']."</td>";
                echo "<td>".$row['title']."</td>";
                echo "<td>".$row['date_published']."</td>";
                echo "</tr>";
            }
            echo "</table>";
            
            echo "<h3>Завдання 6</h3>";
            echo "<p class='add-news-form-title'>Форма для додавання новини</p>";
            echo "<form class='add-news-form' action='add_news.php' method='post'>";
            echo "<label for='theme'>Тематика:</label><br>";
            echo "<input type='text' id='add-news-theme' name='theme'><br>";
            echo "<label for='title'>Заголовок:</label><br>";
            echo "<input type='text' id='add-news-title' name='title'><br>";
            echo "<label for='content'>Контент:</label><br>";
            echo "<textarea id='add-news-content' name='content'></textarea><br>";
            echo "<input class='submit-add-news' type='submit' value='Додати новину'>";
            echo "</form>";
            
        ?>
    </body>
</html>