import serial

uart = serial.Serial("/dev/ttyACM0",9600,timeout = 1)

def enviar():
	m = input("Ingrese a o b : ")
	uart.write(m.encode())

while True:
	enviar()

