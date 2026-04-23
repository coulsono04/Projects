<?php

// This project assesses booleans and comparison operators in PHP to creates a number guessing game.

$play_count = 0;
$correct_guesses = 0;
$guess_high = 0;
$guess_low = 0;

echo "I'm going to think of numbers between 1 and 10 (inclusive). Do you think you can guess correctly?\n";

function guessNumber(){
  global $play_count, $correct_guesses, $guess_high, $guess_low;
  $play_count ++;
  $random_number = rand(1, 10);
  echo "\nWhat is your guess\n";
  $player_input = readline(">>");
  $player_input = intval($player_input);
  echo "youre on round number $play_count, the random number was $random_number, you guessed $player_input.";
  if ($player_input === $random_number){
    $correct_guesses ++;
  } elseif ($player_input > $random_number){
    $guess_high ++;
  } elseif ($player_input < $random_number){
    $guess_low ++;
  }
}

# Could be wrong
for ($i = 10; $i >0; $i --){
  guessNumber();
}
$percent_correct = $correct_guesses/$play_count * 100;
echo "\nYou got $percent_correct % correct!\n";
if ($guess_high > $guess_low){
  echo "When you guessed wrong, you tended to guess high.";
} elseif ($guess_high < $guess_low){
  echo "When you guessed wrong, you tended to guess low.";
}




