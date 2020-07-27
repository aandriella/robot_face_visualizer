#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import String
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
bridge = CvBridge()
def xdisplay_callback(data):
  #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
  try:
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    #cv2.imshow('image', cv_image)
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("window", cv_image)
    cv2.waitKey(1)
  except CvBridgeError as e:
    print(e)
  #cv2.imwrite('/home/aandriella/pal/cognitive_game_ws/src/face_listener/color_img.jpg', cv_image)


def face_listener():
  rospy.init_node('listener', anonymous=True)
  rospy.Subscriber("/robot/expression_diplay", Image, xdisplay_callback)
  rospy.spin()




if __name__ == "__main__":
  face_listener()
