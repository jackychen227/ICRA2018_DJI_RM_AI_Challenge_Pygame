# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:00:40 2018

@author: Qingwu Chen
"""

import numpy as np

map_cfg = np.loadtxt('./cfg/map_cfg.txt')

red_up_cfg = np.loadtxt('./cfg/red_up_cfg.txt')
red_down_cfg = np.loadtxt('./cfg/red_down_cfg.txt')
red_left_cfg = np.loadtxt('./cfg/red_left_cfg.txt')
red_right_cfg = np.loadtxt('./cfg/red_right_cfg.txt')
red_lu_cfg = np.loadtxt('./cfg/red_lu_cfg.txt')
red_ru_cfg = np.loadtxt('./cfg/red_ru_cfg.txt')
red_ld_cfg = np.loadtxt('./cfg/red_ld_cfg.txt')
red_rd_cfg = np.loadtxt('./cfg/red_rd_cfg.txt')
print (red_ru_cfg)

#RED_0
red_0_lu_cfg    = np.loadtxt('./cfg/robot/red/red_00_lu_cfg.txt')
red_0_up_cfg    = np.loadtxt('./cfg/robot/red/red_01_up_cfg.txt')
red_0_ru_cfg    = np.loadtxt('./cfg/robot/red/red_02_ru_cfg.txt')
red_0_right_cfg = np.loadtxt('./cfg/robot/red/red_03_right_cfg.txt')
red_0_rd_cfg    = np.loadtxt('./cfg/robot/red/red_04_rd_cfg.txt')
red_0_down_cfg  = np.loadtxt('./cfg/robot/red/red_05_down_cfg.txt')
red_0_ld_cfg    = np.loadtxt('./cfg/robot/red/red_06_ld_cfg.txt')
red_0_left_cfg  = np.loadtxt('./cfg/robot/red/red_07_left_cfg.txt')
#RED_1
red_1_lu_cfg    = np.loadtxt('./cfg/robot/red/red_10_lu_cfg.txt')
red_1_up_cfg    = np.loadtxt('./cfg/robot/red/red_11_up_cfg.txt')
red_1_ru_cfg    = np.loadtxt('./cfg/robot/red/red_12_ru_cfg.txt')
red_1_right_cfg = np.loadtxt('./cfg/robot/red/red_13_right_cfg.txt')
red_1_rd_cfg    = np.loadtxt('./cfg/robot/red/red_14_rd_cfg.txt')
red_1_down_cfg  = np.loadtxt('./cfg/robot/red/red_15_down_cfg.txt')
red_1_ld_cfg    = np.loadtxt('./cfg/robot/red/red_16_ld_cfg.txt')
red_1_left_cfg  = np.loadtxt('./cfg/robot/red/red_17_left_cfg.txt')
#BLUE_0
blue_0_lu_cfg    = np.loadtxt('./cfg/robot/blue/blue_00_lu_cfg.txt')
blue_0_up_cfg    = np.loadtxt('./cfg/robot/blue/blue_01_up_cfg.txt')
blue_0_ru_cfg    = np.loadtxt('./cfg/robot/blue/blue_02_ru_cfg.txt')
blue_0_right_cfg = np.loadtxt('./cfg/robot/blue/blue_03_right_cfg.txt')
blue_0_rd_cfg    = np.loadtxt('./cfg/robot/blue/blue_04_rd_cfg.txt')
blue_0_down_cfg  = np.loadtxt('./cfg/robot/blue/blue_05_down_cfg.txt')
blue_0_ld_cfg    = np.loadtxt('./cfg/robot/blue/blue_06_ld_cfg.txt')
blue_0_left_cfg  = np.loadtxt('./cfg/robot/blue/blue_07_left_cfg.txt')
#BLUE_1
blue_1_lu_cfg    = np.loadtxt('./cfg/robot/blue/blue_10_lu_cfg.txt')
blue_1_up_cfg    = np.loadtxt('./cfg/robot/blue/blue_11_up_cfg.txt')
blue_1_ru_cfg    = np.loadtxt('./cfg/robot/blue/blue_12_ru_cfg.txt')
blue_1_right_cfg = np.loadtxt('./cfg/robot/blue/blue_13_right_cfg.txt')
blue_1_rd_cfg    = np.loadtxt('./cfg/robot/blue/blue_14_rd_cfg.txt')
blue_1_down_cfg  = np.loadtxt('./cfg/robot/blue/blue_15_down_cfg.txt')
blue_1_ld_cfg    = np.loadtxt('./cfg/robot/blue/blue_16_ld_cfg.txt')
blue_1_left_cfg  = np.loadtxt('./cfg/robot/blue/blue_17_left_cfg.txt')

blue_up_cfg = np.loadtxt('./cfg/blue_up_cfg.txt')
blue_down_cfg = np.loadtxt('./cfg/blue_down_cfg.txt')
blue_left_cfg = np.loadtxt('./cfg/blue_left_cfg.txt')
blue_right_cfg = np.loadtxt('./cfg/blue_right_cfg.txt')
blue_lu_cfg = np.loadtxt('./cfg/blue_lu_cfg.txt')
blue_ru_cfg = np.loadtxt('./cfg/blue_ru_cfg.txt')
blue_ld_cfg = np.loadtxt('./cfg/blue_ld_cfg.txt')
blue_rd_cfg = np.loadtxt('./cfg/blue_rd_cfg.txt')

redModel = np.dstack((red_lu_cfg, red_up_cfg, red_ru_cfg, red_right_cfg, red_rd_cfg,\
                      red_down_cfg, red_ld_cfg, red_left_cfg))
#print (redModel)
print (red_up_cfg)
blueModel = np.dstack((blue_lu_cfg, blue_up_cfg, blue_ru_cfg, blue_right_cfg, blue_rd_cfg,\
                      blue_down_cfg, blue_ld_cfg, blue_left_cfg))
#print (blueModel)

RED_0_MATRIX = np.zeros((80, 50))
RED_1_MATRIX = np.zeros((80, 50))
BLUE_0_MATRIX = np.zeros((80, 50))
BLUE_1_MATRIX = np.zeros((80, 50))
BLUE_MATRIX = np.zeros((80, 50))
GLOBAL_MATRIX = np.zeros((80, 50))
#GLOBAL_MATRIX = RED_0_MATRIX + RED_1_MATRIX + BLUE_0_MATRIX + BLUE_1_MATRIX

robotModel = {
        0:{"DIR":"LU",    "RED_CFG":{0:red_0_lu_cfg,    1:red_1_lu_cfg},    "BLUE_CFG":{0:blue_0_lu_cfg,    1:blue_1_lu_cfg}},
        1:{"DIR":"UP",    "RED_CFG":{0:red_0_up_cfg,    1:red_1_up_cfg},    "BLUE_CFG":{0:blue_0_up_cfg,    1:blue_1_up_cfg}},
        2:{"DIR":"RU",    "RED_CFG":{0:red_0_ru_cfg,    1:red_1_ru_cfg},    "BLUE_CFG":{0:blue_0_ru_cfg,    1:blue_1_ru_cfg}},
        3:{"DIR":"RIGHT", "RED_CFG":{0:red_0_right_cfg, 1:red_1_right_cfg}, "BLUE_CFG":{0:blue_0_right_cfg, 1:blue_1_right_cfg}},
        4:{"DIR":"RD",    "RED_CFG":{0:red_0_rd_cfg,    1:red_1_rd_cfg},    "BLUE_CFG":{0:blue_0_rd_cfg,    1:blue_1_rd_cfg}},
        5:{"DIR":"DOWN",  "RED_CFG":{0:red_0_down_cfg,  1:red_1_down_cfg},  "BLUE_CFG":{0:blue_0_down_cfg,  1:blue_1_down_cfg}},
        6:{"DIR":"LD",    "RED_CFG":{0:red_0_ld_cfg,    1:red_1_ld_cfg},    "BLUE_CFG":{0:blue_0_ld_cfg,    1:blue_1_ld_cfg}},
        7:{"DIR":"LEFT",  "RED_CFG":{0:red_0_left_cfg,  1:red_1_left_cfg},  "BLUE_CFG":{0:blue_0_left_cfg,  1:blue_1_left_cfg}},
        }

Model = {
        0:{"DIR":"LU", "RED_CFG":red_lu_cfg, "BLUE_CFG":blue_lu_cfg},
        1:{"DIR":"UP", "RED_CFG":red_up_cfg, "BLUE_CFG":blue_up_cfg},
        2:{"DIR":"RU", "RED_CFG":red_ru_cfg, "BLUE_CFG":blue_ru_cfg},
        3:{"DIR":"RIGHT", "RED_CFG":red_right_cfg, "BLUE_CFG":blue_right_cfg},
        4:{"DIR":"RD", "RED_CFG":red_rd_cfg, "BLUE_CFG":blue_rd_cfg},
        5:{"DIR":"DOWN", "RED_CFG":red_down_cfg, "BLUE_CFG":blue_down_cfg},
        6:{"DIR":"LD", "RED_CFG":red_ld_cfg, "BLUE_CFG":blue_ld_cfg},
        7:{"DIR":"LEFT", "RED_CFG":red_left_cfg, "BLUE_CFG":blue_left_cfg},
        }

MOVE_ACTION = {"MOVE_FORWARD":0,
               "MOVE_RIGHT":1,
               "MOVE_BACKWARD":2,
               "MOVE_LEFT":3,
               "NO_ACTION":4}
ROTATE_ACTION = {"ROTATE_LEFT":0,
                 "ROTATE_RIGHT":1,
                 "NO_ACTION":2}
Robot_Param = {
        "RED_0":{"matrix":RED_0_MATRIX, "current":{"modelIndex":4, "x":9, "y":40}},
        "RED_1":{"matrix":RED_1_MATRIX, "current":{"modelIndex":3, "x":8, "y":46}},
        "BLUE_0":{"matrix":BLUE_0_MATRIX, "current":{"modelIndex":5, "x":71, "y":7}},
        "BLUE_1":{"matrix":BLUE_1_MATRIX, "current":{"modelIndex":7, "x":72, "y":2}}
        }  
#机器人矩阵自我更新，全局矩阵通过矩阵相加更新
class robotMatrix:
    def __init__(self, robot_key):
        self.matrix = Robot_Param[robot_key]["matrix"]
        self.currentModelIndex = Robot_Param[robot_key]["current"]["modelIndex"]
        self.current_x = Robot_Param[robot_key]["current"]["x"]
        self.current_y = Robot_Param[robot_key]["current"]["y"]
        self.action = "MOVE_FORWARD"
        self.new_x = self.current_x
        self.new_y = self.current_y
        if robot_key == "RED_0":
            self.blueOrRed =  "RED_CFG"
            self.robotNum = 0
        elif robot_key == "RED_1":
            self.blueOrRed =  "RED_CFG"
            self.robotNum = 1
        elif robot_key == "BLUE_0" :
            self.blueOrRed =  "BLUE_CFG"
            self.robotNum = 0
        elif robot_key == "BLUE_1" :
            self.blueOrRed =  "BLUE_CFG"
            self.robotNum = 1
        print ("lastModel")
        print (robotModel[self.currentModelIndex][self.blueOrRed][self.robotNum])
        self.matrixUpdate(self.action)
    vertex = {
        0:{"x_change":-1, "y_change":-1, "position_x":-3, "position_y":-3, "detection_scale_x":[ 0,+5], "detection_scale_y":[ 0,+5]},
        1:{"x_change": 0, "y_change":-1, "position_x": 0, "position_y":-3, "detection_scale_x":[-2,+3], "detection_scale_y":[ 0, 1]},
        2:{"x_change":+1, "y_change":-1, "position_x":+3, "position_y":-3, "detection_scale_x":[-5, 0], "detection_scale_y":[ 0,+5]},
        3:{"x_change":+1, "y_change": 0, "position_x":+3, "position_y": 0, "detection_scale_x":[ 0, 1], "detection_scale_y":[-2,+3]},
        4:{"x_change":+1, "y_change":+1, "position_x":+3, "position_y":+3, "detection_scale_x":[-5, 0], "detection_scale_y":[-5, 0]},
        5:{"x_change": 0, "y_change":+1, "position_x": 0, "position_y":+3, "detection_scale_x":[-2,+3], "detection_scale_y":[ 0, 1]},
        6:{"x_change":-1, "y_change":+1, "position_x":-3, "position_y":+3, "detection_scale_x":[ 0,+5], "detection_scale_y":[-5, 0]},
        7:{"x_change":-1, "y_change": 0, "position_x":-3, "position_y": 0, "detection_scale_x":[ 0, 1], "detection_scale_y":[-2,+3]},        
        8:{"x_change": 0, "y_change": 0, "position_x": 0, "position_y": 0, "detection_scale_x":[ 0, 1], "detection_scale_y":[ 0, 1]}
        }
    
    @classmethod
    def modelIndexTransform(self, currentModelIndex, action):
        if action in ROTATE_ACTION.keys():
#            action_value = ROTATE_ACTION[action]
#            if action_value == 0:
            if action == "ROTATE_LEFT":
                if currentModelIndex == 0:
                    newModelIndex = 7
                else:
                    newModelIndex = currentModelIndex-1
#            elif action_value == 1:
            elif action == "ROTATE_RIGHT":
                if currentModelIndex == 7:
                    newModelIndex = 0
                else:
                    newModelIndex = currentModelIndex+1
#            elif action_value == 2:
            elif action == "NO_ACTION":
                newModelIndex = currentModelIndex
        else:
            newModelIndex = currentModelIndex
        return newModelIndex
    
    @classmethod
    #边缘检测
    def boundaryViolationDection(self, x_vertex,y_vertex):
        if x_vertex in range(80) and y_vertex in range(50):
            return True
        else:
            return False
        
    @classmethod
    #碰撞检测,在全局地图中进行检测    targetMatrix = GLOBAL_MATRIX
    def collisionDection(self, targetMatrix):
        for element in targetMatrix.flat:
            if element == 0 or element == 1:
                return True
            else:
                return False
            
    @classmethod
    #坐标变换
    def positionTransform(self, targetMatrix, currentModelIndex, x, y, action):
        vertexToDetecte = self.vertex[8]
        x_change = 0
        y_change = 0
        if action in MOVE_ACTION.keys():
            if action != "NO_ACTION":            
                action_value = MOVE_ACTION[action]
                vertexToDetecte_key = (currentModelIndex+action_value*2)%8
                vertexToDetecte = self.vertex[vertexToDetecte_key]
                vertexToDetecte_position_x = x+vertexToDetecte["position_x"]
                vertexToDetecte_position_y = y+vertexToDetecte["position_y"]
                if self.boundaryViolationDection(vertexToDetecte_position_x, vertexToDetecte_position_y):
                    x_min = vertexToDetecte_position_x + vertexToDetecte["detection_scale_x"][0]
                    x_max = vertexToDetecte_position_x + vertexToDetecte["detection_scale_x"][1]
                    y_min = vertexToDetecte_position_y + vertexToDetecte["detection_scale_y"][0]
                    y_max = vertexToDetecte_position_y + vertexToDetecte["detection_scale_y"][1]
                    if self.collisionDection(GLOBAL_MATRIX[x_min:x_max, vertexToDetecte_position_y])\
                    and self.collisionDection(GLOBAL_MATRIX[vertexToDetecte_position_y, y_min:y_max]):                   
                        x_change = vertexToDetecte["x_change"]
                        y_change = vertexToDetecte["y_change"]            
        x_update = x + x_change
        y_update = y + y_change
        return x_update, y_update
    
    def matrixCurrentClear(self, targetMatrix, x, y):        
        for i in range(x-2,x+3) :
            for j in range(y-2,y+3) :
                targetMatrix[i,j] = 0
#                if 38<i<43 and 23<j<28:
#                    targetMatrix[i,j] = 1
#                else:
#                    targetMatrix[i,j] = 0
                    
    @classmethod
    def matrixLocalUpdate(self, targetMatrix, Model, x, y):
        ii = 0
        jj = 0
        print ("newModel")
        print(Model)
        for i in range(x-2,x+3) :
            for j in range(y-2,y+3) : 
#                print(i,j)
#                print(ii,jj)
                targetMatrix[i,j] = Model [jj][ii]
                print(targetMatrix[i,j])
                if jj < 4:
                    jj +=1
                elif jj == 4:
                    jj = 0    
            if ii < 4:
                ii +=1
    
#    def matrixUpdate(self, blueOrRed, action, targetMatrix, currentModelIndex, current_x, current_y):
#        newModelIndex = self.modelIndexTransform(currentModelIndex, action)
#        new_x, new_y = self.positionTransform(self, targetMatrix, currentModelIndex, current_x, current_y, action)
#        if new_x != current_x or new_y != current_y:
#            self.matrixCurrentClear(targetMatrix, current_x, current_y)
#            self.matrixLocalUpdate(targetMatrix, Model[newModelIndex][blueOrRed], new_x, new_y)
#        else:
#            if newModelIndex != currentModelIndex:
#                self.matrixLocalUpdate(targetMatrix, Model[newModelIndex][blueOrRed], new_x, new_y)
#            else:
#                pass
    def matrixUpdate(self, action):
        newModelIndex = self.modelIndexTransform(self.currentModelIndex, action)
        self.new_x, self.new_y = self.positionTransform(self.matrix, self.currentModelIndex, self.current_x, self.current_y, action)
        if self.new_x != self.current_x or self.new_y != self.current_y:
            self.matrixCurrentClear(self.matrix, self.current_x, self.current_y)
#            self.matrixLocalUpdate(self.matrix, Model[newModelIndex][self.blueOrRed], self.new_x, self.new_y)
            self.matrixLocalUpdate(self.matrix, robotModel[newModelIndex][self.blueOrRed][self.robotNum], self.new_x, self.new_y)
        else:
            if newModelIndex != self.currentModelIndex:
                self.matrixLocalUpdate(self.matrix, robotModel[newModelIndex][self.blueOrRed][self.robotNum], self.new_x, self.new_y)
#                robotModel[self.currentModelIndex][self.blueOrRed][self.robotNum]
#                print ("test")
#                print (robotModel[newModelIndex][self.blueOrRed][self.robotNum])
            else:
                pass
        print ("last_pos:",self.current_x, self.current_y)
        self.current_x, self.current_y = self.new_x, self.new_y
        print ("new_pos:",self.current_x, self.current_y)
        print ("lastModelIndex:",self.currentModelIndex)
        self.currentModelIndex = newModelIndex
        print ("newModelIndex:",self.currentModelIndex)
#        print (np.max(self.matrix))
#Init_Position = {
#        "RED_0":{"pos":[9,42], "modelIndex":1},
#        "RED_1":{"pos":[9,48], "modelIndex":3},
#        "BLUE_0":{"pos":[72, 4], "modelIndex":7},
#        "BLUE_1":{"pos":[72,10], "modelIndex":5}
#        }
#"init":{"pos":[9,42], "modelIndex":1}, 

     
#class Red_0(robotMatrix):
#    def __init__(self):
#        self.matrix = RED_0_MATRIX
#        self.currentModelIndex = Init_Position["RED_0"]["modelIndex"]
#        self.current_x = Init_Position["RED_0"]["pos"][0]
#        self.current_x = Init_Position["RED_0"]["pos"][1]
#        self.action = "NO_ACTION"
#        
#    def matrixUpdate(self, action):
#        self.matrixUpdate("RED_CFG",action, self.matrix, self.currentModelIndex, self.current_x, self.current_x)
#        robotMatrix.matrixUpdate(action, self.matrix, self.currentModelIndex, self.current_x, self.current_x)
#class bulletMatrix：
          
red_0 = robotMatrix("BLUE_1")   




  


                    
                  
                    
            
    
    
    
        