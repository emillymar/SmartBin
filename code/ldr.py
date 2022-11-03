
#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import pygame
import subprocess
import random

def create_path(file_name):
	return  f'/home/smartbin/Documents/SmartBin/Pictures/{file_name}.jpeg'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

imgs_default = ['Default1', 'Default2', 'Default3']
imgs_feedback = ['Feedback1', 'Feedback2', 'Feedback3']

pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

def display_image(file_name):
    screen.fill((0,0,0))
    img = pygame.image.load(create_path(file_name)).convert()
    screen.blit(img,(0,0))
    pygame.display.update()


while True:
	display_image(random.choice(imgs_default))
	while True:
		if GPIO.input(7) == 0:
			print("Passou o lixo, soltem os memes")
			display_image(random.choice(imgs_feedback))
			time.sleep(5)
			break
