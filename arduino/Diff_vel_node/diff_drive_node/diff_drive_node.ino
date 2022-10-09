/* 
 * This nod ewill subscribe to the /smd_vel topic (Twist).
 * It will publish to /wr and /wl (float32).
 * /wr and /wl will be computed following the differential drive mobile robot model
 */

#include <ros.h>
#include <geometry_msgs/Twist.h> // Type of message for the cmd_vel
#include <std_msgs/Float32.h> //Type of messages for /Wl and /Wr topics
 
ros::NodeHandle  nh; //This structure is necessary to work with ROS (init the node, create publishers, subscribers, etc)

void cmd_vel_cb( const geometry_msgs::Twist& vel_msg){
  digitalWrite(13, HIGH-digitalRead(13));;   // blink the led
}

ros::Subscriber<geometry_msgs::Twist> cmd_vel_sub("cmd_vel", &cmd_vel_cb );
std_msgs::Float32 wl_msg, wr_msg;
ros::Publisher wl_pub("wl", &wl_msg);
ros::Publisher wr_pub("wr", &wr_msg);

void setup()
{ 
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(cmd_vel_sub);
  nh.advertise(wl_pub); //Init the publisher to /wl topic
  nh.advertise(wr_pub); //Init the publisher to /wr topic
}

void loop()
{  
  wl_msg.data = 2.0; //Add some value to the /wl message
  wr_msg.data = 3.1; //Add some value to the /wr message
  wl_pub.publish( &wl_msg ); //Publish the message to the /wl topic
  wr_pub.publish( &wr_msg ); //Publish the message to the /wr topic
  nh.spinOnce(); //Very, very, very improtant to execute at least once ever cylce.
  delayMicroseconds(250);
}
