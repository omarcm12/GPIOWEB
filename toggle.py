
f = open('archivo.txt', 'r');
txt = f.read()
f.close()

f = open('archivo.txt', 'w');

if txt == "1":
	f.write('0')
else:
	f.write('1')

f.close()
