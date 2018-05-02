#!/usr/bin/env python

import numpy as np
#import matplotlib.pyplot as plt
import pdb
import random

'''Initialize agent environment'''
"""This sets up the environment by generating a grid within which the agent must act."""
world = np.full((100,100), float(0))

'''Initialize agent motion'''
"""The motion of the agent when it is supposed to move up by one step at a time."""
def agent_up(i,j):
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

"""The motion of the agent when it is supposed to move down by one step at a time."""
def agent_down(i,j):
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

def tests():
	#test under six possible cases i.e coordinates going to far left, right, up, down, both coordinates going away
	'''Test when agent is moving down'''
	assert agent_down(5,-1) == (5,0)	
	assert agent_down(-10, 50) == (0, 49)	
	assert agent_down(10, 150) == (10, 100)
	assert agent_down(105, 50) == (100, 49)
	assert agent_down(106, 107) == (100, 100)
	assert agent_down(-10, -50) == (0, 0)

	'''Test when agent is moving up'''
	assert agent_up(5,102) == (5,100)	#test when y_coordinate is going above grid
	assert agent_up(105,10) == (100,11)
	assert agent_up(-5,90) == (0,91)
	assert agent_up(5,-6) == (5,0)	#test when both coordinates leave grid
	assert agent_up(105, 150) == (100, 100)
	assert agent_up(-10, -50) == (0, 0)

	'''Test when agent is moving left'''
	assert agent_left(20,-10) == (19,0)		#test when y_coordinate is going to the left end of grid
	assert agent_left(20, 110) == (19,100)
	assert agent_left(-20, 90) == (0,90)
	assert agent_left(120, 90) == (100,90)	#test when y_coordinate is going to the right end of grid
	assert agent_left(120, 110) == (100,100)
	assert agent_left(-8, -10) == (0,0)

	'''Test when agent is moving to the right'''
	assert agent_right(20, 120) == (21, 100)	#test when y_coordinate is going to the right end of grid
	assert agent_right(-10, 50) == (0, 50)		#test when x_coordinate goes to the left end of grid
	assert agent_right(105, 50) == (100, 50)
	assert agent_right(10, -5) == (11, 0)
	assert agent_right(103, 105) == (100, 100)
	assert agent_right(-10, -5) == (0, 0)
	

"""The motion of the agent when it is supposed to move left by one step at a time."""
def agent_left(i,j):
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

"""The motion of the agent when it is supposed to move right by one step at a time."""
def agent_right(i,j):
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
		waypoint = x_coordinate[i], y_coordinate[i]
		waypoints.append(waypoint)
	print (x_coordinate)
	print (y_coordinate)
	print (waypoints)
	
'''Initialize end locations'''
def end_location():
	"""Agent collects the waypoints and goes to these coordinates"""
	x_coordinate = random.choice(range(len(world)))
	y_coordinate = random.choice(range(len(world)))
	end_location = x_coordinate, y_coordinate
