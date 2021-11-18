#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32MultiArray

def callback(data):
    """ Функция вызываемая при получении сообщения """
    data = data.data

    if len(data) == 0:
        rospy.loginfo("Вещестенных корней нет")
    elif len(data) == 1:
        x1 = "{:.3f}".format(data[0])
        rospy.loginfo("Уравнение имеет один вещественный корень: " + x1)
    else:
        x1 = "{:.3f}".format(data[0])
        x2 = "{:.3f}".format(data[1])
        rospy.loginfo("Уравнение имеет два вещественных корня: " + x1 + " " + x2)


def init_subscriber():
    """ Инициализация подписчика """
    rospy.init_node("topic_subscriber_node")
    rospy.Subscriber("answer", Float32MultiArray, callback)
    rospy.spin()


if __name__ == '__main__':
    init_subscriber()