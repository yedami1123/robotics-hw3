#!/usr/bin/env python
import rospy
from common_msgs.msg import cmsg
from common_msgs.srv import csrv, csrvResponse


def callback(msg):
    print "subscribe: ", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.theta
def service_callback(request):
    response = csrvResponse(sum=request.a + request.b)
    print "request data:", request.a, request.b, ", response:", response.sum
    return response

rospy.init_node('common_subscriber')
sub = rospy.Subscriber('cmsg', cmsg, callback)
service = rospy.Service('add_two_number', csrv, service_callback)
rospy.spin()
