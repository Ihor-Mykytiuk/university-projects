<?php
require '../config.php';
?>
<html>
    <head>
        <title>Завдання 6</title>
    </head>
    <body>
        <h3>Завдання 6</h3>
        <p>6.11</p>
        <?php
            $text_6_11 = "Мова програмування - система позначень для опису алгоритмів і структур даних.
            Мова програмування визначає набір лексичних, синтаксичних та семантичних правил, які задають зовнішній вигляд програми і дії, які виконує комп'ютер під її управлінням.";
            //Визначити кількість входжень слів з першого речення у другий.
            function count_word_matches($text) {
                $text = str_replace("\n", " ", $text);
                $sentences = explode(".", $text);
                $first_sentence = explode(" ", $sentences[0]);
                $second_sentence = explode(" ", $sentences[1]);
                $matches = 0;
                foreach ($first_sentence as $word) {
                    if (in_array($word, $second_sentence)) {
                        $matches++;
                    }
                }
                echo "<p>Кількість входжень слів з першого речення у друге: $matches</p>";
            }
            count_word_matches($text_6_11);
        ?>
        <p>6.12</p>
        <?php
            $text_6_12 = "
            PHP інтерпретується веб-сервером в HTML-код, який передається на сторону клієнта. На відміну від таких скриптових мов програмування, як JavaScript, користувач не має доступу до PHP-коду, що є перевагою з точки зору безпеки, але значно погіршує інтерактивність сторінок
            ";
            // Потроїти кожне входження символу «P» в кожному слові
            function triple_p($text) {
                $text = str_replace("\n", " ", $text);
                $words = explode(" ", $text);
                $new_text = str_replace("P", "PPP", $text);
                
                echo "<p>Текст після потроєння символу «P» в кожному слові:</p>";
                echo $new_text;
            }
            triple_p($text_6_12);
        ?>
        <p>6.13</p>
        <?php
            $text_6_13 = "
            У більшості візуальних середовищ програмування реалізовано функції автоматичної генерації коду. Традиційно автоматична генерація коду використовується для створення форм, кнопок, перемикачів та інших візуальних елементів. Деякі сучасні середовища можуть автоматично генерувати мало не будь-які фрагменти програм, а то навіть і цілі програми.
            ";
            //Вивести на екран речення у якому знаходиться слово «програмування».
            function print_sentence_with_word($text, $word) {
                $text = str_replace("\n", " ", $text);
                $sentences = explode(".", $text);
                foreach ($sentences as $sentence) {
                    if (strpos($sentence, $word) !== false) {
                        echo "<p>Речення, у якому знаходиться слово «$word»:</p>";
                        echo $sentence;
                        break;
                    }
                }
            }
            print_sentence_with_word($text_6_13, "програмування");
        ?>
        <h3><a href="lab5.php">Назад</a></h3>
    </body>
</html>



    