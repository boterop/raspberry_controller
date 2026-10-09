import os
import time
import RPi.GPIO as GPIO

pin = os.getenv("FAN_PIN", 7)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

class Fan:
    def __init__(self):
        GPIO.output(pin, False)
        while True:
            max_temperature = int(os.getenv("MAX_TEMPERATURE", 70))
            min_temperature = int(os.getenv("MIN_TEMPERATURE", 50))
            current_temp = self.get_temp()
            if current_temp >= max_temperature:
                GPIO.output(pin, True)
            if current_temp <= min_temperature:
                GPIO.output(pin, False)
            time.sleep(1)

    def get_temp(self) -> float:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            return int(f.read().strip()) / 1000
