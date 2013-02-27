#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#  * Date: 2/27/13
#  * Time: 11:05 AM
#  =============================

import pygame


class GameCycle():
    time_period = 10

    def main_loop(self):
        def _event_handler(self, event_list):
            for event in event_list:
                if event.type == pygame.QUIT:
                    self.game_finish = True
                    print('Event quit')

        print('Main loop call...')
        print(self.game_finish)

        while self.game_finish is False:
            print('While cycle')
            _event_handler(self, pygame.event.get())
            self.scene_drawer.draw()

            self.clock.tick(GameCycle.time_period)
            pass

        pygame.quit()
        print('Main loop done!')

    def __init__(self):
        print('Constructor call')
        pygame.init()
        self.size = [800, 600]
        self.game_score = [0, 0]
        self.game_finish = False

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        self.ball = Ball(self.size[0] // 2, self.size[1] // 2)
        self.scene_drawer = Scene(self.screen, score=self.game_score,
                                  ball=self.ball)

        pygame.display.set_caption('pong on pygame:.')


class Ball:
    size = 20

    def __init__(self, x_pos, y_pos, speed_x=1,
                 speed_y=1, speed_ratio=1, area_size=[800, 600]):

        self.x = x_pos
        self.y = y_pos
        self.speed = speed_ratio
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.max_value_x = area_size[0]
        self.max_value_y = area_size[1]

    def move(self, add_x=0, add_y=0):
        self.x += add_x * self.speed
        self.y += add_y * self.speed


class Pin:
    def __init__(self, width, height, pos_x, pos_y):
        self.width = width
        self.height = height
        self.x = pos_x
        self.y = pos_y


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
        self.right_ping = right
        self.ball = ball

    def draw(self):
        #middle_line_begin [ s]
        max_x, max_y = self.screen.get_size()
        middle_line_begin = [max_x // 2, 0]
        middle_line_end = [max_x // 2, max_y]

        if self.score:
            font = pygame.font.Font(None, 15)
            font.set_bold(False)
            text = font.render("Score: " + str(self.score), False, Scene.colors['white'])
            self.screen.blit(text, [max_x * 0.75, 0])

        pygame.draw.line(self.screen, Scene.colors['white'], middle_line_begin, middle_line_end, 15)

        if self.ball:
            pygame.draw.circle(self.screen, Scene.colors['white'],
                              (self.ball.x, self.ball.y), self.ball.size, 0)
            pygame.draw.circle(self.screen, Scene.colors['red'],
                               (self.ball.x, self.ball.y), self.ball.size + 1, 2)

        pygame.display.flip()


if __name__ == '__main__':
    game = GameCycle()
    game.main_loop()
    pass
