#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D
from common_msgs.msg import cmsg
from common_msgs.srv import csrv, csrvRequest

rospy.init_node('common_publisher')
rospy.wait_for_service('add_two_number')
requester = rospy.ServiceProxy('add_two_number', csrv)
pub = rospy.Publisher('cmsg', cmsg, queue_size=1)
msg = cmsg()a
rate = rospy.Rate(10)
count = 0

while not rospy.is_shutdown():
    if count % 10 == 0:
        req = csrvRequest(a=count, b=count/2)
        res = requester(req)
        print count, "request:", req.a, req.b, "response:", res.sum
    count += 1
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.pose = Pose2D(x=second%4, y=second%7, theta=second%5)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.theta
    rate.sleep()
