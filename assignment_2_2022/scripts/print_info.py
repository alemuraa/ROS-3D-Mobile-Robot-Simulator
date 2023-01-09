#! /usr/bin/env python

import rospy
import math
import time
from assignment_2_2022.msg import Position_velocity

# Frequency with which the info is printed
freq = 1.0

# Last time the info was printed
printed = 0



# Callback function for the info subscriber
def posvel(msg):
	
	global freq, printed
	
	# Compute time period in milliseconds
	period = (1.0/freq) * 1000
	
	# Get current time in milliseconds
	curr_time = time.time() * 1000
	
	
	if curr_time - printed > period:
		
		# Get the desired position
		des_x = rospy.get_param("des_pos_x")
		des_y = rospy.get_param("des_pos_y")
		
		# Get the actual position
		x = msg.x
		y = msg.y
		
		# Compute the distance
		dist = math.dist([des_x, des_y], [x, y])
		
		# Compute the average speed
		average_speed = math.sqrt(msg.v_x**2 + msg.v_y**2)
		
		# print info
		print("Missing distance from desired position: ", dist)
		print("Average speed: ", average_speed,"\n")
		
		# Update printed
		printed = curr_time
	

def main():
	
	# Global variable
	global freq
	
	# Initialize the node
	rospy.init_node('print_info')
	
	# Get the publish frequency parameter
	freq = rospy.get_param("frequency")
	
	# SUBSCRIBER: get from "pos_vel" a parameter (Position_velocity message)
	sub_pos = rospy.Subscriber("/pos_vel", Position_velocity, posvel)
	
	# Wait
	rospy.spin()
	
if __name__ == "__main__":
	main()	
