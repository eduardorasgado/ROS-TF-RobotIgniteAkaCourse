# ROS-TF-RobotIgniteAkaCourse
A way to apply Frame Coordinates Transformations based. Usinf TF library from Robotic Operating System

Instructions:

Simulation 1:

run this on shell->\
rosrun turtlesim_3d_simple_tf_pkg simple_tf_broadcaster.py\
roslaunch turtle_tf_3d run_turtle_tf_listener.launch\
rosrun rviz rviz

and see the TF debugging

Simulation 2:

iRobot follows coke can or turtle1

run this on shell->\
roslaunch turtlesim_3d_simple_tf_pkg turtle_can_broadcaster.launch\
rosrun turtlesim_3d_simple_tf_pkg turtle2_follower_tf_listener.py\
rosrun rviz rviz

