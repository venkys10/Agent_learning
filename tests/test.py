from .. import test_environment

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

	
