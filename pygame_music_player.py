import pygame
import time
import keyboard

# Initialize the mixer
pygame.mixer.init()

# Load a single music file (only one file at a time)
pygame.mixer.music.load("hara.mp3")

# Start playing in a loop (-1 means infinite)
pygame.mixer.music.play(-1)

# Initial volume (0.0 to 1.0)
volume = 0.5
pygame.mixer.music.set_volume(volume)

print("Playing music... 🎶")
print("Press ↑ to increase volume")
print("Press ↓ to decrease volume")
print("Press S to stop music and exit")

try:
    while True:
        if keyboard.is_pressed("up"):
            volume = min(1.0, volume + 0.05)
            pygame.mixer.music.set_volume(volume)
            print(f"Volume: {int(volume * 100)}%")
            time.sleep(0.2)

        elif keyboard.is_pressed("down"):
            volume = max(0.0, volume - 0.05)
            pygame.mixer.music.set_volume(volume)
            print(f"Volume: {int(volume * 100)}%")
            time.sleep(0.2)

        elif keyboard.is_pressed("q"):
            print("Stopping music...")
            pygame.mixer.music.stop()
            break
        
except KeyboardInterrupt:
    pygame.mixer.music.stop()
    print("Stopped by user.")
