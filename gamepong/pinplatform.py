#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#  * Date: 2/27/13
#  * Time: 6:05 PM
#  =============================
#from __future__ import print_function
import pygame


class Pin(pygame.sprite.Sprite):
    def __init__(self, surface, x_pos):

        pygame.sprite.Sprite.__init__(self)
        self.surface = surface
        self.max_x, self.max_y = surface.get_size()

        self.width = 10
        self.height = self.max_y // 7

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill([0xff, 0xff, 0xff])
        self.rect = self.image.get_rect()
        self.rect.y = self.max_y // 2
        self.rect.x = x_pos
        if self.rect.x > (self.max_x - self.width):
            self.rect.x = self.max_x - self.width

        self.dmove = 0
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill([0xff, 0xff, 0xff])

    def set_y_move(self, dmove):
        self.dmove = dmove

    def move(self):
        if (self.rect.y + self.height + self.dmove) > self.max_y:
            self.rect.y = abs(self.max_y - self.height)
        elif self.rect.y + self.dmove < 0:
            self.rect.y = 0
        else:
            self.rect.y += self.dmove


if __name__ == '__main__':
    pass