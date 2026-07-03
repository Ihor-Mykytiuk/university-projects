<?php
    require '../config.php';
    
    mysqli_query($db_server, "drop table dusc");

    mysqli_query($db_server, "create table if not exists dusc(id integer primary key auto_increment, name_d varchar(100) unique, key_concept varchar(250))");
    mysqli_query($db_server, "insert into dusc (name_d, key_concept) values ('Networks', 'HTTPS')");
    mysqli_query($db_server, "insert into dusc (name_d, key_concept) values ('AI','Modeling dfbdsf')");
    

      # <head> <title>LAB_DB TASK 1-3 </title></head>
?>

<html>
    <body>
        <table border="2">
        <h2>Fetch result:</h2>
            <tr><th>Name</th><th>Key concept</th></tr>
            <?php
                $query_res = mysqli_query($db_server, "select * from dusc");
    
                if (mysqli_num_rows($query_res) > 0) {
                    while($row = mysqli_fetch_row($query_res)) {
                       echo "<tr><td>" . $row[0]. "</td><td>".$row[1]."</td></tr>";
                    }
                } else {
                    echo "0 results";
                }
                mysqli_close($db_server);   
            ?>    
        </table>

    </body>
</html>