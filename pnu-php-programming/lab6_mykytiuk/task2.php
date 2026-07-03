<?php
require '../config.php';
?>
<html>
<head>
    <title>Завдання 2</title>
</head>
<body>
    <h3>Завдання 2</h3>
    <?php
    $file = fopen("files/text.txt", "r") or die("Неможливо відкрити файл");
    $text = fread($file, filesize("files/text.txt"));
    fclose($file);
    
    function match_sentences($text, $word_to_find) {
        $pattern = "/\b\w*$word_to_find\w*\b/iu";
        $sentences = preg_split("/(?<=[.!?])\s+/", $text); 
        $matches = array();
        foreach ($sentences as $sentence) {
            preg_match_all($pattern, $sentence, $matches[$sentence]);
        }
        arsort($matches);
        echo "<p>Речення, в яких зустрічається слово <b>" . $word_to_find . "</b>:</p>";
        foreach ($matches as $sentence => $match) {
            if (count($match[0]) > 0) {
                $sentence = str_replace("<", "&lt;", $sentence);
                $sentence = str_replace(">", "&gt;", $sentence);
                foreach ($match[0] as $word) {
                    $sentence = str_replace($word, "<b>" . $word . "</b>", $sentence);
                }
                echo "<p>" . $sentence . "</p>";
            }
        }
    }
    echo "<p>a)</p>";
    match_sentences($text, "тег");
    echo "<p>b)</p>";
    match_sentences($text, "HTML"); 
    echo "<p>c)</p>";
    echo "<form action='task2.php' method='post'>
        Введіть слово: <input type='text' name='word1'><br>
        <input type='submit' value='Знайти речення'><br>
        </form>";
    if (isset($_POST['word1'])) {
        match_sentences($text, $_POST['word1']);
    }
    ?>
    <h3 class='back'><a href="lab6.php">Назад</a><br></h3>
</body>
</html>
