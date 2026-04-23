<?php

// This project assesses the use of booleans and comparison operators in PHP to create a magic 8 ball.

function magic8Ball(){
  $response = readline("\nPlease ask a yes or no question");
  #echo $response;
  $magic_answer = rand(0, 19);
  #echo "\n" . $magic_answer;
  echo "\n";
  if ($magic_answer === 0){
  echo "It is certain.";
  } elseif($magic_answer === 1){
    echo "It is decidedly so.";
  }elseif($magic_answer === 2){
    echo "Without a doubt.";
  }elseif($magic_answer === 3){
    echo "Yes - definitely.";
  }elseif($magic_answer === 4){
    echo "You may rely on it.";
  }elseif($magic_answer === 5){
    echo "As I see it, yes.";
  }elseif($magic_answer === 6){
    echo "Most likely.";
  }elseif($magic_answer === 7){
    echo "Outlook good.";
  }elseif($magic_answer === 8){
    echo "Yes.";
  }elseif($magic_answer === 9){
    echo "Signs point to yes.";
  }elseif($magic_answer === 10){
    echo "Reply hazy, try again.";
  }elseif($magic_answer === 11){
    echo "Ask again later.";
  }elseif($magic_answer === 12){
    echo "Better not tell you now.";
  }elseif($magic_answer === 13){
    echo "Cannot predict now..";
  }elseif($magic_answer === 14){
    echo "Concentrate and ask again.";
  }elseif($magic_answer === 15){
    echo "Don't count on it.";
  }elseif($magic_answer === 16){
    echo "My reply is no.";
  }elseif($magic_answer === 17){
    echo "My sources say no.";
  }elseif($magic_answer === 18){
    echo "Outlook not so good.";
  }elseif($magic_answer === 19){
    echo "Very doubtful.";
  }
}

magic8Ball();
magic8Ball();