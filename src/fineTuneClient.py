#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float64
from std_msgs.msg import UInt32
import roslib
import actionlib

import youbot_nav_msr.msg

def fineTuneClient(stateCmd):
	client=actionlib.SimpleActionClient('fineTuneNav',youbot_nav_msr.msg.locateblockAction)
	client.wait_for_server()
	goal = youbot_nav_msr.msg.locateblockGoal(goalState=stateCmd)
	client.send_goal(goal)
	client.wait_for_result()
	rospy.loginfo("got here")
	return client.get_result

if __name__ == '__main__': 
    try:
    	rospy.init_node("fineTuneClient")
    	motion1 = fineTuneClient(1)
#	rospy.loginfo("got it")
#	if motion1.successOrNot==1:
#		rospy.loginfo("success 0")
#	motion2 = fineTuneClient(1)
#	if motion2.successOrNot==1:
#		rospy.loginfo("success 1")
	rospy.spin()
    except rospy.ROSInterruptException: pass
