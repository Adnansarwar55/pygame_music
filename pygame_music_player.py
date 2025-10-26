import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("hara.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)  # 50% volume

try:
    while True:
        print("Playing...")
        time.sleep(4)
except KeyboardInterrupt:
    print("Stopping music...")
    pygame.mixer.music.stop()
