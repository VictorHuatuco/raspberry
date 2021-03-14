import RPi.GPIO as GPIO
import time

#Config canales
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
#LOOP
while True:
    GPIO.output(21,True)
    time.sleep(5)
    GPIO.output(21,False)
    time.sleep(5)
