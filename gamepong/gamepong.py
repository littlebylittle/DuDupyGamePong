#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#  * Date: 2/27/13
#  * Time: 11:05 AM
#  =============================
import pygame
from . ball import Ball
from . pinplatform import Pin
from . scenemanager import Scene


class GameCycle():
    time_period = 50

    def main_loop(self):

        def _event_handler(self, event_list):
            for event in event_list:
                if event.type == pygame.QUIT:
                    self.game_finish = True
                    print('Event quit')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_PLUS:
                        GameCycle.time_period += 10

                    if event.key == pygame.K_KP_MINUS:
                        GameCycle.time_period -= 10
                        GameCycle.time_period = abs(GameCycle.time_period)

                    if event.key == pygame.K_KP_MULTIPLY:
                        GameCycle.time_period = 50

                    if event.key == pygame.K_DOWN:
                        self.left_pin.set_y_move(5)
                    if event.key == pygame.K_UP:
                        self.left_pin.set_y_move(-5)

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
        self.size = [1600, 1004]
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


if __name__ == '__main__':
    game = GameCycle()
    game.main_loop()
    pass