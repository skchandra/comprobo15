#!/usr/bin/env python
"""Program to wall follow a wall on the right side of the robot
Shivali Chandra
9/13/15"""

import rospy
from geometry_msgs.msg import Vector3, Twist
from sensor_msgs.msg import LaserScan

class WallFollow(object):
	def __init__(self):
		rospy.init_node("wall_follow_node")
		self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
		rospy.Subscriber("/scan", LaserScan, self.processScan) 

	def processScan(self, msg):
		self.scan315 = msg.ranges[315]	
		ang = -.8*(self.scan315-0.75) #proportional control of direction to turn if needed
		self.pub.publish(Twist(linear=Vector3(x=.05), angular=Vector3(z=ang))) #publish msg to move

	def run(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			r.sleep()
			
if __name__ == '__main__':
	follow = WallFollow()
	follow.run()

