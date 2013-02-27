#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#  * Date: 2/27/13
#  * Time: 1:08 PM
#  =============================


import os, sys
import random
import pygame
from pygame.locals import *
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'
import time
import gc
import math

pygame.init()
APPLICATION_w_size = 700
APPLICATION_z_size = 500
screen = pygame.display.set_mode((APPLICATION_w_size, APPLICATION_z_size), RESIZABLE)
#screen = pygame.display.set_mode((APPLICATION_w_size, APPLICATION_z_size), FULLSCREEN)
pygame.display.set_caption("HEHE test circle thingie program    Matthew N. Brown copyright 2007")
#pygame.mouse.set_visible(0)
global background
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))
screen.blit(background, (0, 0))
pygame.display.flip()
random.seed()


## IMAGE STRETCH AND ROTATE: ##
def HEHEHE_font(size):
    fonti = pygame.font.Font(None, size)
    fonti.set_bold(0)
    return fonti
    ## DRAW TEXT IMAGE: ##
def draw_HEHEHE_text (t, special, size, w, z, colory):
    fonty = HEHEHE_font(size)
    IMAGEE = fonty.render(t, special, colory)
    screen.blit(IMAGEE, (w, z))


    ### some functions: ###
def in_repeating_boundy (n, b1, b2):
    if n < b1: n = b2
    if n > b2: n = b1
    return n
def in_boundy (n, b1, b2):
    if n < b1: n = b1
    if n > b2: n = b2
    return n
def in_boundy2D ((w, z), (w1, z1, w2, z2)):
    if w < w1: w = w1
    if w > w2: w = w2
    if z < z1: z = z1
    if z > z2: z = z2
    return w, z
def HEHEHE_distance (w1, z1, w2, z2):
    return math.sqrt(math.pow(w1 - w2, 2) + math.pow(z1 - z2, 2))
def HEHEHE_rect_touching_rect(w1, z1, wol1, zol1, w2, z2, wol2, zol2):
    w2   -= w1
    z2   -= z1
    ww1   = -wol2
    zz1   = -zol2
    return (w2 >= ww1 and w2 <= wol1 and z2 >= zz1 and z2 <= zol1)

    ## keys and mouse stuff: ##
global ky_held, ky_first_held, ky_time_last_pressed
global mouse_w, mouse_z, mouse_inn, mouse_left_pressed, mouse_right_pressed, mouse_left_held, mouse_right_held
not_mouse_left_or_right_held = 1
mouse_left_held = 0
mouse_right_held = 0
mouse_w = 0
mouse_z = 0
mouse_inn = 0
ky_held = [0]
ky_first_held = [0]
ky_time_last_pressed = [0]
m = -1
while (m < 500):
    m += 1
    ky_held += [0]
    ky_first_held += [0]
    ky_time_last_pressed += [0]

    ## MOUSE AND KEY FUNCTIONS: ##
def clear_kys():
    m = -1
    while (m < 500):
        m += 1
        ky_held[m] = 0
        ky_first_held[m] = 0
        ky_time_last_pressed[m] = 0
def mouse_left_pressed_CEV():
    global mouse_left_pressed
    if mouse_left_pressed: mouse_left_pressed = 0; return 1
def mouse_right_pressed_CEV():
    global mouse_right_pressed
    if mouse_right_pressed: mouse_right_pressed = 0; return 1
def old_style_ky(n):
    return (ky_first_held_CEV(n) or (ky_held[n] and ky_time_last_pressed[n] < time.time() - .3))
def ky_first_held_CEV(n):
    if (ky_first_held[n]):
        ky_first_held[n] = 0
        return 1
    else:
        return 0
def mouse_in_rect (w, z, wol, zol):
    return (mouse_w >= w and mouse_z >= z and mouse_w <= w + wol and mouse_z <= z + zol)
def mouse_in_circle (w, z, rad):
    dia = rad * 2
    if mouse_in_rect(w - rad, z - rad, w + dia, z + dia):
        return (HEHEHE_distance(mouse_w, mouse_z, w, z) < rad)
    else:
        return 0

        ## CHECK FOR: KEYBOARD, MOUSE, JOYSTICK, AND OTHERY INPUTY: ##
def check_for_keys():
    global mouse_w, mouse_z, mouse_inn, mouse_left_pressed, mouse_right_pressed, mouse_left_held, mouse_right_held
    global loopy, letter_hitty
    global not_mouse_left_or_right_held
    for e in pygame.event.get():
        if e.type == QUIT:
            loopy = 0
        if e.type == ACTIVEEVENT:
            mouse_inn = (e.gain and (e.state == 1 or e.state == 6))
            if not mouse_inn:
                mouse_w = 0
                mouse_z = 0
        if e.type == KEYDOWN:
            ky_held[e.key] = 1
            ky_first_held[e.key] = 1
            ky_time_last_pressed[e.key] = time.time()
            if (e.key >= 97 and e.key <= 122):
                letter_hitty = e.unicode.lower()
        if e.type == KEYUP:
            ky_held[e.key] = 0
            #ky_first_held[e.key] = 0
        if e.type == MOUSEMOTION:
            mouse_w = e.pos[0]
            mouse_z = e.pos[1]
        if e.type == MOUSEBUTTONUP:
            if e.button == 1: mouse_left_held = 0
            if e.button == 3: mouse_right_held = 0
            if not mouse_left_held and not mouse_right_held: not_mouse_left_or_right_held = 1
        if e.type == MOUSEBUTTONDOWN:
            mouse_left_pressed =  e.button == 1
            mouse_right_pressed = e.button == 3
            mouse_left_held =  mouse_left_held or e.button == 1
            mouse_right_held = mouse_right_held or e.button == 3
            if mouse_left_held or mouse_right_held: not_mouse_left_or_right_held = 0
        if e.type == JOYAXISMOTION: nnnnnn = 7
        if e.type == JOYBALLMOTION: nnnnnn = 8
        if e.type == JOYHATMOTION: nnnnnn = 9
        if e.type == JOYBUTTONUP: nnnnnn = 10
        if e.type == JOYBUTTONDOWN: nnnnnn = 11
        if e.type == VIDEORESIZE:
            global background, Dimage_editing_screen, screen, APPLICATION_w_size, APPLICATION_z_size
            APPLICATION_w_size = e.size[0]
            APPLICATION_z_size = e.size[1]
            screen = pygame.display.set_mode((APPLICATION_w_size, APPLICATION_z_size), RESIZABLE)
            background = pygame.Surface((APPLICATION_w_size, APPLICATION_z_size))
        if e.type == VIDEOEXPOSE: nnnnnn = 13
        if e.type == USEREVENT: nnnnnn = 14

ball_w = 30.0
ball_z = 20.0

ball_wol =  4.0
ball_zol = -1.0

gravity_w = 0.0
gravity_z = 1.0

radius = 11.0

makes_ball_slower_per_bounce = 1.2

if __name__ == '__main__':

# THE MAIN, MAIN, MAIN LOOP:
    loopy = 1
    while (loopy == 1):

        t = time.time()
        while t > time.time() - .03:
            pass
        mouse_left_pressed = 0
        mouse_right_pressed = 0
        check_for_keys()

        ball_wol += gravity_w
        ball_zol += gravity_z

        if old_style_ky(276): ball_wol -= 12
        if old_style_ky(273): ball_zol -= 22
        if old_style_ky(275): ball_wol += 12
        if old_style_ky(274): ball_zol += 22
        if ky_held[115]: ball_wol = 0; ball_zol = 0
        if ky_held[99]: ball_wol = (random.random() * 400) - 200; ball_zol = (random.random() * 400) - 200

        ball_w += ball_wol
        ball_z += ball_zol

        if ball_w <                      radius: ball_w =                      radius; ball_wol = -(ball_wol / makes_ball_slower_per_bounce)
        if ball_z <                      radius: ball_z =                      radius; ball_zol = -(ball_zol / makes_ball_slower_per_bounce)
        if ball_w > APPLICATION_w_size - radius: ball_w = APPLICATION_w_size - radius; ball_wol = -(ball_wol / makes_ball_slower_per_bounce)
        if ball_z > APPLICATION_z_size - radius: ball_z = APPLICATION_z_size - radius; ball_zol = -(ball_zol / makes_ball_slower_per_bounce)

        screen.fill((0, 0, 0))
        draw_HEHEHE_text('Press the arrow keys to move ball.', 0, 25, 0, 0, (255, 255, 255))
        draw_HEHEHE_text('Hold  S  to stop ball.', 0, 25, 0, 30, (255, 255, 255))
        draw_HEHEHE_text('press  C  to make ball go crazy.', 0, 25, 0, 70, (255, 255, 255))
        pygame.draw.circle(screen, (200, 200, 200), (int(ball_w), int(ball_z)), int(radius))

        #if ky_first_held[27]: loopy = 0
        pygame.display.flip()