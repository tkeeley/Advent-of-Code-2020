<!-- # Advent of Code Day 2 -->

<?php
$part1 = 0;
$part2 = 0;
foreach (explode("\n", file_get_contents("passwords.txt")) as $pass) {
$pass = explode(" ", $pass);
$policy = explode("-", $pass[0]);
foreach (count_chars($pass[2], 1) as $i => $val) {
if (str_replace(":", "", $pass[1]) == chr($i) && $policy[0] <= $val && $policy[1] >= $val) {
$part1++;
        }
    }
if (str_replace(":", "", $pass[1]) === $pass[2][$policy[0] - 1] || str_replace(":", "", $pass[1]) === $pass[2][$policy[1] - 1]) {
if ($pass[2][$policy[0] - 1] !== $pass[2][$policy[1] - 1]){
$part2++;
        } 
    }
} 
echo "Part 1:<br>" . $part1 . "<br><br>Part 2:<br>" . $part2; 
?>