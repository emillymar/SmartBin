import pygame
import time

pygame.init()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
done = False
image0 = pygame.image.load("/home/smartbin/Documents/SmartBin/Pictures/Default1.jpeg").convert()

screen.blit(image0,(0,0))
pygame.display.flip()

time.sleep(10)
pygame.quit()
