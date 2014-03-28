#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#  =============================
from __future__ import print_function
import gamepong

if __name__ == '__main__':
    game = gamepong.GameCycle(resolution=[1300, 300])
    game.main_loop()
    pass
