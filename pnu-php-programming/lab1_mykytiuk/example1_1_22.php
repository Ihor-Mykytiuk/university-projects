<?php
require '../config.php';
?>
<html>
    <title>Приклад оператора do...while</title>
<body>
<?php
// Імітація кидка грального кубика доки не випаде 6
echo "<h3>Імітація кидка грального кубика доки не випаде 6</h3>";
do {
    $number=rand(1, 6);

    echo "Випало число ".$number."<br>";
    
} while ($number!=6);

?>

<h3 class='back'><a href='lab1.php'>Назад</a></h3>
</body>
</html>