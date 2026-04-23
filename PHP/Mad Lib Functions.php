<?php

// This project assesses the creation of functions in PHP, and creates a Mad Lib game.

function generateStory($singular_noun, $verb, $color, $distance_unit){
  $story = "The ${singular_noun}s are lovely, ${color}, and deep.\nBut I have promises to keep,\nAnd ${distance_unit} to go before I $verb,\nAnd ${distance_unit} to go before I go to explode and ${verb} away.\n";
  return $story;
}

echo generateStory("carrot", "run", "red", "miles");
echo generateStory("parsnip", "swim", "blue", "cm");
echo generateStory("brocolli", "climb", "brown", "meters");
