#! /usr/bin/env python
import rospy
import time
import tf
from turtle_tf_3d.get_model_gazebo_pose import GazeboModel

def tf_publisher_function(pose_msg, robot_name):
    br = tf.TransformBroadcaster()
    
    br.sendTransform(
        (pose_msg.position.x, 
        pose_msg.position.y, 
        pose_msg.position.z),
        (pose_msg.orientation.x,
        pose_msg.orientation.y,
        pose_msg.orientation.z,
        pose_msg.orientation.w),
        rospy.Time.now(),
        robot_name,
        "/world"
        )

def tf_publisher():
    rospy.init_node("simple_tf_publisher", anonymous=True)
    robot_name_list = ["turtle1", "turtle2"]
    gazebo_model_object = GazeboModel(robot_name_list)
    
    for robot_name in robot_name_list:
        pose_now = gazebo_model_object.get_model_pose(robot_name)
        
    time.sleep(1)
    rospy.loginfo("Ready... Starting to publish TF data now...")
    
    rate = rospy.Rate(5) #5HZ
    
    while not rospy.is_shutdown():
        
        for robot_name in robot_name_list:
            pose_now = gazebo_model_object.get_model_pose(robot_name)
        
            if not pose_now:
                rospy.logwarn("The pose of robot is not yet available, try it again later...")
            else:
                tf_publisher_function(pose_now, robot_name)
                
            rate.sleep()
            
if __name__=='__main__':
    try:
        tf_publisher()
    except rospy.ROSInterruptException:
        print("An error ocurred")