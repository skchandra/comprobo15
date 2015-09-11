#!/usr/bin/env python

from visualization_msgs.msg import Marker
from std_msgs.msg import Header, ColorRGBA
import rospy
from geometry_msgs.msg import Vector3, Pose, Point

rospy.init_node('sphere')

type_msg = 2
scale_msg = Vector3(1,1,1)
color_msg = ColorRGBA(255,0,0,1)
pose_msg = Pose(position=Point(1,2,0))

header_msg = Header(stamp=rospy.Time.now(), frame_id="odom")
marker = Marker(header=header_msg, color=color_msg, type=2, pose=pose_msg, scale=scale_msg)

pub = rospy.Publisher("/my_point", Marker, queue_size=10)

r = rospy.Rate(10)
while not rospy.is_shutdown():
	pub.publish(marker)
	r.sleep()
