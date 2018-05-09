#!/usr/dev/env python
import sys
import numpy as np
sys.path.append('../environment')
from test_environment import *
from matplotlib import pyplot as plt


# world = np.full((10,10), float(0))
# waypoints = ([4, 6],[4, 2],[7, 9])

def rewards():
	""" This function assigns rewards to all the cells in environment"""
	for i in range(len(reward)):
		for j in range(len(reward)):
			reward[i][j] = -2

	for i,j in waypoints(5):	#reward for getting waypoints is 100
		print (i,j)
		reward[i][j] = 100

	p,q = end_location() 	#reward for getting to end location is 40
	reward[p][q] = 40 

	
	print (reward)

def env_motion():
	""" This function tells the agent what action to take when it is the test environment """
	
	#waypoints(5)

if __name__ == '__main__':
	rewards()
	env_motion()