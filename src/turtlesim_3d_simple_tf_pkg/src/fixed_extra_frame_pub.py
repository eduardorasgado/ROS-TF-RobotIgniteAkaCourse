#! /usr/bin/env python

import rospy
import tf

def main():
    rospy.init_node('my_fixed_carrot_tf_broadcaster1')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(3.0)
    
    while not rospy.is_shutdown():
        br.sendTransform(
            (1.0, 0.0, 3.0),
            (0.0, 0.0, 0.0, 1.0),
            rospy.Time.now(),
            "fixed_carrot",
            "turtle2"
            )
        
        rate.sleep()

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print("AN error ocurred")
        