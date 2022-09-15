#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Int16
from os import environ 
class joy_control:

    def __init__(self):
        # Max velocity Motors
        self.max_velocity           = 200
        # Min velocity to move
        self.min_velocity_to_move   = 10
            
        # Control buttons
            # Motors
        self.axis_left_motor    =1
        self.axis_right_motor   =4
            # Stop
        self.button_stop_motors = 1
        #ROS
        rospy.init_node('joy_control', anonymous=True)
        # Publishers
        self.pub_left_motor_vel = rospy.Publisher('left_motor_vel', Int16, queue_size=10)
        self.pub_right_motor_vel = rospy.Publisher('right_motor_vel', Int16, queue_size=10)
        # Suscribers
        rospy.Subscriber("/joy", Joy, self.__get_joy_data)
        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
    def __get_joy_data(self,data):
        left    = self.max_velocity * data.axes[self.axis_left_motor]
        right   = self.max_velocity * data.axes[self.axis_right_motor]
        # Stop button
        if (data.buttons[self.button_stop_motors]==1):
            left    = 0
            right   = 0
        # Min velocity
            #Left
        if (-self.min_velocity_to_move <=left<=self.min_velocity_to_move):
            left    = 0
            #Right
        if (-self.min_velocity_to_move <=right<=self.min_velocity_to_move):
            right    = 0
        left    = int(left)
        right   = int(right)
        # Publish Data
        self.pub_left_motor_vel.publish(left)
        self.pub_right_motor_vel.publish(right)



if __name__ == '__main__':
    my_joy = joy_control()