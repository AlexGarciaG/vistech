#!/usr/bin/env python3
from cmath import inf
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from math import pi
#This class will subscribe to the /number topic and display the received number as a string message
class Control():
    def __init__(self):
        ############################## Max velocity ###################################
        max_linear_velocity = 1
        max_distance = 12.0
        self.linear_proportional = max_linear_velocity/max_distance
        self.min_distance_to_move = 0.5
        max_angular_velocity = pi
        max_radius = pi
        self.angular_proportional = max_angular_velocity/max_radius
        self.min_radius_to_move = (6*pi)/180.0
        self.robot_velocity = Twist()
        #################################################################################
        rospy.on_shutdown(self.on_shutdown)
        ############################### Publisher ######################################
        self.pub = rospy.Publisher('cmd_vel/autonomous', Twist, queue_size=1)
        ############################### SUBSCRIBERS #####################################
        rospy.Subscriber("/scan", LaserScan, self.__get_data_laser)
        ############ CONSTANTS AND VARIABLES ################
        self.laser_scan_received_flag =0 #This flag will tell us when at least one number has been received.
        self.laser = LaserScan()
        #********** INIT NODE **********###
        r = rospy.Rate(1) #1Hz
        near_object = 0
        angle       = 0
        linear_x    = 0
        angular_z   = 0
        while not rospy.is_shutdown():
            if self.laser_scan_received_flag: #If the flag is 1, then publish the message
                self.laser_scan_received_flag = 0
                near_object, angle = self.__get_closer_object()

                rospy.loginfo("The distance to the closestes object is :"+str(near_object)+"m from the robot at " + str(angle*(180/pi)))
                linear_x = near_object*self.linear_proportional
                angular_z = -angle*self.angular_proportional
            if (-self.min_distance_to_move < near_object < self.min_distance_to_move ):
                linear_x = 0
            if (-self.min_radius_to_move < angle < self.min_radius_to_move ):
                angular_z = 0
            rospy.loginfo("Linear velocity:"+str(linear_x)+" Angular velocity:" + str(angular_z))
            self.robot_velocity.linear.x = linear_x
            self.robot_velocity.angular.z = angular_z
            self.pub.publish(self.robot_velocity)
            r.sleep()
    def __get_closer_object(self):
        near_object = min(self.laser.ranges)
        index = self.laser.ranges.index(near_object)
        angle = self.laser.angle_min+self.laser.angle_increment*index
        if (near_object == inf):
            near_object = 0
            angle = 0
        return near_object,angle
    def __get_data_laser(self, laser):
        self.laser = laser
        self.laser_scan_received_flag = 1
    def on_shutdown(self):
        self.robot_velocity.linear.x = 0.0
        self.robot_velocity.angular.z = 0.0
        self.pub.publish(self.robot_velocity)
        pass

if __name__ == "__main__":
    rospy.init_node("control", anonymous=True)
    Control()