import pygame
import random

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
pygame.font.init()

background = pygame.image.load('background.png')
user = pygame.image.load('user.png')
egg = pygame.image.load('egg.png')

def display_score(score):
  font = pygame.font.SysFont('Comic Sans MS', 30)
  score_test = 'Score: ' + str(score)
  test_img = font.render(score_test, True, (0, 255, 0))
  screen.blit(test_img, [20, 10])


#function for move egg:
def random_offset():
  return -1*random.randint(100, 1500)

egg_y = [random_offset(), random_offset(),random_offset()]
user_x = 150
score = 0

def crashed(idx):
  global score
  global keep_alive
  score = score - 6
  egg_y[idx] = random_offset()
  if score < -350:
    keep_aalive = False

def update_egg_pos(idx):
  global score
  if egg_y[idx] > 620:
    egg_y[idx] = random_offset()
    score = score + 5
  else:
    egg_y[idx] = egg_y[idx] + 5


keep_alive = True
clock = pygame.time.Clock()
while keep_alive:
#user movement:
  pygame.event.get()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT] and user_x < 295:
    user_x = user_x + 10
  elif keys[pygame.K_LEFT] and user_x > 0:
    user_x = user_x - 10

  update_egg_pos(0)
  update_egg_pos(1)
  update_egg_pos(2)

  screen.blit(background, [0, 0])
  screen.blit(user, [user_x, 520])
  screen.blit(egg, [0, egg_y[0]])
  screen.blit(egg, [150, egg_y[1]])
  screen.blit(egg, [300, egg_y[2]])

#chash point:
  if egg_y[0] > 500 and user_x < 70:
    crashed(0)

  if egg_y[1] > 500 and user_x < 200:
    crashed(1)

  if egg_y[2] > 500 and user_x > 200:
    crashed(2)
  
  display_score(score)

  pygame.display.update()
  clock.tick(66)