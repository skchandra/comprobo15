#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Vector3, Twist

rospy.init_node("autonomous")

def up():
	return (.3, 0.0)

def right():
	return (0.0, -.6)

def stop():
	return (0.0, 0.0)

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

def publish(lin, ang):
	msg = Twist(linear=lin, angular=ang)
	pub.publish(msg)
	print msg

lin = Vector3()
ang = Vector3()


t_end = time.time() + 1
while time.time() < t_end:
	lin.x, ang.z = up()
	publish(lin, ang)
	time.sleep(3)
	lin.x, ang.z = right()
	publish(lin, ang)
	time.sleep(3)
	lin.x, ang.z = up()
	publish(lin, ang)
	time.sleep(3)
	lin.x, ang.z = right()
	publish(lin, ang)
	time.sleep(3)
	lin.x, ang.z = up()
	publish(lin, ang)
	time.sleep(3)
	lin.x, ang.z = right()
	publish(lin, ang)
	time.sleep(3)
	lin.x, ang.z = up()
	publish(lin, ang)

