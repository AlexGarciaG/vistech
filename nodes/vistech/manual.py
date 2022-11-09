#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Empty
from math import pi

#This class will subscribe to the /number topic and display the received number as a string message
class Control():
    def __init__(self):
        ############################## Max velocity ###################################

        self.robot_velocity = Twist()
        #################################################################################
        self.max_linear_velocity = int(rospy.get_param("~max_linear_velocity", 1.0))
        self.max_angular_velocity = int(rospy.get_param("~max_angular_velocity", pi))
            # Limit number
        self.max_angular_velocity = max(-pi, self.max_angular_velocity)
        self.max_angular_velocity = min(pi, self.max_angular_velocity)

        rospy.on_shutdown(self.on_shutdown)
        ############################### Publisher ######################################
        self.pub_cmd_vel = rospy.Publisher('cmd_vel/manual', Twist, queue_size=1)
        self.pub_enable_autonomous = rospy.Publisher('enable_autonomous', Empty, queue_size=1)
        ############################### SUBSCRIBERS #####################################
        rospy.Subscriber("/joy", Joy, self.__get_data_joy)
        ############ CONSTANTS AND VARIABLES ################
        self.joy_received_flag =False #This flag will tell us when at least one number has been received.
        self.joy = Joy()
        #********** INIT NODE **********###
        r = rospy.Rate(60) #1Hz
        linear_x  = 0
        angular_z = 0
        enable_skip = False
        while not rospy.is_shutdown():

            if self.joy_received_flag: #If the flag is 1, then publish the message
                self.joy_received_flag = False
                if (self.joy.buttons[0]):
                    self.pub_enable_autonomous.publish()
                    enable_skip = True
                    continue
                if (enable_skip):
                    enable_skip = False
                    continue
                
                angular_z, linear_x = self.__calculate_velocity()
                self.robot_velocity.linear.x = linear_x
                self.robot_velocity.angular.z = angular_z
                self.pub_cmd_vel.publish(self.robot_velocity)
                

            r.sleep()
    def __calculate_velocity(self):
        angular_z = -self.joy.axes[0] * self.max_angular_velocity
        linear_x  = self.joy.axes[1] * self.max_linear_velocity
        return angular_z, linear_x
    def __get_data_joy(self, joy):
        self.joy = joy
        self.joy_received_flag = True

    def on_shutdown(self):
        self.robot_velocity.linear.x = 0.0
        self.robot_velocity.angular.z = 0.0
        self.pub_cmd_vel.publish(self.robot_velocity)
        pass

if __name__ == "__main__":
    rospy.init_node("control", anonymous=True)
    Control()