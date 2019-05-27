#include <ros/ros.h>
#include <stdlib.h>
#include <geometry_msgs/Twist.h>

#define time_start 1000000
#define time_stop 1000000

using namespace std;
int times;
int main(int argc, char** argv)
{
    ros::init(argc, argv, "vel_ctrl");
    ros::NodeHandle n;
    ros::Publisher vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 10);
    times = time_start; 
    while(ros::ok() && times)
    {
        geometry_msgs::Twist vel_cmd;
        vel_cmd.linear.x = 0;
        vel_cmd.linear.y = -0.1;
        vel_cmd.linear.z = 0;
        
        vel_cmd.angular.x = 0;
        vel_cmd.angular.y = 0;
        vel_cmd.angular.z = 0;

        vel_pub.publish(vel_cmd);
         times--;
        ros::spinOnce();
    }
return 0;
}
