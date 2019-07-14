# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 20:58:43 2018

@author: Qingwu Chen
"""
#import os
import numpy as np
from const import *

GLOBAL_MAP = np.zeros((50,80), int)
RED_MAP = np.zeros((50,80), int)
BLUE_MAP = np.zeros((50,80), int)

map_cfg = np.loadtxt('./cfg/map_cfg.txt')

red_up_cfg = np.loadtxt('./cfg/red_up_cfg.txt')
red_down_cfg = np.loadtxt('./cfg/red_down_cfg.txt')
red_left_cfg = np.loadtxt('./cfg/red_left_cfg.txt')
red_right_cfg = np.loadtxt('./cfg/red_right_cfg.txt')
red_lu_cfg = np.loadtxt('./cfg/red_lu_cfg.txt')
red_ru_cfg = np.loadtxt('./cfg/red_ru_cfg.txt')
red_ld_cfg = np.loadtxt('./cfg/red_ld_cfg.txt')
red_rd_cfg = np.loadtxt('./cfg/red_rd_cfg.txt')

blue_up_cfg = np.loadtxt('./cfg/blue_up_cfg.txt')
blue_down_cfg = np.loadtxt('./cfg/blue_down_cfg.txt')
blue_left_cfg = np.loadtxt('./cfg/blue_left_cfg.txt')
blue_right_cfg = np.loadtxt('./cfg/blue_right_cfg.txt')
blue_lu_cfg = np.loadtxt('./cfg/blue_lu_cfg.txt')
blue_ru_cfg = np.loadtxt('./cfg/blue_ru_cfg.txt')
blue_ld_cfg = np.loadtxt('./cfg/blue_ld_cfg.txt')
blue_rd_cfg = np.loadtxt('./cfg/blue_rd_cfg.txt')

redModel = np.dstack((red_up_cfg, red_ru_cfg, red_right_cfg, red_rd_cfg,\
                      red_down_cfg, red_ld_cfg, red_left_cfg, red_lu_cfg))
print (redModel)

blueModel = np.dstack((blue_up_cfg, blue_ru_cfg, blue_right_cfg, blue_rd_cfg,\
                      blue_down_cfg, blue_ld_cfg, blue_left_cfg, blue_lu_cfg))
print (blueModel)
#red_robot_model = {
#            "up":red_up_cfg,
#            "ru":red_ru_cfg,
#            "right":red_right_cfg,
#            "rd":red_rd_cfg,
#            "down":red_down_cfg,
#            "ld":red_ld_cfg,
#            "left":red_left_cfg,
#            "lu":red_lu_cfg,         
#            }
#cnt = 0 
#for key, value in red_robot_model.items():
#    print("{}:{}".format(key, value))     
#print ("map_cfg:", map_cfg.shape)
#print ("red_up_cfg:", red_up_cfg.shape)
#print ("red_down_cfg:", red_down_cfg.shape)
print ("Loaded cfg files successfully!")

#filepath = '.\cfg'
#pathDir = os.listdir(filepath)      #获取当前路径下的文件名，返回List
#for s in pathDir:
#    newDir=os.path.join(filepath,s)     #将文件命加入到当前文件路径后面
#    if os.path.isfile(newDir) :         #如果是文件
#        if os.path.splitext(newDir)[1]==".txt":  #判断是否是txt
#            np.loadtxt(newDir)                     #读文件
#            print (newDir)
#            pass

class Map:
#    _CONFIG = {
#            "-1":{"color":BLACK, "class":Obstacle},
#            "0":{"color":WHITE, "class":Free},
#            "1":{"color":GREEN, "class":Bonus},
#            "2":{"color":RED, "class":RedArmor},
#            "3":{"color":BLUE, "class":BlueArmor},
#            "4":{"color":GREEN, "class":RobotEdge},
#            }
#    red_robot_model = {
#            "up":red_up_cfg,
#            "ru":red_ru_cfg,
#            "right":red_right_cfg,
#            "rd":red_rd_cfg,
#            "down":red_down_cfg,
#            "ld":red_ld_cfg,
#            "left":red_left_cfg,
#            "lu":red_lu_cfg,         
#            }
#    cnt = 0 
#    for key, value in red_robot_model.items():
#        print("{}:{}".format(key, value))
        
    @classmethod
    def load(self, mapMatrix):
        for i in range(len(mapMatrix)):
            for j in range(len(mapMatrix[i]-1)):
                print (mapMatrix[i][j])
                gridType = mapMatrix[i][j]
                self.create_map(gridType, j, i)
                
    @classmethod
    def create_map(gridType, x, y):
        if gridType in Map._CONFIG.keys():
            cfg = Map._CONFIG[gridType]
            