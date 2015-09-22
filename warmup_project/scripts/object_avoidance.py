#!/usr/bin/env python
"""Program to avoid objects and continuously move around a room.
Shivali Chandra
9/15/15""" 

import rospy
from geometry_msgs.msg import Vector3, Twist, Pose
from sensor_msgs.msg import LaserScan

class ObjectAvoid(object):

	def __init__(self):
		rospy.init_node("object_avoid_node")
		self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
		rospy.Subscriber("/scan", LaserScan, self.processScan) 

	def processScan(self, msg):
		"""Function to take in scan, store values if objects are detected within a certain range
		and direct the robot to turn and move away from the object until it is gone from the field
		of vision. Ideally, this directs the robot to traverse a room in a circle"""
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
			dist = .1
		self.pub.publish(Twist(linear=Vector3(x=dist), angular=Vector3(z=ang)))
			
	def run(self):
		r = rospy.Rate(5)
		while not rospy.is_shutdown():
			r.sleep()

if __name__ == '__main__':
	obj = ObjectAvoid()
	obj.run()
