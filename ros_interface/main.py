import rospy
import std_msgs.msg
import geometry_msgs.msg


def print_message(p):
    string = "(%s)" % p.__class__.__name__
    string += " "
    attributes = dir(p)
    attributes = [a for a in attributes if not a.startswith("_") and not a.endswith("_")]
    string += "(" + ",".join(attributes) + ")"
    string += " "
    string += "(" + ",".join([str(getattr(p, a)) for a in attributes]) + ")"
    rospy.loginfo(string)

def pose_callback(data):
    if isinstance(data, geometry_msgs.msg.Pose):    
        rospy.loginfo("Pose sent from %s:" % rospy.get_caller_id())
        print_message(data.position)
        print_message(data.orientation)


def twist_stamped_callback(data):
    if isinstance(data, geometry_msgs.msg.TwistStamped):
        rospy.loginfo("TwistStamped sent from %s:" % rospy.get_caller_id())
        print_message(data.header)
        print_message(data.twist)


def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("ChatterPose", geometry_msgs.msg.Pose, pose_callback)
    rospy.Subscriber("ChatterTwistStamped", geometry_msgs.msg.TwistStamped, twist_stamped_callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
