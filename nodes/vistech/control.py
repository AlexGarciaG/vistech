#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from math import pi
import time

#This class will subscribe to the /number topic and display the received number as a string message
class Control():
    def __init__(self):
        ############################## Max velocity ###################################
        self.max_linear_velocity = int(rospy.get_param("~max_linear_velocity", 1.0))
        self.max_angular_velocity = int(rospy.get_param("~max_angular_velocity", pi))
            # Limit number
        self.max_angular_velocity = max(-pi, self.max_angular_velocity)
        self.max_angular_velocity = min(pi, self.max_angular_velocity)
        #################################################################################
        rospy.on_shutdown(self.on_shutdown)
        ############################### Publisher ######################################
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        ############################### SUBSCRIBERS #####################################
        rospy.Subscriber("cmd_vel/manual", Twist, self.__cmd_vel_manual)
        rospy.Subscriber("cmd_vel/autonomous", Twist, self.__cmd_vel_autonomous)
        rospy.Subscriber("enable_autonomous", Empty, self.__enable_autonomous)
        ############ CONSTANTS AND VARIABLES ################
        self.autonomous_flag = 0 #This flag will tell us when at least one number has been received.
        self.cmd_vel = Twist()
        self.autonomous = Twist()
        self.manual = Twist()
        #********** INIT NODE **********###
        r = rospy.Rate(60)
        while not rospy.is_shutdown():
            if self.autonomous_flag:
                self.autonomous_flag = 1
                self.cmd_vel = self.autonomous
            else:
                self.cmd_vel = self.manual
            self.pub.publish(self.cmd_vel)
            r.sleep()
    def __cmd_vel_manual(self, twist):
        self.manual          = twist
        self.autonomous_flag = 0
    def __cmd_vel_autonomous(self, twist):
        self.autonomous          = twist
    def __enable_autonomous(self,data):
        time.sleep(5)
        self.autonomous_flag     = 1
    def on_shutdown(self):
        self.cmd_vel.linear.x = 0.0
        self.cmd_vel.angular.z = 0.0
        self.pub.publish(self.cmd_vel)
        pass

if __name__ == "__main__":
    rospy.init_node("control", anonymous=True)
    Control()