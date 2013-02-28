#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#  * Date: 2/27/13
#  * Time: 11:05 AM
#  =============================
import pygame
from . ball import Ball
from . pinplatform import Pin


class GameCycle():
    time_period = 50

    def main_loop(self):

        def _event_handler(self, event_list):
            for event in event_list:
                if event.type == pygame.QUIT:
                    self.game_finish = True

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

        while self.game_finish is False:
            _event_handler(self, pygame.event.get())
            self.render()

            self.clock.tick(GameCycle.time_period)
            self.ball.move()
            self.left_pin.move()
            pass

        pygame.quit()

    def __init__(self, resolution=None):
        pygame.init()
        if not resolution:
            self.size = [800, 600]
        else:
            self.size = resolution
        self.game_score = [0, 0]
        self.game_finish = False

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)

        self.left_pin = Pin(self.screen, 0)
        self.right_pin = Pin(self.screen, self.size[0] + 1,)

        self.ball = Ball(self, )

        self.displayed_sprites = pygame.sprite.RenderPlain()
        self.displayed_sprites.add(self.left_pin, self.right_pin, self.ball)

        pygame.display.set_caption('pong on pygame:.')

    def render(self):
        colors = dict()
        colors['red'] = [0xff, 0, 0]
        colors['green'] = [0, 0xff, 0]
        colors['blue'] = [0, 0, 0xff]
        colors['white'] = [0xff, 0xff, 0xff]
        colors['black'] = [0, 0, 0]

        self.screen.fill(colors['black'])

        self.displayed_sprites.draw(self.screen)

        max_x, max_y = self.screen.get_size()
        middle_line_begin = [max_x // 2, 0]
        middle_line_end = [max_x // 2, max_y]

        font = pygame.font.Font(None, 15)
        font.set_bold(False)
        text = font.render("Score:  " + str(self.game_score), False, colors['white'])
        self.screen.blit(text, [max_x * 0.75, 0])

        pygame.draw.line(self.screen, colors['white'],
                         middle_line_begin, middle_line_end, 15)
        pygame.display.flip()


if __name__ == '__main__':
    game = GameCycle()
    game.main_loop()
    pass