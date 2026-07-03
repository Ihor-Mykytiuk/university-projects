<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 2</title>
    </head>
    <body>
        <h3>Завдання 2</h3>
        <form action="task2.php" method="post">
            Введіть ім'я файлу, щоб перевірити чи він існує: <br>
            <label for="file_name">Ім'я файлу: </label>
            <input type="text" name="file_name" id="file_name">
            <span style="color:gray">Приклад: lab5.php</span>
            <br>
            <input type="submit" value="Готово">
        </form>
        <?php
            if (isset($_POST['file_name'])) {
                if (!empty($_POST['file_name'])) {
                    $file_name = $_POST['file_name'];
                    if (file_exists($file_name)) {
                        echo "Файл з іменем $file_name у поточному каталозі існує";
                        echo "<br>Розмір файлу: ".filesize($file_name) . " байт";
                        echo "<br>Час створення файлу: ".date("F d Y H:i:s.", filectime($file_name));
                        echo "<br>Час останньої модифікації файлу: ".date("F d Y H:i:s.", filemtime($file_name));
                        echo "<br>Вміст файлу: <br>".file_get_contents($file_name);
                    } else {
                        echo "Файл з іменем $file_name у поточному каталозі не існує";
                    }
                    
                } else {
                    echo "Поле не може бути пустим";
                }
            }
        ?>
        <h3 class="back"><a href="lab5.php">Назад</a></h3>
    </body>
</html>

    