#!/usr/bin/env python

import rospy
import math
import numpy as np
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import UInt32
from geometry_msgs.msg import Quaternion

cubeThresh = 0.5

scan = LaserScan()

def scanUpdate(lScan):
	global scan
	scan = lScan

def alignSensor():
	global scan

	idealTurn = Twist()
	targetAngle=0.0

	robotController = rospy.Publisher('cmd_vel',Twist,queue_size=10)

	rate = rospy.Rate(1.0)
	while not rospy.is_shutdown():
		for i in range(len(scan.ranges)):
			if (i>0) and (abs(scan.ranges[i] < cubeThresh)):
				targeti = i
				targetAngle = scan.angle_min + i*scan.angle_increment

			if (targetAngle > 0) and (abs(targetAngle) > np.pi/100):
				idealTurn.angular.z = 0.1
				rospy.loginfo("turn left")
			elif (targetAngle < 0) and (abs(targetAngle) > np.pi/100):
				idealTurn.angular.z = -0.1
				rospy.loginfo("turn right")
			else:
				idealTurn.angular.z = 0.0
		
		rospy.loginfo(targetAngle)
		robotController.publish(idealTurn)
		rate.sleep()

if __name__ == '__main__':
    try:
    	rospy.init_node('scan_align')
    	rospy.Subscriber("scan",LaserScan,scanUpdate)
    	alignSensor()
    	rospy.spin()
    except rospy.ROSInterruptException: pass
