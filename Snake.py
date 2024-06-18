import pygame as pg
import random as rd
from pygame.locals import *


class Snake:
    def __init__(self):
        self.block_size = 15
        self.x = (40 * self.block_size) // 2
        self.y = (40 * self.block_size) // 2
        self.actionsCompleted = 0
        self.last_mov = 0
        self.snake_size = 1
        self.snaker = []
        self.gain = False
        self.appleX = rd.randrange(0, 40) * self.block_size
        self.appleY = rd.randrange(0, 40) * self.block_size
        self.appleGained = False
        self.score = 0
        self.win = pg.display.set_mode((600, 600))
        self.cstate = None
        self.pstate = None
        self.game_over = False
        self.reward = 0
        pg.draw.rect(self.win, (255, 0, 0), [self.appleX, self.appleY, self.block_size, self.block_size])


    def update(self, action):
        self.pstate = self.get_state()
        if self.x == self.appleX and self.y == self.appleY:
            self.snaker.append(pg.Rect(self.x, self.y, self.block_size, self.block_size))
            self.snake_size += 1
            self.gain = True
            self.appleGained = True
            self.score = self.score + 1
            self.newApp()
            self.reward = 1
            self.actionsCompleted = 0
            print("APPLE")
        else:
            self.reward = -0.1
            self.gain = False
            self.appleGained = False
            self.actionsCompleted += 1

        if self.x == 600 or self.x < 0 or self.y == 600 or self.y < 0:
            self.game_over = True
        if action == 0:
            if len(self.snaker) > 1 and self.last_mov == 1:
                self.game_over = True
            self.last_mov = 0
            self.y += self.block_size
            self.snaker.append(pg.Rect(self.x, self.y, self.block_size, self.block_size))
        elif action == 1:
            if len(self.snaker) > 0 and self.last_mov == 0:
                self.game_over = True
            self.last_mov = 1
            self.y -= self.block_size
            self.snaker.append(pg.Rect(self.x, self.y, self.block_size, self.block_size))
        elif action == 2:
            if len(self.snaker) > 0 and self.last_mov == 3:
                self.game_over = True
            self.last_mov = 2
            self.x += self.block_size
            self.snaker.append(pg.Rect(self.x, self.y, self.block_size, self.block_size))
        elif action == 3:
            if len(self.snaker) > 0 and self.last_mov == 2:
                self.game_over = True
            self.last_mov = 3
            self.x -= self.block_size
            self.snaker.append(pg.Rect(self.x, self.y, self.block_size, self.block_size))
        if len(self.snaker) > self.snake_size:
            del self.snaker[0]

        for snek in self.snaker:
            if len(self.snaker) > 1:
                head = self.snaker[-1]
                if head.x == snek.x and head.y == snek.y and snek is not head:
                    self.game_over = True
        self.cstate = self.get_state()
        if self.game_over:
            self.reward = -10


        return self.reward, self.game_over


    def get_state(self):
        DirLeft = (self.last_mov == 0)
        DirRight = (self.last_mov == 1)
        DirUp = (self.last_mov == 2)
        DirDown = (self.last_mov == 3)
        right = (self.appleX > self.x)
        left = (self.appleX < self.x)
        above = (self.appleY > self.y)
        below = (self.appleY < self.y)
        DangAbove = self.gonnaDie(0)
        DangBelow = self.gonnaDie(1)
        DangRight = self.gonnaDie(2)
        DangLeft = self.gonnaDie(3)
        return [int(DirLeft), int(DirRight), int(DirUp), int(DirDown), int(right), int(left), int(above), int(below), DangAbove, DangBelow, DangRight, DangLeft]


    def gonnaDie(self, dir):
        if dir == 0:
            for snek in self.snaker:
                if len(self.snaker) > 0:
                    head = self.snaker[-1]
                    if (head.x == snek.x and head.y - self.block_size == snek.y and snek != head) or self.y - self.block_size < 0:
                        return 1
            if len(self.snaker) > 0:
                if self.last_mov == 0:
                    return 1
            return 0
        if dir == 1:
            for snek in self.snaker:
                if len(self.snaker) > 0:
                    head = self.snaker[-1]
                    if (head.x == snek.x and head.y + self.block_size == snek.y and snek is not head) or self.y + self.block_size == 600:
                        return 1
            if len(self.snaker) > 0:
                if self.last_mov == 1:
                    return 1
            return 0
        if dir == 2:
            for snek in self.snaker:
                if len(self.snaker) > 0:
                    head = self.snaker[-1]
                    if (head.x - self.block_size == snek.x and head.y == snek.y and snek is not head) or self.x - self.block_size < 0:
                        return 1
            if len(self.snaker) > 0:
                if self.last_mov == 2:
                    return 1
            return 0
        if dir == 3:
            for snek in self.snaker:
                if len(self.snaker) > 0:
                    head = self.snaker[-1]
                    if (head.x + self.block_size == snek.x and head.y == snek.y and snek is not head) or self.x + self.block_size == 600:
                        return 1
            if len(self.snaker) > 0:
                if self.last_mov == 3:
                    return 1
            return 0
        return None

    def newApp(self):
        self.appleX = rd.randrange(0, 40) * self.block_size
        self.appleY = rd.randrange(0, 40) * self.block_size

        while True:
            for snake in self.snaker:
                if self.appleX == snake.x and self.appleY == snake.y:
                    self.appleX = rd.randrange(0, 40) * self.block_size
                    self.appleY = rd.randrange(0, 40) * self.block_size
                    continue
            break

    def gotApp(self):
        self.snaker.append(pg.Rect(self.x, self.y, self.block_size, self.block_size))
        self.snake_size += 1
        self.newApp()

    def render(self, maxApple):
        self.win.fill((0, 0, 0))
        font = pg.font.Font('arial.ttf', 32)
        # snake parts
        for snek in self.snaker:
            pg.draw.rect(self.win, (0, 255, 0), [snek.x, snek.y, self.block_size, self.block_size])

        pg.draw.rect(self.win, (255, 0, 0), [self.appleX, self.appleY, self.block_size, self.block_size])
        ScreenText = font.render('Highest Score: ' + str(maxApple), True, (255, 255, 255))
        self.win.blit(ScreenText, (600 - ScreenText.get_width(), 0))

