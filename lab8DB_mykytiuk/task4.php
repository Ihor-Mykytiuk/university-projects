<?php
    require '../config.php';

    // mysqli_query($db_server, "drop table user");

    mysqli_query($db_server, "CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTO_INCREMENT, 
        login VARCHAR(250) UNIQUE, email VARCHAR(250), password VARCHAR(100))");

    if(isset($_POST["login"], $_POST["email"], $_POST["password"])){
        $email = $_POST["email"];
        $login = $_POST["login"];
        $password = $_POST["password"];

        if(mysqli_query($db_server, "INSERT INTO user(login, email, password) VALUES ('$login', '$email', '$password')")){
            echo "<p>User successfully added!</p>";
        }
    }
?>

<html>
    <head> <title>LAB DB - TASK 4</title></head>
    <style>
        form{
            width: 250px;
            margin : 0 auto;
            display: flex;
            flex-direction: column;
        }

        table{margin: 1em;}
    </style>
    <body>
        <form action="" method="POST">
            <input type="text" name="login" placeholder="Your login:" required>
            <input type="text" name="email" placeholder="Your email:" required>
            <input type="password" name="password" placeholder="Your password:" required>
            <input type="submit" value="Sign up!">
        </form>

        <table border="2">
            <tr><th>ID</th><th>Login</th><th>Email</th><th>Password</th></tr>

            <?php
            //  $query_res1 = mysqli_query($db_server, "delete from user where id='3'");

                $query_res = mysqli_query($db_server, "select * from user order by id");
    
                if (mysqli_num_rows($query_res) > 0) {
                    while($row = mysqli_fetch_assoc($query_res)) {
                        echo "<tr><td>".$row["id"]."</td><td>".$row["login"]."</td><td>".$row["email"]."</td><td>".$row["password"]."</td></tr>";
                    }
                } else {
                    echo "0 results";
                }
                           
                    mysqli_close($db_server);   
            ?>
        </table>

        <h3 class='back'><a href='lab8_DB.php'>Назад</a></h3>
    </body>
</html>