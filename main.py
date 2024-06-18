import pygame as pg
import pygame.draw
from pygame.locals import *
from Snake import Snake
from agent import Agent
WHITE = (255, 255, 255)

pg.init()

agent = Agent(12, 4, learning_rate=0.15,discount_rate=0.95, epsilon=1)
window = pg.display.set_mode((600, 600))

window.fill(WHITE)

snek = Snake()
running = True

episode_num = 0
font = pygame.font.Font('arial.ttf', 32)

maxApple = 0
localApple = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    state = snek.get_state()
    action = agent.get_action(state=state)
    reward, game_over = snek.update(action)
    if reward > 0:
        localApple += 1
    if localApple > maxApple:
        maxApple = localApple

    if game_over is True:
        agent.endEpisode()
        snek.__init__()
        print(f"EPISODE {episode_num}\nEPSILON {agent.epsilon}")
        episode_num += 1
        localApple = 0
    new_state = snek.get_state()
    agent.updateQTable(state=state,action=action,reward=reward,next_state=new_state)
    snek.render(maxApple)
    pg.display.update()
    if episode_num % 100 == 0 and episode_num != 0:
        pg.time.delay(50)