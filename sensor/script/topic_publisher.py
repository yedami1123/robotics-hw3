#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D
from common_msgs.msg import cmsg

rospy.init_node('common_publisher')
pub = rospy.Publisher('cmsg', cmsg, queue_size=1)
msg = cmsg()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.pose = Pose2D(x=second%4, y=second%7, theta=second%5)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.theta
    rate.sleep()
