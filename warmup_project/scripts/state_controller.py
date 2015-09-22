#!/usr/bin/env python
"""Program to wall follow a wall on right side and then object avoid when 
another wall or obstacle in the way is reached. 
Shivali Chandra
9/20/15"""

import rospy
from geometry_msgs.msg import Vector3, Twist
from sensor_msgs.msg import LaserScan

class StateController(object):
	def __init__(self):
		rospy.init_node("state_controller_node")
		self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
		rospy.Subscriber("/scan", LaserScan, self.processScan) 
		self.state = 0 #to see which behavior robot is doing in terminal

	def processScan(self, msg):
		print self.state
		self.scan315 = msg.ranges[315]
		print self.scan315, msg.ranges[0]
		#if self.state == 0:
		if self.scan315 < 0.7 and msg.ranges[0] > 0.5: #if certain scan within range, wall follow
			self.state = 0
			ang = -.8*(self.scan315-0.6) #proportional control of direction to turn if needed
			self.pub.publish(Twist(linear=Vector3(x=.05), angular=Vector3(z=ang))) #publish msg to move
		else: #otherwise avoid obstacles
			self.state = 1
			scan = dict()
			for i in range(0, 360):
				scan[i] = msg.ranges[i]
			scanLeftFront = [(i, scan[i]) for i in scan if (i < 91 and i > 0 and scan[i] < .6 and scan[i] != 0.0)]
			scanRightFront = [(i, scan[i]) for i in scan if (i > 270 and i < 360 and scan[i] < .6 and scan[i] != 0.0)]
			scanLeftBack = [(i, scan[i]) for i in scan if (i < 181 and i > 90 and scan[i] < .6 and scan[i] != 0.0)]
			scanRightBack = [(i, scan[i]) for i in scan if (i > 180 and i < 271 and scan[i] < .6 and scan[i] != 0.0)]
			#if there is more to avoid on left side then turn right
			ang = len(scanRightFront) - len(scanLeftFront) * .01
			#dist = .05
			if (len(scanRightBack)+len(scanLeftBack)) > 0:
				dist = (len(scanRightBack)+len(scanLeftBack) - 1) * .05
			else: 
				dist = .05
			self.pub.publish(Twist(linear=Vector3(x=dist), angular=Vector3(z=ang)))

	def run(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			r.sleep()
			
if __name__ == '__main__':
	state = StateController()
	state.run()