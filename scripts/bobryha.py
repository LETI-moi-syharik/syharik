#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('kod_one')
pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
rate = rospy.Rate(10)

def start_talker():
	i = 0
	msg = String()
	while not rospy.is_shutdown():
			hello_str = str(i)
			pub = rospy.Publisher('my_chat_topic', String, queue_size=10)
			rospy.loginfo(hello_str)
			msg.data = hello_str
			pub.publish(msg)
			i = i+2
			rate.sleep()
try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
