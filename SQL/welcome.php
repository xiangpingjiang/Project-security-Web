<?php
$name = $_GET['name'];
$pass = $_GET['pass'];
// echo $name;
// echo $pass;
$sql = "SELECT  * FROM student  where name = '$name' and pwd = '$pass'" ;
echo $sql."<br>";


$servername = "localhost";
$username = "root";
$password = "xpj123456";
$dbname = "test";

 
// create connection
$conn = new mysqli($servername, $username,$password,$dbname);
 
// test connection
// if ($conn->connect_error) {
//     die("connection failed: " . $conn->connect_error);
// } 
// echo "connection succed";


$result = $conn->query($sql);
 
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo  "login succed";
    }
} else {
    echo "login failed";
}


$conn->close();

?>
