'''
Voeg de volgende 2 dingen aan de game toe:

  - Laat de auto aan de linkerkant van het scherm terugkomen als de auto aan de rechterkant van het scherm af rijdt HINT: Gebruik een ```if``` met daarin de ```x_pos```
  - Laat een aantal regendruppels van de bovenkant van het scherm naar beneden vallen

Slides: https://docs.google.com/presentation/d/16rz2C4Pqhx4YNCokEU_5mc3rtQXXNEoi7gFAGzv9s_A/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
screen. fill ("white")
pygame.display.set_caption('Auto rijden!')
clock = pygame.time.Clock()
running = True

background_surface = pygame.Surface((800, 400))
background_surface.fill("white")

auto_surface = pygame.image.load("Opdrachten/PyGame/Les3/graphics/auto.png").convert_alpha()
auto_x_pos = 0

regen = pygame.image.load("Opdrachten/PyGame/Les3/graphics/regen.png")
regen = pygame.transform.scale (regen, (400,200))

while running:

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      running = False

    screen.blit(background_surface, (0, 0))

    if auto_x_pos >800:
      auto_x_pos -= 800
    auto_x_pos += 2

    screen.blit(auto_surface, (auto_x_pos, 200))

    screen.blit(regen, (300, 200 ))

 

 
      

    pygame.display.update()
    clock.tick(60)