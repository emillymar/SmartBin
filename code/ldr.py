#!/usr/bin/python

import RPi.GPIO as GPIO
import time
from PIL import Image
import subprocess
import random

ldr_last_state = 1

def open_image(file_name):
    img_path = f'/home/smartbin/Pictures/{file_name}.jpeg'
    img = Image.open(img_path)
    img.show()
    return img

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

imgs_default = ['Default1','Default2','Default3']
imgs_feedback = ['Feedback1','Feedback2','Feedback3']

while True:
    img = open_image(random.choice(imgs_default))

    while True:
        if GPIO.input(7) == 0:
            
            print("Passou o lixo, soltem os memes")
            subprocess.run(["killall display"], shell=True)
            img = open_image(random.choice(imgs_feedback))
            time.sleep(5)
            subprocess.run(["killall display"], shell=True)
            img.close()
            break

