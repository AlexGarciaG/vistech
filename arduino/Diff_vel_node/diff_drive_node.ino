/* 
 * This nod ewill subscribe to the /smd_vel topic (Twist).
 * It will publish to /wr and /wl (float32).
 * /wr and /wl will be computed following the differential drive mobile robot model
 */

#include <ros.h>
#include <geometry_msgs/Twist.h> // Type of message for the cmd_vel

ros::NodeHandle  nh; //This structure is necessary to work with ROS (init the node, create publishers, subscribers, etc)

void cmd_vel_cb( const geometry_msgs::Twist& vel_msg){
  digitalWrite(13, HIGH-digitalRead(13));;   // blink the led
}

ros::Subscriber<geometry_msgs::Twist> cmd_vel_sub("cmd_vel", &cmd_vel_cb );

void setup()
{ 
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(cmd_vel_sub);
}

void loop()
{  
  nh.spinOnce(); //Very, very, very improtant to execute at least once ever cylce.
  delay(1);
}
