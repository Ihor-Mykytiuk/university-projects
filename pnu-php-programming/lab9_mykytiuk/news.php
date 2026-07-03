<?php require '../config.php'; ?>
<html>
    <head>
        <title>Новина</title>
        <style>
            .content {
                width: 1200px;
                margin: 0 auto;
                padding: 0 15px;
            }
            .news-title {
                font-size: 24px;
                margin: 0 0 20px 0;
            }
            .news-date {
                font-size: 14px;
                margin: 0 0 10px 0;
            }
            .news-content {
                font-size: 16px;
                margin: 0 0 20px 0;
            }
            
        </style>
    </head>
    <body>
        <div class="content">
        <?php
            $id = $_GET['id'];
            $result = mysqli_query($db_server, "SELECT * FROM mykytiuk_ihor_news WHERE id='$id'");
            $row = mysqli_fetch_assoc($result);
            echo "<h2 class='news-title'>".$row['title']."</h1>";
            echo "<p class='news-date'>".$row['date_published']."</p>";
            echo "<p class='news-content'>".$row['content']."</p>";
        ?>
        </div>
        <h3 class='back'><a href='lab9.php'>Назад</a></h3>
    </body>
</html>