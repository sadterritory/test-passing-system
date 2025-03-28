<?php
//$ans = $_SESSION['a'];
$ans = 3;
$rows = array($ans, 5 - $ans);
$width = 210;
$height = 150;
$rowWidth = 50;
$rowInterval = 10;
$img = imagecreatetruecolor($width, $height);
$white = imagecolorallocate($img, 255, 255, 255);
imagefill($img, 0, 0, $white);
for ($i = 0, $y1 = $height, $x1 = 30; $i < count($rows); $i++) {
    if ($rows[$i] == $ans)
        $color = imagecolorallocate($img, 0, 255, 0);
    else
        $color = imagecolorallocate($img, 255, 0, 0);
    $y2 = $y1 - $rows[$i] * $height / 7;
    $x2 = $x1 + $rowWidth;
    imagefilledrectangle($img, $x1, $y1, $x2, $y2, $color);
    $x1 = $x2 + $rowInterval;
}
header("Content-type: image/png");
imagepng($img);
imagedestroy($img);