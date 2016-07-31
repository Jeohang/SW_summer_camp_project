import sys
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
 
sensor = Adafruit_DHT.DHT11
pin = 18
 
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin,50)
p.start(7.5)
 
while True:
    temperature, humidity = Adafruit_DHT.read_retry(sensor, pin)
    if temperature is not None and humidity is not None:
        print('Temperature = {0:0.1f}*C ' .format(humidity))
        print('Humidity = {0:0.1f}% '.format(temperature))
    else:
        print('Cannot get the sensor data!')
    time.sleep(2)
    
try:
    if temperature > 30:
        p.ChangeDutyCycle(15)
        time.sleep(1)
    elif temperature <= 30:
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
except KeyboardInterrput:
    p.stop()
    GPIO.cleanup()
