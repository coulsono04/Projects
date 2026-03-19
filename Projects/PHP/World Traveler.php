<?php

// This PHP program converts different currencies to USD, and showcases string concatination.
  
  $riel = 2103942;
  $kyat = 19092;
  $krones = 109;
  $lek = 9094;

  echo $riel;
  echo "\n" . $kyat;
  echo "\n" . $krones;
  echo "\n" . $lek;

  $rielER = 0.00025;
  $kyatER = 0.00048;
  $kronesER = 0.1;
  $lekER = 0.012;

  echo "\n" . $riel * $rielER;
  echo "\n" . $kyat * $kyatER;
  echo "\n" . $krones * $kronesER;
  echo "\n" . $lek * $lekER . "\n";

  $finalCost = (($riel * $rielER) + ($kyat * $kyatER) + ($krones * $kronesER) + ($lek * $lekER)) - 4;
  echo "The final cost is $${finalCost}";

  $finalCost = floor($finalCost);
  echo "${finalCost}";