import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *
from time import sleep
from random import uniform


def create_pose():
    p = Pose()
    p.position.x = uniform(-5, 5)
    p.position.y = uniform(-5, 5)
    p.position.z = uniform(-5, 5)
    p.orientation.x = uniform(-5, 5)
    p.orientation.y = uniform(-5, 5)
    p.orientation.z = uniform(-5, 5)
    p.orientation.w = uniform(-5, 5)
    return p


def create_twist_stamped():
    t = TwistStamped()
    t.header.stamp = rospy.Time.now()
    t.twist.linear.x = uniform(-1, 1)
    t.twist.linear.y = uniform(-1, 1)
    t.twist.linear.z = uniform(-1, 1)
    t.twist.angular.x = uniform(-1, 1)
    t.twist.angular.y = uniform(-1, 1)
    t.twist.angular.z = uniform(-1, 1)
    return t


def talker():
    publish_pose = rospy.Publisher(
        'ChatterPose', Pose, queue_size=10,
    )
    publish_twist_stamped = rospy.Publisher(
        'ChatterTwistStamped', TwistStamped, queue_size=10,
    )
    rospy.init_node('talker', anonymous=True)

    while not rospy.is_shutdown():
        publish_pose.publish(create_pose())
        publish_twist_stamped.publish(create_twist_stamped())
        sleep(1)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.loginfo("rospy.ROSInterruptException")
        exit(1)
