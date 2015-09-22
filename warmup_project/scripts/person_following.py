#!/usr/bin/env python
"""Program to wall follow a wall on the right side of the robot
Shivali Chandra
9/13/15"""

import rospy
from geometry_msgs.msg import Vector3, Twist
from sensor_msgs.msg import LaserScan
import math

class PersonFollow(object):

	def __init__(self):
		rospy.init_node("person_follow_node")
		self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
		rospy.Subscriber("/scan", LaserScan, self.processScan) 

	def processScan(self, msg):
		leftScan = msg.ranges[0:30] #left side
		leftFound = [i for i in leftScan if i < 1 and i != 0.0]
		rightScan = msg.ranges[330:360] #right side
		rightFound = [i for i in rightScan if i < 1 and i != 0.0]
		allScan = leftFound+rightFound
		
		if (len(allScan) == 0): #if nothing found in field of vision just go straight
			avgDist = 1.2
		else:
			avgDist = sum(allScan)/len(allScan)
		
		ang = (len(leftFound) - len(rightFound)) * .08 #proportional control for turning
		dist = (avgDist - 1) * .75 #proportional control for moving fwd
		
		print ang, dist
		self.pub.publish(Twist(linear=Vector3(x=dist), angular=Vector3(z=ang)))
	
	def run(self):
		r = rospy.Rate(20)
		while not rospy.is_shutdown():
			r.sleep()

if __name__ == '__main__':
	follow = PersonFollow()
	follow.run()
			