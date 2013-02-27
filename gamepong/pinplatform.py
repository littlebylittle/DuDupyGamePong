#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#  * Date: 2/27/13
#  * Time: 6:05 PM
#  =============================
#from __future__ import print_function


class Pin:
    def __init__(self, surface):
        self.surface = surface
        self.width = 10
        self.max_x, self.max_y = surface.get_size()
        self.y = self.max_y // 2
        self.height = self.max_y // 7
        self.dmove = 0
        print(self.y)

    def set_y_move(self, dmove):
        self.dmove = dmove

    def move(self):
        if (self.y + self.height + self.dmove) > self.max_y:
            self.y = abs(self.max_y - self.height)
            print self.y
        elif self.y + self.dmove < 0:
            self.y = 0
        else:
            self.y += self.dmove


if __name__ == '__main__':
    pass