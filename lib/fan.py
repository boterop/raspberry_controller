import os
import time
import RPi.GPIO as GPIO
from lib.api import API

pin = os.getenv("FAN_PIN", 7)
max_temperature = os.getenv("MAX_TEMPERATURE", 70)
min_temperature = os.getenv("MIN_TEMPERATURE", 50)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)


class Fan():
    def __init__(self):
        while True:
            system_info = API.request(os.getenv("SYSTEM-USAGE-URL"))
            current_temp = system_info['CPU']['temperature']
            if current_temp >= max_temperature:
                GPIO.output(pin, True)
            if current_temp <= min_temperature:
                GPIO.output(pin, False)
            time.sleep(1)
