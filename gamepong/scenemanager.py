#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#  * Date: 2/27/13
#  * Time: 6:06 PM
#  =============================
#from __future__ import print_function
import pygame


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

        pygame.draw.line(self.screen, Scene.colors['white'],
                         middle_line_begin, middle_line_end, 15)

        # if self.ball:
        #     #self.ball.draw(self)
        #     pygame.draw.circle(self.screen, Scene.colors['white'],
        #                        (self.ball.rect.x, self.ball.rect.y), self.ball.size, 0)
        #     pygame.draw.circle(self.screen, Scene.colors['red'],
        #                        (self.ball.rect.x, self.ball.rect.y), self.ball.size + 1, 2)
        #
        # if self.left_pin:
        #     rect = [(0, self.left_pin.rect.y), (self.left_pin.width, self.left_pin.height)]
        #     pygame.draw.rect(self.screen, Scene.colors['white'], rect, 0)
        #
        # if self.right_pin:
        #     rect = [(self.right_pin.rect.x - self.right_pin.width, self.right_pin.rect.y),
        #             (max_x + 1, self.right_pin.height)]
        #     pygame.draw.rect(self.screen, Scene.colors['white'], rect, 0)

        self.screen.displayed_sprites.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    pass