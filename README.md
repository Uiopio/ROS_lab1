# ROS_lab1
# Лабораторная работа 1
## Описание
Вариант №2. Вполнил Самарин Алексей.

Работа выполнена в **ubuntu 20.04**

## Запуск
Действия описанные ниже выполняются для созданного рабочего пространства.

* Копируем папку **package** в папку src рабочего пространства.
* Выполняем `catkin_make` в терминале в рабочем пространстве.
* Запускаем ядро роса: `roscore`
* Запускаем сервис: `rosrun package my_servise.py`
* Запускаем подписчика: `rosrun package topic_subscriber.py`
* Обращение к сервису: `rosservice call /myService "a: 0.0 b: 1.0 c: 1.0"`

