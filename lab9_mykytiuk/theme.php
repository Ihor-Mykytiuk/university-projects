<?php require '../config.php'; ?>
<html>
    <head>
        <title>Тематика новин</title>
        <style>
            .content {
                width: 1200px;
                margin: 0 auto;
                padding: 0 15px;
            }
            .theme-title {
                font-size: 24px;
                margin: 0 0 20px 0;
            }
            .news-title {
                font-size: 18px;
                margin: 0 0 10px 0;
            }
            .news-title__link {
                text-decoration: none;
                color: #000;
            }
            .news-title__link:hover {
                text-decoration: underline;
            }
            
        </style>
    </head>
    <body>
        <div class="content">
        <?php
            $theme = $_GET['theme'];
            $result = mysqli_query($db_server, "SELECT * FROM mykytiuk_ihor_news WHERE theme='$theme'");
            
            if (mysqli_num_rows($result) > 0) {
                echo "<h2 class='theme-title'>$theme</h2>";
                while ($row = mysqli_fetch_array($result)) {
                    echo "<h2 class='news-title'><a class='news-title__link' href='news.php?id=".$row['id']."'>".$row['title']."</a></h2><br>";
                    
                    
                }
            } else {
                echo "<p>Новини відсутні</p>";
            }
        ?>
        </div>
        <h3 class='back'><a href='lab9.php'>Назад</a></h3>
    </body>
</html>