#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import pdb
import random

'''Initialize agent environment'''
world = np.full((100,100), float(0))

'''Initialize agent motion'''
def agent_up(i,j):
	for x in range(len(world)):
		#pdb.set_trace()
		if j >= 100:
			j = 100
		elif j <= 0:
			j = 0
		else:
			j = j + 1
		plt.plot(i,j,'ro')
		plt.show()

def agent_down(i,j):
	for x in range(len(world)):
		if j >= 100:
			j = 100
		elif j <= 0:
			j = 0
		else:
			j = j - 1
			plt.plot(i,j,'ro')
			plt.show()

def test_down():
	assert agent_down(5,-1) == (5,0)			

def agent_left(i,j):
	for x in range(len(world)):
		if i >= 100:
			i = 100
		elif i <= 0:
			i = 0
		else:
			i = i - 1
			plt.plot(i,j,'ro')
			plt.show()

def agent_right(i,j):
	for x in range(len(world)):
		if i >= 100:
			i = 100
		elif i <= 0:
			i = 0
		else:
			i = i + 1
			plt.plot(i,j,'ro')
			plt.show()


'''Initialize waypoints '''
def waypoints(number_waypoints):
	x_coordinate = []
	y_coordinate = []
	waypoints = []
	for i in range(number_waypoints):	#generates required number of waypoints
		x_coord = random.choice(range(len(world)))   #randomly chooses a number from 0,100 in this case
		x_coordinate.append(x_coord)
	for j in range(number_waypoints):
		y_coord = random.choice(range(len(world)))
		y_coordinate.append(y_coord)

	for i in range(number_waypoints):	#pairing the x and y coordinates 
		waypoint = x_coordinate[i], y_coordinate[i]
		waypoints.append(waypoint)
	print x_coordinate
	print y_coordinate
	print waypoints

waypoints(7)
agent_left(10,30)

'''Initialize start locations'''