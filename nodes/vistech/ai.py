#!/usr/bin/env python
import rospy
import cv2
from cv_bridge import CvBridge
from std_msgs.msg import String
from sensor_msgs.msg import Image
from os import path
from zipfile import ZipFile
from os import mkdir

def detect_trafic_sign():
    bridge = CvBridge()

    pub_detect = rospy.Publisher('detect/string', String, queue_size=0)
    pub_image  = rospy.Publisher('detect/image', Image, queue_size=0)

    rospy.init_node('detect_trafic_sign', anonymous=True)
    rate = rospy.Rate(60) 
    vid = cv2.VideoCapture(0)
    if not(path.exists("ai_trafic_sign")):
        with ZipFile("./ai_trafic_sign.zip", 'r') as zObject:
        
            # Extracting all the members of the zip 
            # into a specific location.
            zObject.extractall(
                path="./")
    while not rospy.is_shutdown():

        ret, frame = vid.read()
        resized = cv2.resize(frame, (160,160), interpolation = cv2.INTER_AREA)
        image_message = bridge.cv2_to_imgmsg(resized, encoding="passthrough")

        pub_detect.publish("Hola")
        pub_image.publish(image_message)
        rate.sleep()

if __name__ == '__main__':
    try:
        detect_trafic_sign()
    except rospy.ROSInterruptException:
        pass