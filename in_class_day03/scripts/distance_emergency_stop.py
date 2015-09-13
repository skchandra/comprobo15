#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Vector3, Twist
from sensor_msgs.msg import LaserScan


class Emergency_stop(object):
	def __init__(self):
		rospy.init_node("dist_emergency_stop_node")
		self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
		rospy.Subscriber("/scan", LaserScan, self.processScan) 

	def processScan(self, msg):
		print msg.ranges[180]
		if msg.ranges[180] == 0.0 or msg.ranges[0] > 1:
			self.pub.publish(Twist(linear=Vector3(x=.05)))
		else:
			self.pub.publish(Twist())
		
	def run(self):
		r = rospy.Rate(10)
		while not rospy.is_shutdown():
			r.sleep()

if __name__ == '__main__':
	stop = Emergency_stop()
	stop.run()