#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard %s", msg.data)

rospy.init_node('crocodile')
rospy.Subscriber('lezhit_hodya', String, callback, queue_size=10)
rospy.spin()

