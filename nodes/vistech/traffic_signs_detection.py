#!/usr/bin/env python3
import rospy
import cv2
from cv_bridge import CvBridge
from std_msgs.msg import String
from sensor_msgs.msg import Image
from os import path
from zipfile import ZipFile
import torch
import numpy as np

def detect_trafic_sign():
    bridge = CvBridge()

    pub_detect = rospy.Publisher('detect/string', String, queue_size=0)
    pub_image  = rospy.Publisher('detect/image', Image, queue_size=0)
    pub_camera_image  = rospy.Publisher('camera/image', Image, queue_size=0)
    rospy.init_node('detect_trafic_sign', anonymous=True)
    rate = rospy.Rate(60) 
    vid = cv2.VideoCapture(0)
    dir_path = path.dirname(path.realpath(__file__))
    #Load model
        #Unzip model
    if not(path.exists(dir_path+"/ai_trafic_sign")):
        with ZipFile(dir_path+"/ai_trafic_sign.zip", 'r') as zObject:
            # Extracting all the members of the zip 
            # into a specific location.
            zObject.extractall(
                path=dir_path+"/")
    print('Load model')
    torch.hub.set_dir(dir_path)
    model = None
    if not(path.exists(dir_path+"/WongKinYiu_yolov7_main")):
        model = torch.hub.load("WongKinYiu/yolov7",'custom',dir_path+'/ai_trafic_sign/weights/best.pt',force_reload=True)
    else:
        model = torch.hub.load(dir_path+"/WongKinYiu_yolov7_main",'custom',dir_path+'/ai_trafic_sign/weights/best.pt',source='local',force_reload=True)
    print("Is ready")
    while not rospy.is_shutdown():

        ret, frame = vid.read()
        original_frame = frame.copy()
        resized_original        = cv2.resize(original_frame, (160,160), interpolation = cv2.INTER_AREA)
        image_message_original  = bridge.cv2_to_imgmsg(resized_original, encoding="passthrough")
        pub_camera_image.publish(image_message_original)

        results=model(frame)
        #print(results.names)
        detected = ''
        for i in results.xywhn[0]:
            confidence = float(i[4])
            level = int(i[5])
            name = results.names[level]
            if confidence >0.8:
                #print(confidence,level,name)
                detected = detected +';' +str(name)
        detection = np.squeeze(results.render())
        resized_detection       = cv2.resize(detection, (160,160), interpolation = cv2.INTER_AREA)
        image_message_detected  = bridge.cv2_to_imgmsg(resized_detection, encoding="passthrough")
        pub_detect.publish(detected)
        pub_image.publish(image_message_detected)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        detect_trafic_sign()
    except rospy.ROSInterruptException:
        pass