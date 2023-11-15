import rospy
from std_msgs.msg import String

def publish_mode():
    rospy.init_node("drop_module_publisher")  # 노드 초기화
    pub = rospy.Publisher("drop_command_type", String, queue_size=10)  # 토픽 이름과 메시지 유형 설정

    rate = rospy.Rate(1/5)  # 1초에 한 번 메시지를 publish

    while not rospy.is_shutdown():
        message = "mode1_b"
        pub.publish(message)  # "mode2"를 토픽에 publish
        rospy.loginfo("Published message: %s", message)

        # 2초 동안 대기
        rospy.sleep(3.0)

        # "mode1"로 메시지 변경
        message = "mode1_a"
        pub.publish(message)  # "mode1"을 토픽에 publish
        rospy.loginfo("Published message: %s", message)

        rospy.sleep(3.0)
        # "mode1"로 메시지 변경
        message = "mode1_c"
        pub.publish(message)  # "mode1"을 토픽에 publish
        rospy.loginfo("Published message: %s", message)
        
        rospy.sleep(3.0)

        # "mode1"로 메시지 변경
        message = "mode1_d"
        pub.publish(message)  # "mode1"을 토픽에 publish
        rospy.loginfo("Published message: %s", message)

        rospy.sleep(3.0)
        
        rate.sleep()

if __name__ == "__main__":
    try:
        publish_mode()
    except rospy.ROSInterruptException:
        pass
