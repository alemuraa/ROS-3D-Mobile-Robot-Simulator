#! /usr/bin/env python

import rospy
from assignment_2_2022.srv import goal_srv, goal_srvResponse
import actionlib
import actionlib.msg
import assignment_2_2022.msg

# Inizializing variables to count goals cancelled or reached
goal_canc = 0;
goal_reach = 0;

# Function for counting goals actions to send to the subscriber 
def result(msg):
	
	global goal_canc, goal_reach
	
	# Get the status of the result from the msg 
	status = msg.status.status
	
	# Goal cancelled (status = 2)
	if status == 2:
		goal_canc += 1
		
	# Goal reached (status = 3)
	elif status == 3:
		goal_reach += 1
		
# Service function
def data(req):
	
	global goal_canc, goal_reach
	
	# Return the response
	return goal_srvResponse(goal_reach, goal_canc)

def main():

	# Initialize the node
	rospy.init_node('service')
	
	# Create the service
	srv = rospy.Service('service', goal_srv, data)
	
	# SUBSCRIBER: for the result topic
	sub_result = rospy.Subscriber('/reaching_goal/result', assignment_2_2022.msg.PlanningActionResult, result)
	
	# Wait
	rospy.spin()
	
if __name__ == "__main__":
    main()
