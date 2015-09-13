#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3, Twist
from neato_node.msg import Bump
from sensor_msgs.msg import LaserScan

class StateChanger(object):
	def __init__(self):
		rospy.init_node("states_node")
		self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1) 
		rospy.Subscriber("/bump", Bump, self.getBump) 
		rospy.Subscriber("/scan", LaserScan, self.getScan)
		self.state = 0

	def getBump(self, msg):
		self.bump = msg

	def getScan(self, msg):
		self.scan = msg.ranges[180]

	def goFwd(self):
		print 'fwd'
		self.pub.publish(Twist(linear=Vector3(x=.1)))
		if (msg.leftFront) or (msg.rightFront) or (msg.rightSide) or (msg.leftSide):
			print 'change'
			self.state = 1

	def processScan(self, msg):
		print 'back'
		self.pub.publish(Twist(linear=Vector3(x=0)))
		#self.pub.publish(Twist(linear=Vector3(x=-.1)))
		if self.scan != 0.0 or self.scan < 1:
			self.state = 2 

	def turnLeft(self):
		print 'left'
		#self.pub.publish(Twist(angular=Vector3(z=-.3)))
		#rospy.sleep(1)
		self.state = 0

	def run(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			print 'hi'
			if self.state == 0:
				self.goFwd()
			if self.state == 1:
				self.processScan()
			if self.state == 2:
				self.turnLeft()
			r.sleep()

if __name__ == "__main__":
	state = StateChanger()
	state.run()
