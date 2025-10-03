# Gegeven is Pikachu die nu wel normaal kan lopen als je de pijltjes ingedrukt houdt!

# Gegeven is een variabele game_actief, deze is True, doe het volgende:

#   - Als game_actief True is moet alle code van de game werken, zet deze code dus in een if
#   - Als pikachu collide met de tekst "Dood!" maak game_actief dan False
#   - Als game_actief False is, maak het scherm dan zwart en zet pikachu weer in het midden van het scherm
#   - Als de speler dan op spatie drukt, start het spel dan opnieuw (game_actief = True)

# Slides: https://docs.google.com/presentation/d/1fzbS39wrbh226ts72wHhQzyjpxuYxhqV9pEE8XcwTPM/edit?usp=sharing
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Keyboard en zwaartekracht')
font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()

enemy_surface = font.render("Dood!", False, "red")
enemy_rect = enemy_surface.get_rect(center= (300, 200))

pikachu_surface = pygame.image.load("Opdrachten/PyGame/Les7/graphics/pikachu.png").convert_alpha()
pikachu_rect = pikachu_surface.get_rect(topleft = (180, 20))

zwaartekracht = 0
game_actief = True

# Game loop
while True:
  # Event loop
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    
    if game_actief:
       if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and pikachu_rect.bottom >= 300:
          zwaartekracht = -20
    else:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_actief = True
  # Playing
  if game_actief: 
    if pikachu_rect.colliderect(enemy_rect):
      game_actief = False
 
    screen.fill("turquoise")
    screen.blit(enemy_surface, enemy_rect)

    zwaartekracht += 1
    pikachu_rect.y += zwaartekracht

    if pikachu_rect.bottom >= 300:
      pikachu_rect.bottom = 300

    # Poll for input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT and pygame.K_d] and pikachu_rect.right + 6 <= 400:
      pikachu_rect.x += 6
    if keys[pygame.K_LEFT and pygame.K_a] and pikachu_rect.left - 6 >= 0:
      pikachu_rect.x -= 6
  
  # Game over    
  else:
    screen.fill("black")

  screen.blit(pikachu_surface, pikachu_rect)

  pygame.display.update()
  clock.tick(60)
