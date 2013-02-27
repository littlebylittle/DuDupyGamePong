#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#  * Date: 2/27/13
#  * Time: 11:05 AM
#  =============================

import pygame


class GameCycle():
    time_period = 150

    def main_loop(self):

        def _event_handler(self, event_list):
            for event in event_list:
                if event.type == pygame.QUIT:
                    self.game_finish = True
                    print('Event quit')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_PLUS:
                        GameCycle.time_period += 10
                        print('timer +=10')

                    if event.key == pygame.K_0:
                        GameCycle.time_period -= 10
                        print('timer -=10')

                    if event.key == pygame.K_KP0:
                        GameCycle.time_period = 100

                    if event.key == pygame.K_DOWN:
                        self.left_pin.set_y_move(10)
                    if event.key == pygame.K_UP:
                        self.left_pin.set_y_move(-10)

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.left_pin.set_y_move(0)
                    if event.key == pygame.K_UP:
                        self.left_pin.set_y_move(0)
            pass

        print(self.game_finish)

        while self.game_finish is False:
            #print('While cycle')
            _event_handler(self, pygame.event.get())
            self.scene_drawer.draw()

            self.clock.tick(GameCycle.time_period)
            self.ball.move(1, 2)
            self.left_pin.move()
            pass

        pygame.quit()
        print('Main loop done!')

    def __init__(self):
        print('Constructor call')
        pygame.init()
        self.size = [1500, 1004]
        self.game_score = [0, 0]
        self.game_finish = False

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        self.ball = Ball(self.size[0] // 2, self.size[1] // 2, scene=self.screen)
        self.left_pin = Pin(self.screen)
        self.right_pin = Pin(self.screen)
        self.scene_drawer = Scene(self.screen, score=self.game_score,
                                  ball=self.ball, left=self.left_pin, right=self.right_pin)

        pygame.display.set_caption('pong on pygame:.')


class Ball:
    size = 15

    def __init__(self, x_pos, y_pos, speed_x=10,
                 speed_y=5, speed_ratio=1, scene=None):

        print('Call construct ball')
        self.x = x_pos
        self.y = y_pos
        self.speed = speed_ratio
        self.speed_x = speed_x
        self.speed_y = speed_y

        self.max_value_x, self.max_value_y = scene.get_size()

    def move(self, add_x=0, add_y=0):
        if self.x > self.max_value_x or self.x < 0:
            self.speed_x *= -1
        if self.y > self.max_value_y or self.y < 0:
            self.speed_y *= -1

        self.x += self.speed_x
        self.y += self.speed_y


class Pin:
    def __init__(self, surface):
        self.surface = surface
        self.width = 10
        max_x, max_y = surface.get_size()
        self.y = max_y // 2
        self.height = max_y // 7
        self.dmove = 0
        print(self.y)

    def set_y_move(self, dmove):
        self.dmove = dmove

    def move(self):
        self.y += self.dmove

class Scene:
    colors = dict()
    colors['red'] = [0xff, 0, 0]
    colors['green'] = [0, 0xff, 0]
    colors['blue'] = [0, 0, 0xff]
    colors['white'] = [0xff, 0xff, 0xff]
    colors['black'] = [0, 0, 0]

    def __init__(self, screen, left=None, right=None, ball=None, score=None):
        self.screen = screen
        self.score = score
        self.left_pin = left
        self.right_pin = right
        self.ball = ball
        self.i = 0

    def draw(self):
        #middle_line_begin [ s]
        max_x, max_y = self.screen.get_size()
        middle_line_begin = [max_x // 2, 0]
        middle_line_end = [max_x // 2, max_y]

        self.screen.fill(Scene.colors['black'])

        if self.score:
            font = pygame.font.Font(None, 15)
            font.set_bold(False)
            text = font.render("Score:  " + str(self.score), False, Scene.colors['white'])
            self.screen.blit(text, [max_x * 0.75, 0])

        pygame.draw.line(self.screen, Scene.colors['white'], middle_line_begin, middle_line_end, 15)

        if self.ball:
            pygame.draw.circle(self.screen, Scene.colors['white'],
                              (self.ball.x, self.ball.y), self.ball.size, 0)
            pygame.draw.circle(self.screen, Scene.colors['red'],
                               (self.ball.x, self.ball.y), self.ball.size + 1, 2)

        if self.left_pin:
            rect = [(0, self.left_pin.y), (self.left_pin.width, self.left_pin.height)]
            pygame.draw.rect(self.screen, Scene.colors['white'], rect, 0)

        if self.right_pin:
            rect = [(max_x - self.right_pin.width, self.right_pin.y),
                    (max_x + 1, self.right_pin.height)]
            pygame.draw.rect(self.screen, Scene.colors['white'], rect, 0)

        pygame.display.flip()

if __name__ == '__main__':
    game = GameCycle()
    game.main_loop()
    pass
