import RPi.GPIO
import time
GPIO.setmode(GPIO,BOARD)
GPIO.setup(18,GPIO.OUT)

humidity = 70

if humidity >= 70:
    while True:
        GPIO.output(18,True)
        time.sleep(1)
        GPOI.output(18,False)
        time.sleep(1)
