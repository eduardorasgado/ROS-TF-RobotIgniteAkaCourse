#! /usr/bin/env python
import rospy
import tf
import math

def main():
    rospy.init_node("my_moving_carrot_tf_broadcaster")
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(5.0)
    turning_speed_rate = 2.0
    while not rospy.is_shutdown():
        t = (rospy.Time.now().to_sec() * math.pi) * turning_speed_rate
        
        #Map to only turn maximun [0,2 * pi]
        rad_var = t % (2*math.pi)
        #(1.0 * math.sin(rad_var), 1.0 * math.cos(rad_var), 0.0),
        quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0, rad_var)
        
        br.sendTransform(
            (1.0, 0.0, 0.0),
            (quaternion[0], quaternion[1], quaternion[2], quaternion[3]),
            rospy.Time.now(),
            "moving_carrot",
            "coke_can"
            )

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print("An error ocurred on moving extra broadcaster")