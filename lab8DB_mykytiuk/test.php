<? require '../config.php'; ?>
<html>
    <head>
        <title>test</title>
    </head>
    <body>
        <h1>Test</h1>
    <?php 
    // Підключення до бази даних
    $db_server = mysqli_connect($db_host, $db_user, $db_pass, $db_name);
    /*mysqli_query($db_server, "SET NAMES utf8");
    mysqli_query($db_server, "SET CHARACTER SET utf8");
    mysqli_query($db_server, "SET character_set_connection = utf8");
    
    mysqli_query($db_server, "DROP TABLE test");
    mysqli_query($db_server, "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(250), age INTEGER)");
    
    mysqli_query($db_server, "INSERT INTO test(name, age) VALUES('Ivan', 25)");*/
    $query_res = mysqli_query($db_server, "SELECT * FROM test");
    if (mysqli_num_rows($query_res) > 0) {
        while($row = mysqli_fetch_assoc($query_res)) {
            echo "ID: {$row['id']}<br>";
            echo "Name: {$row['name']}<br>";
            echo "Age: {$row['age']}<br>";
        }
    } else {
        echo "0 results";
    }
    ?>
    <form action="test.php" method="post">
        <input name="increment" type="number" required>
        <input type="submit" value="Increment">
    </form>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (isset($_POST['increment'])) {
            $increment = $_POST['increment'];
            mysqli_query($db_server, "UPDATE test SET age = age + $increment");
            header("Location: {$_SERVER['PHP_SELF']}");
            exit();
        }
    }
    ?>
</html>