#!/usr/bin/env python
""" ROS node that approaches wall using proportional control """

import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

class WallApproach(object):
	def __init__(self):
		rospy.init_node("wall_approach")
		