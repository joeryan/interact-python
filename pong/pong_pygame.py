# simple pong game in pygame
# Author: Joe Ryan
# 21 MAR 2015

import sys, pygame
import time

pygame.init()

size = width, height = 720, 500
ball_vel = [1,1]
black = 0, 0, 0
white = 255, 255, 255
pad_w = 400
pad_h = 80

screen = pygame.display.set_mode(size)

ball = pygame.image.load('pong_ball.gif')
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(ball_vel)
    time.sleep(0.001)
    if ballrect.left < 0 or ballrect.right > width:
        ball_vel[0] = -ball_vel[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        ball_vel[1] = -ball_vel[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    l_gut = pygame.draw.line(screen, white, (pad_w, 0), (pad_w, height), 4)

