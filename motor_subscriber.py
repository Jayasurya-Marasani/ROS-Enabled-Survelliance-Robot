#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import String 
def callback(msg): print(msg.data)
rospy.init_node('listener',anonymous=True)
sub=rospy.Subscriber('chatter',String,callback)
rospy.spin()