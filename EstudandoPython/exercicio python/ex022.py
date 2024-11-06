import pygame
import time

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega a música MP3
pygame.mixer.music.load("musicaex022.mp3")

# Reproduz a música
pygame.mixer.music.play()

print("Pressione Enter para parar a música.")
input()  # Espera o usuário pressionar Enter para parar a música

# Para a música
pygame.mixer.music.stop()
print("Música parada.")

