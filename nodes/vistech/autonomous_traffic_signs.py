#!/usr/bin/env python3
from cmath import inf
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from math import pi
#This class will subscribe to the /number topic and display the received number as a string message
class Control():
    def __init__(self):
        ############################## Max velocity ###################################
        max_linear_velocity = float(rospy.get_param("~max_linear_velocity", 1.0))
        max_distance = 12.0
        self.linear_proportional = max_linear_velocity/max_distance
        self.min_distance_to_move = 0.75
        max_angular_velocity = float(rospy.get_param("~max_angular_velocity", pi))
        max_radius = pi
        self.angular_proportional = max_angular_velocity/max_radius
        self.min_radius_to_move = (6*pi)/180.0
        self.robot_velocity = Twist()
        #################################################################################
        rospy.on_shutdown(self.on_shutdown)
        ############################### Publisher ######################################
        self.pub = rospy.Publisher('cmd_vel/traffic_signs', Twist, queue_size=1)
        ############################### SUBSCRIBERS #####################################
        rospy.Subscriber("/detect/string", String, self.__get_data_ai)
        ############ CONSTANTS AND VARIABLES ################
        self.ai_received_flag = False #This flag will tell us when at least one number has been received.
        self.ai = String()
        #********** INIT NODE **********###
        r = rospy.Rate(1) #1Hz
        near_object = 0
        angle       = 0
        linear_x    = 0
        angular_z   = 0
        while not rospy.is_shutdown():
            if self.ai_received_flag: #If the flag is 1, then publish the message
                self.ai_received_flag = False
                near_object, angle = self.__get_velocity()

                linear_x = near_object*self.linear_proportional
                angular_z = -angle*self.angular_proportional

            rospy.loginfo("Linear velocity:"+str(linear_x)+" Angular velocity:" + str(angular_z))
            self.robot_velocity.linear.x = linear_x
            self.robot_velocity.angular.z = angular_z
            self.pub.publish(self.robot_velocity)
            r.sleep()
    # Suscriber
    def __get_data_ai(self, ai_string):
        self.ai = ai_string
        self.ai_received_flag = True
    #Functions
    def __get_velocity(self):
        return 1,0
    #on_shutdown
    def on_shutdown(self):
        self.robot_velocity.linear.x = 0.0
        self.robot_velocity.angular.z = 0.0
        self.pub.publish(self.robot_velocity)
        pass

if __name__ == "__main__":
    rospy.init_node("control", anonymous=True)
    Control()