#!/usr/bin/env python

import sys
import numpy as np
sys.path.append('./learn')
#from test_environment import *
from matplotlib import pyplot as plt
import pdb

from learn import test_environment as te


gamma = 0.2 	#discount factor
prob = 0.8 		#probability of taking action
reward = -2

# te.world = np.full((10,10), float(0))
# waypoints = ([1,2],[2,5],[5,7], [8,8])

# for i,j in waypoints:
# 	te.world[i][j] = 70

# te.world[9,9] = 30 

def rewards():
	""" This function assigns rewards to all the cells in environment"""
	# for i in range(len(world)):
	# 	for j in range(len(world)):
	# 		world[i][j] = -2

	for i,j in te.waypoints(5):	#reward for getting waypoints is 100
		#print (i,j)
		te.world[i][j] = 100

	p,q = te.end_location() 	#reward for getting to end location is 40
	te.world[p][q] = 40 

	
	return (te.world)

def max_value(x,y):
	""" This function gets maximum value of all adjacent cells to the agent
	TODO: optimize this part """
	x_coord_u = te.agent_up(x,y)[0]
	y_coord_u = te.agent_up(x,y)[1]

	x_coord_d = te.agent_down(x,y)[0]
	y_coord_d = te.agent_down(x,y)[1]

	x_coord_r = te.agent_right(x,y)[0]
	y_coord_r = te.agent_right(x,y)[1]

	x_coord_l = te.agent_left(x,y)[0]
	y_coord_l = te.agent_left(x,y)[1]

	values = (te.world[x_coord_u][y_coord_u], te.world[x_coord_d][y_coord_d], te.world[x_coord_r][y_coord_r], te.world[x_coord_l][y_coord_l])
	if values[0] >= (values[1] and values[2] and values[3]):
		i,j = te.agent_up(x,y)
		return (te.world[i][j])		#gives the value of the cell in the world on top of the current cell
	elif values[1] > (values[0] and values[2] and values[3]):
		i,j = te.agent_down(x,y)
		return (te.world[i][j])
	elif values[2] > (values[0] and values[1] and values[3]):
		i,j = te.agent_right(x,y)
		return (te.world[i][j])
	elif values[3] > (values[0] and values[1] and values[2]):
		i,j = te.agent_left(x,y)
		return (te.world[i][j])

def env_motion_start(x, y):
	""" This function tells the agent what action to take when it is in the test environment 
	TODO: develop complete algorithm"""
	
	rewards()	#Initialize all rewards 

	# for i in range(len(te.world)):
	# 	for j in range(len(te.world)):
	# 		#pdb.set_trace()
	# 		te.world[i][j] += prob * (reward + gamma * max_value(x,y))

	# print (te.world)
	# return (te.world)
	
if __name__ == '__main__':
	print (max_value(2,2))
	#env_motion_start(5,7)