#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import math

from package.srv import MyService, MyServiceResponse
from std_msgs.msg import Float32MultiArray


publisher = rospy.Publisher('answer', Float32MultiArray, queue_size=10)


def solve_quad(a, b, c):
    """ Функция возвращающая корни квадратного уравнения """

    answer = []

    # Линейное уравнение
    if a == 0:
        answer.append(-c / b)
        return answer

    D = b ** 2 - 4 * a * c

    if D > 0:
        answer.append((-b + math.sqrt(D)) / (2 * a))
        answer.append((-b - math.sqrt(D)) / (2 * a))

    elif D == 0:
        answer.append((-b) / (2 * a))

    return answer

def handler(data):
    """ Обработчик сервиса """
    global publisher
    a = data.a
    b = data.b
    c = data.c

    print("Данные полученные сервисом", a, b, c)

    result = solve_quad(a, b, c) # получаем корни уравнений
    result_pub = Float32MultiArray(data = result) # помещаем корни в Float32MultiArray для отправки
    publisher.publish(result_pub) # Публикуем

    return MyServiceResponse(result)


def init_service():
    """ Инициализация сервиса """
    rospy.init_node("my_service")
    service = rospy.Service('myService', MyService, handler)
    rospy.spin()

if __name__ == "__main__":
    init_service()
