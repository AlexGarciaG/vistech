#include <ros.h>
#include <std_msgs/Int16.h>

/// ROS
ros::NodeHandle nh;
// Left Motor velocity
void left_motor_vel_Callback( const std_msgs::Int16& left_motor_vel){
  send_left_velocity_to_motor(left_motor_vel.data);
}
void right_motor_vel_Callback( const std_msgs::Int16& right_motor_vel){
  send_right_velocity_to_motor(right_motor_vel.data);
}


ros::Subscriber<std_msgs::Int16> sub_left_motor_vel("left_motor_vel", &left_motor_vel_Callback );
ros::Subscriber<std_msgs::Int16> sub_right_motor_vel("right_motor_vel", &right_motor_vel_Callback );

///Motors
int safe = 20;
// Motor 1
int IN1 = 3;
int IN2 = 4;

// Motor 2
int IN3 = 6;
int IN4 = 5;

// Motor 3
int IN5 = 8;
int IN6 = 9;

// Motor 4
int IN7 = 11;
int IN8 = 10;

int mode = 0;

void setup() {
  //Serial.begin(9600); 
  nh.initNode();
  nh.subscribe(sub_left_motor_vel);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(IN5, OUTPUT);
  pinMode(IN6, OUTPUT);
  pinMode(IN7, OUTPUT);
  pinMode(IN8, OUTPUT);
}

void loop() {
  nh.spinOnce();
  delay(1);
}

void send_left_velocity_to_motor(int vel){
  if (vel>0){
    analogWrite(IN1, vel);
    analogWrite(IN3, vel);

  }
  else {
    analogWrite(IN2, vel);
    analogWrite(IN4, vel);
    
  }
}
void send_right_velocity_to_motor(int vel){
  if (vel>0){
    analogWrite(IN5, vel);
    analogWrite(IN7, vel);
  }
  else{
    analogWrite(IN6, vel);
    analogWrite(IN8, vel);
  }
}

