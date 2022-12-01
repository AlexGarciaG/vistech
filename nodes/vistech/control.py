#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from std_msgs.msg import Empty
from math import pi
from time import sleep

#This class will subscribe to the /number topic and display the received number as a string message
class Control():
    def __init__(self):
        ############################## Max velocity ###################################

        self.manual_velocity = Twist()
        self.follow_closest_object_velocity = Twist()
        self.traffic_signs_velocity = Twist()
        self.robot_velocity = Twist()
        #################################################################################
        self.max_linear_velocity = float(rospy.get_param("~max_linear_velocity", 1.0))
        self.max_angular_velocity = float(rospy.get_param("~max_angular_velocity", pi))
            # Limit number
        self.max_angular_velocity = max(-pi, self.max_angular_velocity)
        self.max_angular_velocity = min(pi, self.max_angular_velocity)

        rospy.on_shutdown(self.on_shutdown)
        ############################### Publisher ######################################
        self.pub_cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        ############################### SUBSCRIBERS #####################################
        rospy.Subscriber("/joy", Joy, self.__get_data_joy)
        rospy.Subscriber("/joy_remote", Joy, self.__get_data_joy)
        rospy.Subscriber("cmd_vel/follow_closest_object", Twist, self.__cmd_vel_autonomous_follow_closest_object)
        rospy.Subscriber("cmd_vel/traffic_signs", Twist, self.__cmd_vel_autonomous_traffic_signs)
        ############ CONSTANTS AND VARIABLES ################
        self.joy_received_flag =False #This flag will tell us when at least one number has been received.
        self.new_received_flag =False #This flag will tell us when at least one number has been received.

        self.joy = Joy()
        #********** INIT NODE **********###
        self.flag = 'manual'
        self.enable_skip = False
        r = rospy.Rate(60) #1Hz
        while not rospy.is_shutdown():

            if self.joy_received_flag: #If the flag is 1, then publish the message
                self.joy_received_flag = False
                self.__calculate_manual_velocity()
                if (self.enable_skip):
                    self.enable_skip = False
                else:
                    self.__define_cmd_vel()
                self.new_received_flag = True
            if self.new_received_flag: #If the flag is 1, then publish the message
                self.new_received_flag = False
                if(self.flag=='manual'):
                    self.robot_velocity = self.manual_velocity
                elif(self.flag=='follow_closest_object'):
                    self.robot_velocity = self.follow_closest_object_velocity
                elif(self.flag=='traffic_signs'):
                    self.robot_velocity = self.traffic_signs_velocity
                print(self.flag,self.robot_velocity)
                self.pub_cmd_vel.publish(self.robot_velocity)
            r.sleep()
    #Suscribers
    def __get_data_joy(self, joy):
        self.joy = joy
        self.joy_received_flag = True
    def __cmd_vel_autonomous_follow_closest_object(self, twist):
        self.new_received_flag = True
        self.follow_closest_object_velocity          = twist   
    def __cmd_vel_autonomous_traffic_signs(self, twist):
        self.new_received_flag = True
        self.traffic_signs_velocity          = twist    
    # calculate velocity
    def __define_cmd_vel(self):
        if (self.joy.buttons[0]):
            self.flag = 'follow_closest_object'
            self.enable_skip = True
            #sleep(5)
        elif (self.joy.buttons[1]):
            self.flag = 'traffic_signs'
            self.enable_skip = True
            #sleep(5)
        else:
            self.flag = 'manual'
            self.enable_skip = False

    def __calculate_manual_velocity(self):
        self.manual_velocity.linear.x = self.joy.axes[1] * self.max_linear_velocity
        self.manual_velocity.angular.z = -self.joy.axes[0] * self.max_angular_velocity
        return
    # shutdown
    def on_shutdown(self):
        self.robot_velocity.linear.x = 0.0
        self.robot_velocity.angular.z = 0.0
        self.pub_cmd_vel.publish(self.robot_velocity)
        pass

if __name__ == "__main__":
    rospy.init_node("control", anonymous=True)
    Control()