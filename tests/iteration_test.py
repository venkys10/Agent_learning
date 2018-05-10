#!/usr/bin/env python
import numpy as np
import sys
sys.path.append('../learn')
import iteration as it
import test_environment as te

te.world = np.full((10,10), float(0))
waypoints = ([1,2],[2,5],[5,7], [8,8])

for i,j in waypoints:
	te.world[i][j] = 70

te.world[9,9] = 30 
# values = (10,20,5,4)

def value_test():
	print (it.max_value(7,8))
	print (te.world)

value_test()


