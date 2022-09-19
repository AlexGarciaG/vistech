#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import datetime
import os
import cv2
import sys
class camera_capture_pictures:
    def __init__(self):
        #Pictures
            # Time between pictures 
        self.time_between_pictures = 1
            # Were to save pictures
        self.path_saved_pictures = os.path.expanduser('~')+"/vistec/pictures/"
        os.makedirs(self.path_saved_pictures , exist_ok=True)
            # Pictures to take
        self.pictures_to_take = 2
            #Pictures name
        self.pintures_name      = "Stop"
            #Pictures format
        self.pintures_format    = ".png"
            #Counter
        self.counter = 0
        # OpenCV bridge
        self.bridge = CvBridge()
        # Time
        self.ct = datetime.datetime.now()
        #ROS
        rospy.init_node('camera_transform_to_opencv', anonymous=True)
            #Suscriber
        rospy.Subscriber("/usb_cam_node/image_raw", Image, self.__transform_ros_to_opencv)
        rospy.spin()
        

    def __transform_ros_to_opencv(self,image_message):
        # Get dif 
        dif = (datetime.datetime.now().timestamp()-self.ct.timestamp())        
        if (self.time_between_pictures<int(dif)):
            self.ct = datetime.datetime.now()
            path_name = self.path_saved_pictures+self.pintures_name+self.ct.strftime("%m-%d-%Y_%H-%M-%S")+self.pintures_format
            # Transform openCV
            cv_image = self.bridge.imgmsg_to_cv2(image_message, desired_encoding='bgr8') 
            cv2.imwrite(path_name, cv_image)
            print(self.counter)
            self.counter+=1
        if  self.counter >= self.pictures_to_take:
            rospy.signal_shutdown("All pictures were taken")
    def __del__(self):
        pass

        

if __name__ == '__main__':
    my_camera = camera_capture_pictures()