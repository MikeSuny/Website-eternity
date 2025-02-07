<?php
session_start();
$conn = new mysqli("localhost", "root", "", "login_system");

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $password = $_POST["password"];

    $stmt = $conn->prepare("SELECT * FROM users WHERE email = ? AND password = ?");
    $stmt->bind_param("ss", $email, $password);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $_SESSION["user"] = $email;
        header("Location: php1.php");
    } else {
        echo "Login failed. Invalid credentials.";
    }
}
?>

<?php
session_start();
if (!isset($_SESSION["user"])) {
    header("Location: index1.html");
    exit();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h2>Login Successful!</h2>
    <p>Welcome, <?php echo $_SESSION["user"]; ?>!</p>
    <a href="php1.php">Logout</a>
</body>
</html>

<?php
session_start();
session_destroy();
header("Location: index1.html");
?>

