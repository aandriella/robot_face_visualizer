#!/usr/bin/env python

import os
import sys
import rospy
import timeit
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import String



def face_listener():
  rospy.init_node('listener', anonymous=True)
  rospy.Subscriber("/robot/xdisplay", Image, xdisplay_callback)


def get_user_hr_callback(self, msg):
  rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
  rospy.spin()


if __name__ == "__main__":
  face_listener()