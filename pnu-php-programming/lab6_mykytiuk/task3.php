<?php
require '../config.php';
?>
<html>
<head>
    <title>Завдання 3</title>
</head>
<body>
    <h3>Завдання 3</h3>
    <?php
    $html_file = fopen("files/task3_text.html", "r") or die("Unable to open file!"); 
    $text = fread($html_file, filesize("files/task3_text.html"));
    fclose($html_file);
    function delete_tags($text) {
        $text = preg_replace('/<[^>]*>/', ' ', $text);
        return $text;
    }
    $text = delete_tags($text);
    while (strpos($text, "  ") !== false) {
        $text = str_replace("  ", " ", $text);
    }
    echo $text; 
    ?>
    <h3 class='back'><a href="lab6.php">Назад</a><br></h3>
</body>
</html>