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
		self.state = 0

	def processScan(self, msg):
		self.scan315 = msg.ranges[315]
		self.scanRight = msg.ranges[270]	
		print self.scan315, self.scanRight
		if self.scan315 > 0.8 and self.scanRight > .5: #if too far away move fwd until you find a wall
			self.state = 0
		if self.scan315 > 0.8: #if turning away from wall
			self.state = 1
		if self.scan315 < 0.73: #if too close to wall
			self.state = 2


	def goFwd(self):
		print 'fwd'
		self.pub.publish(Twist(linear=Vector3(x=.07)))
		
	def turnLeft(self):
		print 'left'
		while self.scan315 < 0.74:
			self.pub.publish(Twist(angular=Vector3(z=.1)))
		self.state = 0

	def turnRight(self):
		print 'right'
		while self.scan315 > 0.75:
			self.pub.publish(Twist(angular=Vector3(z=-.1)))
		self.state = 0

	def run(self):
		r = rospy.Rate(20)
		while not rospy.is_shutdown():
			r.sleep()
			if self.state == 0:
				self.goFwd()
			if self.state == 1:
				self.turnRight()
			if self.state == 2:
				self.turnLeft()

if __name__ == '__main__':
	stop = WallFollow()
	stop.run()
			
