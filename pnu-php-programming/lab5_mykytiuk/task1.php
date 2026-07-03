<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 1</title>
    </head>
    <body>
        <h3>Завдання 1</h3>
        <p>Приклад 4</p>
        <p>Читання рядків з файлу</p>
        <?php 
            $fp = fopen( "files/ex1.txt", "r" ) or die( "Не вдалося відкрити файл!" );
            while( ! feof( $fp ) ) echo( fgets( $fp, 1024 ) )."<br>"; 
        ?> 
        <hr>
        <p>Приклад 5</p>
        <p>Виведення на екран другої половини файлу</p>
        <?php 
            $f = "files/ex1.txt"; $fp = fopen( $f, "r" ) or die( "Не вдалося відкрити $f" );
            $fsize = filesize( $f ); 
            $half =(int)( $fsize / 2 ); 
            fseek( $fp, $half ); 
            echo( fread( $fp,($fsize - $half) ) );
        ?> 
        <hr>
        <p>Приклад 6</p>
        <p>Запис і додавання в файл</p>
        <?php 
            $fp = fopen( "files/ex2.txt", "w" ) or die( " Не вдалося відкрити файл " ); 
            fputs( $fp, " Запис в файл \n" ); 
            fclose( $fp );
            $fp = fopen( "files/ex2.txt", "a" ) or die( " Не вдалося відкрити файл " );
            fputs( $fp, " Додавання в кінець файлу " ); fclose( $fp );
        ?> 
        <hr>
        <p>Приклад 7</p>
        <p>Блокування файлу</p>
        <?php 
            $fp = fopen( "files/ex1.txt", "a" ) or die( " Не вдалося відкрити файл " );
            flock( $fp, 2 ); // Повне блокування
            fputs( $fp, " Запис в файл \n" ); 
            flock( $fp, 3 ); // Розблокування 
            fclose( $fp ); 
        ?>
        <p>Приклад 8</p>
        <?php
            $targetDirectory = 'files/'; // Папка для завантаження файлів

            if (!file_exists($targetDirectory)) {
                mkdir($targetDirectory, 0777, true); // Створюємо папку, якщо її не існує
            }

            if ($_FILES) {
                $file = $_FILES['file'];
                $fileName = $file['name'];
                $targetPath = $targetDirectory . basename($fileName);

                if (move_uploaded_file($file['tmp_name'], $targetPath)) {
                    echo "Файл \"$fileName\" успішно завантажено.";
                } else {
                    echo "Сталася помилка при завантаженні файлу.";
                }
                echo "<p>Оригінальна назва: " . $_FILES['file']['name'] . "</p>";
                echo "<p>Тип файлу: " . $_FILES['file']['type'] . "</p>";
                echo "<p>Розмір: " . $_FILES['file']['size'] . "</p>";
                echo "<p>Тимчасове ім'я: " . $_FILES['file']['tmp_name'] . "</p>";
            }
        ?>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file" />
            <input type="submit" value="Завантажити" />
        </form>
        <h3 class='back'><a href='lab5.php'>Назад</a></h3>
    </body>
</html>