"""
constant value, should be capital 
"""

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480
CAMERA_FPS = 30

WIDTH_FOV = 24.273#29.5
HEIGHT_FOV = 19.013#22.6

ROBOT_ANGLE = 60 #기본자세 머리 각도. 231012 기준

ROBOT_HEIGHT = 32.5

# 대회 세팅
# YELLO_MASK = [[23,59,118],[62,190,242]]
# RED_MASK = [[158,172,123],[191,246,242]]#[[63,79,145],[179,255,255]] 

# 케1 세팅
YELLO_MASK = [[20,96,162],[120,226,255]]
RED_MASK = [[130,71,118],[255,255,255]]


TASK_FLAG = 1
NOW = 0
DELAY_TIME = 500000 #0.5s

# NECK_LIST = [39, 33, 82, 34, 80, 36, 78]#[39, 33, 37, 34, 31, 36, 29] # 순서대로 20도, 30도, 40도, 50도, 60도, 70도, 80도
NECK_LIST = [84, 83, 82, 81, 80, 79, 78] 
NECK_VALUE = [20, 30, 40, 50, 60, 70, 80]
NECK_POINTER = 0
NECK_PREPOINTER = 0

FALLDOWN_FLAG = 0
RCV_RX = 0

HIT_NUM = 0