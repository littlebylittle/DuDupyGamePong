#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#  * Date: 2/27/13
#  * Time: 6:02 PM
#  =============================
from __future__ import print_function


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


if __name__ == '__main__':
    pass