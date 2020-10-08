import Map
import PathFinder
import RobotMessage
import numpy as np


sokobanMap = Map.Map('testmap.txt', 3, 3)
print('File name: ' + sokobanMap.fileName)
print('Map: ')
print(sokobanMap.map)