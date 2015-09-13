#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Vector3, Twist
from neato_node.msg import Bump


class Emergency_stop(object):
	def __init__(self):
		rospy.init_node("emergency_stop_node")
		self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
		rospy.Subscriber("/bump", Bump, self.processBump) 

	def processBump(self, msg):
		if (msg.leftFront) or (msg.rightFront) or (msg.rightSide) or (msg.leftSide):
			self.pub.publish(Twist(linear=Vector3(x=-.1)))
		else:
			self.pub.publish(Twist(linear=Vector3(x=.1)))

	
	def run(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			r.sleep()

if __name__ == '__main__':
	stop = Emergency_stop()
	stop.run()

