
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)							#LED
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) 	#BOTON pull up active
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) 	#SENSOR pull up active

led = GPIO.input(17)
sensor = GPIO.input(22)

print(led)
print(sensor)
while True:

	#check the state button
	if GPIO.input(27) == 0:
		print("presiono")
		sleep(0.08) 		#rebote del boton
		f = open('archivo.txt', 'r')
		aux = f.read()
		f.close();
		if aux == '0':
			f = open('archivo.txt', 'w');
			f.write('1');
			f.close()
		else:
			f = open('archivo.txt', 'w');
			f.write('0');
			f.close()

	#check the state sensor
	if GPIO.input(22) != sensor:
		print("entre sensor")
		sensor = GPIO.input(22)
		f = open('sensor.txt', 'w');
		f.write(str(sensor));
		f.close()

	#Update the state led
	f = open('archivo.txt', 'r')
	aux = f.read()
	f.close();
	if aux == '1':
		GPIO.output(17,1)
	else:
		GPIO.output(17,0)
		


