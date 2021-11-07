import RPi.GPIO as GPIO
import time

HR = 95
SpO2 = 92
FEV1 = 31

def button_callback(channel):
    print("Button was pressed!")
    FEV1 = 29

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:

    print("LED on")
    GPIO.output(18,GPIO.HIGH)    

    GPIO.add_event_detect(15,GPIO.RISING,callback=button_callback)

    end_message = input("Press enter to quit\n")


    print("LED off")
    GPIO.output(18,GPIO.LOW)


finally:
    GPIO.cleanup()

    log = open("../data/data.txt", "w")
    log.write("HR,SpO2,FEV1\n")
    log.write("{:n},{:n},{:n}\n".format(HR,SpO2,FEV1))
    log.close() 

print("This file terminated!")