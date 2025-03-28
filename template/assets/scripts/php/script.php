<?php

date_default_timezone_set("Asia/Novosibirsk");

$allTrues = 4;
$qCounter = 0;

if (isset($_POST["q1"]) && isset($_POST["q2"]) && (isset($_POST["q31"]) || isset($_POST["q32"]) || isset($_POST["q33"]))) {
    if ($_POST["q1"] == "true") {
        $qCounter++;
    }
    if ($_POST["q2"] == "true") {
        $qCounter++;
    }
    if (isset($_POST['q31']) && $_POST["q31"] == "true") {
        $qCounter++;
    }
    if (isset($_POST['q32']) && $_POST["q32"] == "true") {
        $qCounter++;
    }

    $dt = date("Y-m-d h:i:sa", time());

    $res_file = fopen("../../texts/results.txt", "a") or die("Error: file not found");

    fwrite($res_file, $qCounter . " - " . $dt . "\n");

    fclose($res_file);

    echo $qCounter . " - " . $dt;

    $_POST = array();

} else {
    echo "Fill in all fields";
    $_POST = array();
}


