'''
Gegeven is een weg en een auto. Van de auto is al een rectangle gemaakt en deze gebruiken we om de auto te plaatsen en te laten bewegen.

Van de weg is echter nog geen rectangle gemaakt.

Doe het volgende:

  - Maak een rectangle van de weg met surface.get_rect()
  -  precies in het  dat de center  deze rectangle in het midden van de game staat (weg)
  - Zorg dat de onderkant van de auto (bottom) op dezelfde plek staat als de onderkant van de weg (dan rijdt de auto namelijk op de weg)
  - Zorg dat wanneer de auto en het obstakel colliden je de auto weer naar het begin van het scherm verplaatst (de pion staat pas op de goede plek als de weg is verplaatst)

Vergeet niet om de weg_surface naar de weg_rect te blitten in plaats van naar een aantal coordinaten!

EXTRA:

Blit een stukje tekst "Game over" naar het scherm als de auto de pion raakt.

Slides: https://docs.google.com/presentation/d/1VjYiTjIcSU_x6R_K0pPASkzf7xis3oa_IpjzcmC-Wq8/edit?usp=sharing
'''
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Auto rijden!')
clock = pygame.time.Clock()
running = True

background = pygame.Surface((800, 400))
background.fill("white")

weg = pygame.image.load("Opdrachten/PyGame/Les4/graphics/weg.png").convert()
weg_rect = weg.get_rect(topleft=(0, 75))

auto = pygame.image.load("Opdrachten/PyGame/Les4/graphics/auto.png").convert_alpha()
auto_rect = auto.get_rect(bottom = 350)

obstakel = pygame.image.load("Opdrachten/PyGame/Les4/graphics/obstakel.png").convert_alpha()
obstakel_rect = obstakel.get_rect(bottomleft = (625, 250))

while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(background, (0, 0))
  screen.blit(weg, weg_rect)
  screen.blit(weg , (0, 75))
  screen.blit(obstakel, obstakel_rect)
  
  auto_rect.left += 0
  if auto_rect.left > 800:
    auto_rect.right = 0
  screen.blit(auto, auto_rect)

  pygame.display.update()
  clock.tick(60)
