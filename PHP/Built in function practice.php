<?php

// Functions and built in functions practice, including calculating a meal cost + a tip or calculating the area of a circle.

function convertToShout($string){
   return strtoupper($string) . "!";
}

$string_converted = convertToShout("Hello there!");
echo $string_converted;

function tipGenerously($cost_of_meal){
  return ceil($cost_of_meal * 1.2);
}

$meal_with_tip = tipGenerously(100);
echo $meal_with_tip;

function calculateCircleArea($diameter){
  $area = pi() * ($diameter / 2) ** 2;
  return $area;
}

$area_of_circle = calculateCircleArea(50);
echo $area_of_circle;