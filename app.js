$(document).ready( function (){

  	$("#boton").click(toggle);

    /* funciones encargadas de verificar el estado de los dispositivos */
    setInterval(realTimeLed,1000/30);
    setInterval(realTimeSensor,1000/30);
}

);

/* funcion encargada de verificar el estado del led constantemenrte */ 

function realTimeLed(){
  var url = "led.php";
  $.ajax({
    type: "POST",
    url: url,
    success: function(data){
      if(data == "1"){
         document.getElementById("imgLed").src="led-512.png";
       }else{
        document.getElementById("imgLed").src="ledOff.png";
       }
    }
  });
}

/* funcion encargada de verificar el estado del sensor constantemenrte */

function realTimeSensor(){ 
  var url = "sensor.php";
  $.ajax({
    type: "POST",
    url: url,
    success: function(data){
      if(data == "1"){
          document.getElementById("imgSensor").src="powerOn.png";
       }else{
          document.getElementById("imgSensor").src="power.png";
       }
    }
  });
}

/* Funcion encargada de hacer la peticion al servidor del toggle al led */

function toggle(){
  var url = "togge.php";
  $.ajax({
    type: "POST",
    url: url,
    success: function(data){
      console.log(data);
    }
  });
}

