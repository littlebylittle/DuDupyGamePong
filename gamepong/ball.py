#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#  * Date: 2/27/13
#  * Time: 6:02 PM
#  =============================
from __future__ import print_function
import pygame
from random import randint

class Ball(pygame.sprite.Sprite):
    size = 15

    def __init__(self, gcycle,):
        pygame.sprite.Sprite.__init__(self)
        self.speed_x = randint(1, 3)
        self.speed_y = randint(1, 3)
        self.callobj = gcycle
        self.max_value_x, self.max_value_y = gcycle.screen.get_size()

        self.image = pygame.Surface([Ball.size, Ball.size])
        self.image.fill([0xff, 0xff, 0xff])

        self.rect = self.image.get_rect()
        self.rect.x = self.max_value_x // 2
        self.rect.y = self.max_value_y // 2

        #block list - engine for calculating collision between shapes
        self.block_list = pygame.sprite.RenderPlain()
        self.block_list.add(gcycle.left_pin)
        self.block_list.add(gcycle.right_pin)

    def move(self):
        result = pygame.sprite.spritecollide(self, self.block_list, False)
        if result:
            self.speed_x *= -1
            self.speed_y *= -1
            self.speed_y -= 1

        if self.rect.x < (self.callobj.left_pin.rect.x // 2):
            self.callobj.game_score[1] += 1
            self.speed_x *= -1
            self.rect.x = self.max_value_x // 2
            self.rect.y = self.max_value_y // 2


        if self.rect.x > self.max_value_x:
            self.speed_x *= -1

        if self.rect.y > (self.max_value_y - self.size // 2) or self.rect.y < 0:
            self.speed_y *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

if __name__ == '__main__':
    pass