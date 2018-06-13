<?php 
	/* Ejecucion de script de python para hacer toggle en el archivo */
  	echo shell_exec("python /var/www/html/toggle.py 2>&1");
  	echo "ok";

?>
