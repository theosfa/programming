import turtle                                                       # Подключение библиотеки turtle
import datetime
import os


from time import sleep                                              # Подключение метода sleep библиотеки time
from math import tan, sqrt, pi, pow, radians                        # Подключение методов для работы с математическими функциями


turtle.screensize(canvwidth=50, canvheight=300, bg="black")         # Установка размеров окна и его задний фон
print(turtle.screensize())                                          # Вывод размеров окна в консоль
t = turtle.Turtle()                                                 # Создание "черепашки" в переменной t

t.hideturtle()                                                      # Спрятать "черепашку"
t.color("white")                                                    # Установить цвет "черепашки" на белый
turtle.title("My Clocks")                                           # Изменение названия окна на "My Clocks"
clockRadius = 200                                                   # Установка радиуса часов на 300

def clock(clockRadius):                                             # Функция рисования часов, передаваемые значаения - радиус часов
    t.pensize(3)                                                    # Установка толщины пера на 3 px
    t.penup()                                                       # Поднятие пера
    t.home()                                                        # Возврат пера в изначальное положение
    t.pendown()                                                     # Опустить перо
    t.dot(10)                                                       # Рисование точки размером 10 px
    t.penup()                                                       # Поднятие пера
    t.goto(0,-clockRadius)                                          # Перемещение пера в казанную точку
    t.pendown()                                                     # Опустить перо
    t.circle(clockRadius)                                           # Рисование круга с заданным радиусом


def decimals():
    pass

def printTimer(clockRadius, hour, minute, seconds):
    t.pensize(2)
    t.penup()
    t.goto(0, -clockRadius-150)
    t.pendown()
    t.write(f"{hour}:{minute}:{seconds}", font=("Verdana", 15, "normal"))

def button(clockRadius):
    t.pensize(2)
    t.penup()
    t.goto(0, -clockRadius-50)
    t.pendown()
    t.goto(100, -clockRadius-50)
    t.goto(100, -clockRadius-100)
    t.goto(-100, -clockRadius-100)
    t.goto(-100, -clockRadius-50)
    t.goto(0, -clockRadius-50)

def buttonTimer(x, y):
    global clockRadius
    global timer
    if x < 100 and x > -100 and y < -clockRadius-50 and y > -clockRadius-100 :
        timer = not timer
    return

def arrow(degree, r, th):                                           # Функция рисование стрелы, передаваеммые значения - градус, длина, толщина стрелки
    t.pensize(th)                                                   # Установка толщину пера на th
    angle = 0
    if degree <= 90:                                                # Если градус <= 90 то
        angle = abs(degree - 90)                                    # Вычитание 90 градусов
    elif degree <= 180:                                             # Если градус <= 180 то
        angle = abs(degree - 180)                                   # Вычитание 180 градусов
    elif degree <= 270:                                             # Если градус <= 270 то
        angle = abs(degree - 180)                                   # Вычитание 270 градусов
    elif degree <= 360:                                             # Если градус <= 360 то
        angle = abs(degree - 180)                                   # Вычитание 360 градусов
    t.penup()                                                       # Поднятие пера
    x = sqrt(pow(r, 2)/(1+pow(tan(radians(angle)), 2)))             # Расчет абсциссы крайней точки стрелки
    y = int(sqrt(pow(r, 2) - pow(x, 2)))                            # Расчет ординаты крайней точки стрелки
    if degree <= 90:                                                # Если градус <= 90 то
        t.goto(int(x), int(y))                                      # Распологаем стрелку в первой четверти
    elif degree <= 180:                                             # Если градус <= 180 то
        t.goto(y, -int(x))                                          # Распологаем стрелку во второй четверти
    elif degree <= 270:                                             # Если градус <= 270 то
        t.goto(-y, -int(x))                                         # Распологаем стрелку в третьей четверти
    elif degree <= 360:                                             # Вычитание 360 градусов
        t.goto(-y, int(x))                                          # Распологаем стрелку в четвертой четверти
    t.pendown()                                                     # Опустить перо
    t.home()                                                        # Возврат пера в изначальное положение

def getPosition(i,j):
    print("(", i, "," ,j,")")
    return

global timer
timer = False
startTimerSeconds = 0
angleArrowTimer = 0
turtle.tracer(0, 0)                                                 # Ускорение анимации по средством вывода всего за раз а не постепенно
while True:                                                         # Бесконечный цикл для работы часов
    time = datetime.datetime.now()
    angleSeconds = time.second*6
    angleMinutes = time.minute*6 + time.second/10
    angleHours = (time.hour-12)*30 + (time.second+time.minute*60)/120
    # print(f"{time.hour}:{time.minute}:{time.second}")
    if timer:
        t.penup()
        t.goto(-20, -clockRadius-85)
        t.pendown()
        t.write("STOP", font=("Verdana", 15, "normal"))
        t.color("red")
        angleArrowTimer += 0.6
        arrow(angleArrowTimer, clockRadius-20, 1)
        t.hideturtle()
        t.color("white")
    else:
        angleArrowTimer = 0
        t.penup()
        t.goto(-20, -clockRadius-85)
        t.pendown()
        t.write("START", font=("Verdana", 15, "normal"))
    t.color("red")
    arrow(angleArrowTimer, clockRadius-20, 1)
    t.hideturtle()
    t.color("white")
    clock(clockRadius)                                              # Вызов функции рисования часов
    button(clockRadius)
    printTimer(clockRadius, timer_hour, timer_minute, timer_seconds)
    arrow(angleSeconds, clockRadius-25, 1)                          # Вызов функции рисования секундной стрелки
    arrow(angleMinutes, clockRadius-75, 3)                          # Вызов функции рисования минутной стрелки
    arrow(angleHours, clockRadius-115, 5)                            # Вызов функции рисования часовой стрелки
    turtle.Screen().onclick(buttonTimer)
    turtle.update()                                                 # Обновление экрана
    sleep(0.1)
    t.clear()                                                       # Очистка экрана


# r = const
# y = tg(degree)*x
# y^2 + x^2 = r^2
# y^2 = (tg(degree)*x)^2
# x^2(1+tg(degree)^2) = r^2
# x = sqrt(r^2/(1+tg(degree)^2))
# y = sqrt(r^2-x^2)
