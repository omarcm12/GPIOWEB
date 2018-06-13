<?php 
	$myfile = file_get_contents('sensor.txt',true);
  		if ($myfile == "1") {
  		 	echo "1";
  		 } 
  		 else{
  		 	echo "0";
  		 }
?>
