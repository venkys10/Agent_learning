#!/usr/bin/env python

import numpy as np
#import matplotlib.pyplot as plt
import pdb
import random

'''Initialize agent environment'''
"""This sets up the environment by generating a grid within which the agent must act."""
world = np.full((100,100), float(0))

'''Initialize agent motion'''
"""The motion of the agent when it is supposed to move right by one step at a time."""
def agent_right(i,j):
	for x in range(len(world)):
		#pdb.set_trace()
		if j >= 100:
			j = 100 
		elif j <= 0:
			j = 0
		else:
			j = j + 1

		if i >= 100:
			i = 100
		elif i <= 0:
			i = 0
		return (i,j)
		#plt.plot(i,j,'ro')
		#plt.show()

"""The motion of the agent when it is supposed to move left by one step at a time."""
def agent_left(i,j):
	for x in range(len(world)):
		if j >= 100:
			j = 100 
		elif j <= 0:
			j = 0
		else:
			j = j - 1

		if i >= 100:
			i = 100
		elif i <= 0:
			i = 0
		return (i,j)
			#plt.plot(i,j,'ro')
			#plt.show()
	

"""The motion of the agent when it is supposed to move up by one step at a time."""
def agent_up(i,j):
	for x in range(len(world)): 
		if i >= 100:
			i = 100
		elif i <= 0:
			i = 0
		else:
			i = i - 1
		
		if j >= 100:
			j = 100
		elif j <= 0:
			j = 0
		return (i,j)
			#plt.plot(i,j,'ro')
			#plt.show()

"""The motion of the agent when it is supposed to move down by one step at a time."""
def agent_down(i,j):
	for x in range(len(world)):
		if j >= 100:
			j = 100 
		elif j <= 0:
			j = 0

		if i >= 100:
			i = 100
		elif i <= 0:
			i = 0
		else:
			i = i + 1
		return (i,j)
			#plt.plot(i,j,'ro')
			#plt.show()


'''Initialize waypoints '''
"""The waypoints for the agent to collect infromation from are initialized. The agent will follow the below generated waypoints in each run"""
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
		waypoint = [x_coordinate[i], y_coordinate[i]]
		waypoints.append(waypoint)
	#print (x_coordinate)
	#print (y_coordinate)
	return (waypoints)
	
'''Initialize end locations'''
def end_location():
	"""Agent collects the waypoints and goes to these coordinates"""
	x_coordinate = random.choice(range(len(world)))
	y_coordinate = random.choice(range(len(world)))
	end_location = x_coordinate, y_coordinate
	return (end_location)
