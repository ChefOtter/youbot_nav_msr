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

	not_norm_w = np.pi/4.0

	pose = PoseStamped()
	pose.header.stamp = rospy.Time.now()
	pose.header.frame_id = "base_footprint"
	pose.pose.position.x=0.0
	pose.pose.position.y=0.0
	pose.pose.position.z=0.0

	robotController = rospy.Publisher('move_base_simple/goal',PoseStamped,queue_size=10)

	rate = rospy.Rate(1.0)
	while not rospy.is_shutdown():
		for i in range(len(scan.ranges)):
			if (i>0) and (abs(scan.ranges[i] < cubeThresh)):
				targeti = i
				targetAngle = scan.angle_min + i*scan.angle_increment

			if (targetAngle > 0) and (abs(targetAngle) > np.pi/10):
				not_norm_w = np.pi/10.0
				rospy.loginfo("turn left")
			elif (targetAngle < 0) and (abs(targetAngle) > np.pi/10):
				not_norm_w = -np.pi/10.0
				rospy.loginfo("turn right")
			else:
				not_norm_w = 0.0
		
		rospy.loginfo(not_norm_w)

		# calculate the normalized Quaternion to send to the robot
		q = np.array([0,0,1,not_norm_w])
		qn = q/np.linalg.norm(q)
		pose.pose.orientation=Quaternion(*qn)

		pose.header.stamp=rospy.Time.now()
		robotController.publish(pose)
		rate.sleep()

if __name__ == '__main__':
    try:
    	rospy.init_node('scan_align')
    	rospy.Subscriber("scan",LaserScan,scanUpdate)
    	alignSensor()
    	rospy.spin()
    except rospy.ROSInterruptException: pass
