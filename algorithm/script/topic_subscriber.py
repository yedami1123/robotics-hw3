#!/usr/bin/env python
import rospy
from common_msgs.msg import cmsg

def callback(msg):
    print "subscribe: ", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.theta

rospy.init_node('common_subscriber')
sub = rospy.Subscriber('cmsg', cmsg, callback)
rospy.spin()
