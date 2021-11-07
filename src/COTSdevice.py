import RPi.GPIO as GPIO
import time

HR = 95
SpO2 = 92
FEV1 = 31

inpin = 15
outpin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(inpin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(outpin,GPIO.OUT)

button='up'
light='off'

try:
    while True:
        if (button=='up' and light=='off'):
            # wait for button press before changing anything
            if not GPIO.input(inpin):
                GPIO.output(outpin, 1)
                button='down'; 
                light='on'

        elif (button=='down' and light=='on'):
            # stay in this state until button released
            if GPIO.input(inpin):
                button='up'
                HR = 90
                SpO2 = 90
                FEV1 = 25

        elif (button=='up' and light=='on'):
            if not GPIO.input(inpin):
                GPIO.output(outpin, 0)
                button='down'
                light='off'

        elif (button=='down' and light=='off'):
            if GPIO.input(inpin):
                button='up'
        time.sleep(0.1)


finally:
    GPIO.cleanup()

    log = open("../data/data.txt", "w")
    log.write("HR,SpO2,FEV1\n")
    log.write("{:n},{:n},{:n}\n".format(HR,SpO2,FEV1))
    log.close() 

print("This file terminated!")