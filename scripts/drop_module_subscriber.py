import rospy
from std_msgs.msg import String
import serial
import time


# Callback 함수: 토픽 메시지를 받았을 때 실행될 함수
def callback(data):
    rospy.loginfo("Received message: %s", data.data)
    
    # 아두이노로 메시지 전송
    message = data.data
    ser.write(message.encode('utf-8'))
    rospy.loginfo("Sent message to Arduino: %s", message)
    time.sleep(1)  # 1초 동안 대기 (원하는 대기 시간으로 수정)
    #received_data = ser.readline()
    #rospy.loginfo("Received message from Arduino: %s", received_data.decode('utf-8'))


def listener():
    rospy.init_node("arduino_communication")  # 노드 초기화
    rospy.Subscriber("drop_command_type", String, callback)  # 토픽 이름을 수정
    rospy.spin()

if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 9600)  # 아두이노와의 시리얼 통신 설정
    try:
        listener()
    except rospy.ROSInterruptException:
        ser.close()
