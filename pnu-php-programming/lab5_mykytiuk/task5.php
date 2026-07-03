<?php
require '../config.php';
?>
<html>
    <title>Завдання 5</title>
<body>
    <h3>Завдання 5</h3>
    <p>5.1</p>
    <?php
    //Функція, що виводить слова заданого тексту у алфавітному порядку
    function print_words_reverse($text) {
        // Взяти до уваги переноси рядків
        $text = str_replace("\n", " ", $text);
        // Розділити текст на слова
        
        $words = explode(" ", $text);
        // Відсортувати слова
        sort($words);
        // Вивести слова
        echo "<p>Слова заданого тексту у алфавітному порядку:</p>";
        foreach ($words as $word) {
            echo $word . " ";
        }
    
    }
    // Текст дістати з файлу mykytiuk_text.txt
    $file = fopen("files/mykytiuk_text.txt", "r") or die("Неможливо відкрити файл");
    $text = fread($file, filesize("files/mykytiuk_text.txt"));
    fclose($file);
    print_words_reverse($text); 
    ?>
    <p>5.2</p>
    <?php
    // Вивести список двох слів, які найчастіше зустрічаються у тексті.
    function print_most_common_words($text) {
        // Взяти до уваги переноси рядків
        $text = str_replace("\n", " ", $text);
        // Розділити текст на слова
        $words = explode(" ", $text);
        // Підрахувати кількість кожного слова
        $word_count = array();
        foreach ($words as $word) {
            if (isset($word_count[$word])) {
                $word_count[$word]++;
            } else {
                $word_count[$word] = 1;
            }
        }
        // Відсортувати слова за кількістю зустрічей
        arsort($word_count);
        // Вивести два слова, які найчастіше зустрічаються
        echo "<p>Два слова, які найчастіше зустрічаються у тексті:</p>";
        $i = 0;
        foreach ($word_count as $word => $count) {
            echo $word . " " . $count . "<br>";
            $i++;
            if ($i == 2) {
                break;
            }
        }
    }
    print_most_common_words($text); 
    echo "<p>5.3</p>";
    function print_longest_words($text) {
        $text = str_replace("\n", " ", $text);
        $text = preg_replace("/[.,!?:;()]/", "", $text);
        $words = explode(" ", $text);
        $words_length = array();
        foreach ($words as $word) {
            $words_length[$word] = strlen($word);
        }
        $max_length = max($words_length);
        echo "<p>Найдовше слово у тексті:</p>";
        foreach ($words_length as $word => $length) {
            if ($length == $max_length) {
                echo $word . ": " . $length / 2 . "<br>";
            }
        }
        

    }
    print_longest_words($text);
    echo "<p>5.4</p>";
    function print_shortest_words($text) {
        $text = str_replace("\n", " ", $text);
        $words = preg_split('/\s+/', $text);
        $words_length = array();
        foreach ($words as $word) {
            $word = trim($word, ".,!?:;()-");
            if (!empty($word)) {
                $words_length[$word] = strlen($word);
            }
        }
        $min_length = min($words_length);
        echo "<p>Найкоротше слово у тексті:</p>";
        foreach ($words_length as $word => $length) {
            if ($length == $min_length) {
                echo $word . ": " . $length / 2 . "<br>";
            }
        }
    }
    print_shortest_words($text);
    echo "<p>5.5</p>";
    function print_words_starting_with($text, $letter) {
        $text = str_replace("\n", " ", $text);
        // Розділити текст на слова
        $words = preg_split('/\s+/', $text);
        echo "<p>Слова, які починаються на літеру " . $letter . ":</p>";
        foreach ($words as $word) {
            $word = trim($word, ".,!?:;()-");
            if (!empty($word) && mb_substr($word, 0, 1) == $letter) {
                echo $word . "<br>";
            }
        }
    }
    print_words_starting_with($text, "і");
    echo "<p>5.6</p>";
    function replace_lowercase($text, $letter) {
        $text = str_replace($letter, mb_strtoupper($letter), $text);
        echo "<p>Текст після заміни малої літери " . $letter . " на велику:</p>";
        echo $text;
    }
    replace_lowercase($text, "о");
    echo "<p>5.7</p>";
    $file_task7 = fopen("files/mykytiuk_text_5_7.txt", "r") or die("Неможливо відкрити файл");
    $text_task7 = fread($file_task7, filesize("files/mykytiuk_text_5_7.txt"));
    fclose($file_task7);
    function print_random_paragraph($text) {
        $paragraphs = preg_split('/\n+/', $text);
        $random_paragraph = $paragraphs[array_rand($paragraphs)];
        echo "<p>Випадковий абзац:</p>";
        echo $random_paragraph;
    }
    print_random_paragraph($text_task7);
    ?>
    <h3 class="back"><a href="lab5.php">Назад</a></h3>
</body>
</html>