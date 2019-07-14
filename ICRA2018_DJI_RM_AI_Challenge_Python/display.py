# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 10:06:24 2018

@author: Lenovo
"""

import pygame
import numpy as np
import time
import sys
from pygame.locals import *
#from sys import exit

from const import *
from matrix import *


running = False
pygame.init()


UI_CFG = {
        "GLOBAL":{"targetMatrix":GLOBAL_MATRIX, "pos_index_x":0, "pos_index_y":0, "title":"GLOBAL"},
        "BLUE_0":{"targetMatrix":BLUE_0_MATRIX, "pos_index_x":1, "pos_index_y":0, "title":"BLUE_0"},
        "BLUE_1":{"targetMatrix":BLUE_1_MATRIX, "pos_index_x":1, "pos_index_y":1, "title":"BLUE_1"},
        "RED_0":{"targetMatrix":RED_0_MATRIX, "pos_index_x":2, "pos_index_y":0, "title":"RED_0"},
        "RED_1":{"targetMatrix":RED_1_MATRIX, "pos_index_x":2, "pos_index_y":1, "title":"RED_1"}
        }  

redArmorGridSurf = pygame.Surface(GRID_SCALE_PIXEL)
redArmorGridSurf.fill(RED)
blueArmorGridSurf = pygame.Surface(GRID_SCALE_PIXEL)
blueArmorGridSurf.fill(BLUE)
carGridSurf = pygame.Surface(GRID_SCALE_PIXEL)
carGridSurf.fill(GREEN)
obstacleGridSurf = pygame.Surface(GRID_SCALE_PIXEL)
obstacleGridSurf.fill(WHITE)
freeGridSurf = pygame.Surface(GRID_SCALE_PIXEL)
freeGridSurf.fill(BLACK)
bonusGridSurf = pygame.Surface(GRID_SCALE_PIXEL)
bonusGridSurf.fill(GREEN)
bulletGridSurf = pygame.Surface(GRID_SCALE_PIXEL)
bulletGridSurf.fill(ORANGE)

screen = pygame.display.set_mode((800, 500), 0, 32)
       
class UI:
    gridPixel = 5
    boundary = 10
    fontPixel = 10
    
    matrixNum_x = 3
    matrixNum_y = 2
    textPos_x = np.zeros((matrixNum_x, matrixNum_y))
    textPos_y = np.zeros((matrixNum_x, matrixNum_y))
    matrixPos_x = np.zeros((matrixNum_x, matrixNum_y))
    matrixPos_y = np.zeros((matrixNum_x, matrixNum_y))
    
    matrix_width  = 80*gridPixel
    matrix_height = 50*gridPixel
    
    screen_width  = matrix_width*matrixNum_x + boundary*(matrixNum_x+1)
    screen_height = matrix_height*matrixNum_y + boundary*matrixNum_y + fontPixel*matrixNum_y
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
    screen.fill((255, 255, 255))
    pygame.display.set_caption("ICRA2018 DJI RM AI CHALLENGE-Qingwu Chen")
    for i in range(matrixNum_x):
        for j in range(matrixNum_y):
            textPos_x[i,j] = boundary + (boundary+matrix_width) *i
            textPos_y[i,j] = matrix_height*j + boundary*j + fontPixel*j
            matrixPos_x[i,j] = textPos_x[i,j] 
            matrixPos_y[i,j] = textPos_y[i,j] + fontPixel
#    print ("textPos_x[0,0]",textPos_x[1,0])  
#    print ("matrixPos_x[0,0]",matrixPos_x[1,0])
    
    def __init__(self):
        self.matrixVisualze_init("GLOBAL")

    @classmethod           
    def textDispaly(self,textToDispaly, x, y):
        #创建一个Font对象，freesansbold是Python自带的一种字体
        fontObj=pygame.font.Font("freesansbold.ttf", self.fontPixel)
        
        #render表达
        #fontObj.render(字符串,True或False(指定是否要抗锯齿),字体颜色，[背景底色])的返回一个Surface对象
        #背景颜色(可选)如果想要一个透明的背景，就直接省略这个参数
        textSurfaceObj=fontObj.render(textToDispaly,False,(255, 0, 0),(0, 0, 0))
        screen.blit(textSurfaceObj, (x,y))
    
    @classmethod    
    def matrixDisplayUpdate(self, targetMatrix, x, y):
        for i in range(80):
            for j in range(50):
#                a = x+i*self.gridPixel
#                b = y+j*self.gridPixel
#                print("x==",a)
#                print("y==",b)
                if targetMatrix[i][j] == -1:
                    screen.blit(obstacleGridSurf, (x+i*self.gridPixel, y+j*self.gridPixel))
                elif targetMatrix[i][j] == 0:
                    screen.blit(freeGridSurf,     (x+i*self.gridPixel, y+j*self.gridPixel))
                elif targetMatrix[i][j] == 2 or targetMatrix[i][j] == 3:
                    screen.blit(redArmorGridSurf, (x+i*self.gridPixel, y+j*self.gridPixel))
                elif targetMatrix[i][j] == 4 or targetMatrix[i][j] == 5:
                    screen.blit(blueArmorGridSurf, (x+i*self.gridPixel, y+j*self.gridPixel))
                elif targetMatrix[i][j] == 6:
                    screen.blit(carGridSurf, (x+i*self.gridPixel, y+j*self.gridPixel))

    def ui_DisplayUpdate(self, display_cfg_KEY):
        self.matrixDisplayUpdate(UI_CFG[display_cfg_KEY]["targetMatrix"],\
                                 self.matrixPos_x[UI_CFG[display_cfg_KEY]["pos_index_x"], UI_CFG[display_cfg_KEY]["pos_index_y"]], \
                                 self.matrixPos_y[UI_CFG[display_cfg_KEY]["pos_index_x"], UI_CFG[display_cfg_KEY]["pos_index_y"]])

    def matrixVisualze_init(self, display_cfg_KEY):
        self.ui_DisplayUpdate(display_cfg_KEY)  
        self.textDispaly(UI_CFG[display_cfg_KEY]["title"],\
                         self.textPos_x[UI_CFG[display_cfg_KEY]["pos_index_x"], UI_CFG[display_cfg_KEY]["pos_index_y"]], \
                         self.textPos_y[UI_CFG[display_cfg_KEY]["pos_index_x"], UI_CFG[display_cfg_KEY]["pos_index_y"]])

        
    
       
#screen = pygame.display.set_mode((800, 500), 0, 32)

startTime = time.clock()

red_0 = robotMatrix("BLUE_1")
#red_0.matrixUpdate()  

map_cfg = BLUE_1_MATRIX
#print (map_cfg.shape)
endTime = time.clock()
#print (map_cfg)
ui_test = UI()
ui_test.matrixVisualze_init("BLUE_0")
ui_test.matrixVisualze_init("BLUE_1")
ui_test.matrixVisualze_init("RED_0")
ui_test.matrixVisualze_init("RED_1")
#for i in range(len(map_cfg)):
#    for j in range(len(map_cfg[i])):
##        print (map_cfg[i][j])
#        if map_cfg[i][j] == -1:
#            screen.blit(obstacleGridSurf, (i*GRID_PIXEL, j*GRID_PIXEL))
#        elif map_cfg[i][j] == 0:
#            screen.blit(freeGridSurf, (i*GRID_PIXEL, j*GRID_PIXEL))
#        elif map_cfg[i][j] == 2 or map_cfg[i][j] == 3:
#            screen.blit(redArmorGridSurf, (i*GRID_PIXEL, j*GRID_PIXEL))
#        elif map_cfg[i][j] == 4 or map_cfg[i][j] == 5:
#            screen.blit(blueArmorGridSurf, (i*GRID_PIXEL, j*GRID_PIXEL))
#        elif map_cfg[i][j] == 6:
#            screen.blit(carGridSurf, (i*GRID_PIXEL, j*GRID_PIXEL))
        
print ("Loaded cfg files successfully!")

endTime = time.clock()
print ('Running time: %f Seconds'%(endTime - startTime))

while True:
    for event in pygame.event.get():  
        if event.type == QUIT:  
            pygame.quit()  
            exit  
            running = True  
    if running == True:  
        break
                
    pygame.display.flip()

