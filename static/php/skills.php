<?php
$host = "127.0.0.1"; //IP of your database
$userName = "root"; //Username for database login
$userPass = "toor"; //Password associated with the username
$database = "resume"; //Your database name

$connectQuery = mysqli_connect($host,$userName,$userPass,$database);

$name = $_GET["name"];

if(mysqli_connect_errno()){
    echo mysqli_connect_error();
    exit();
}else{
    $selectQuery = "SELECT score FROM `skills` where name='$name' ";
    $result = mysqli_query($connectQuery,$selectQuery);
    $row = mysqli_fetch_assoc($result);

    echo json_encode($row);

}
?>