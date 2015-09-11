#!/usr/bin/env python
import tty
import select
import sys
import termios
import rospy
from geometry_msgs.msg import Vector3, Twist

rospy.init_node("teleop")

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key

def left():
	return (0.0, .5)

def up():
	return (.5, 0.0)

def right():
	return (0.0, -.5)

def down():
	return (-.5, 0.0)

def stop():
	return (0.0, 0.0)

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

settings = termios.tcgetattr(sys.stdin)
key = None

while key != '\x03':
	key = getKey()
	lin = Vector3()
	ang = Vector3()

	if (ord(key) == 97):
		lin.x, ang.z = left()
	elif (ord(key) == 119):
		lin.x, ang.z = up()
	elif (ord(key) == 100):
		lin.x, ang.z = right()
	elif (ord(key) == 120):
		lin.x, ang.z = down()
	elif (ord(key) == 115):
		lin.x, ang.z = stop()
	else:
		print "invalid"

	msg = Twist(linear=lin, angular=ang)
	pub.publish(msg)
	print msg
    