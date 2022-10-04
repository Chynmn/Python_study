
import turtle
from random import *

# print("HelloWorld")

# -*- coding: utf-8 -*-

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     return a * b / gcd(a, b)
#
# va = int(input("첫번째 정수를 입력하시오: "))
# vb = int(input("두번째 정수를 입력하시오: "))
#
# if vb > va:
#     va, vb = vb, va
#
# gcd_v = gcd(va, vb)
# print("gcd_v= ", gcd_v)
#
# lcm_v = lcm(va, vb)
# print("lcm_v= ", lcm_v)


# import turtle
#
# t = turtle.Turtle()
# t.shape("turtle")
# n = int(input("몇각형을 그리시겠어요?(3-6): "))
#
# for i in range(n):
#     t.forward(100)
#     t.left(360 // n)
#
# turtle.done()


# fahrenheit = float(input("화씨온도: "))
# celsius = (fahrenheit - 32.0) * 5.0 / 9.0
# print("섭씨온도:", celsius)

# from sympy import Symbol, solve
# x = Symbol('x')
# equation = 2 * x - 6
# print(solve(equation))

# num = int(input("정수를 입력하세요 : "))

# if num < 0:
#     print("음수 입니다.")
# else:
#     print("음수가 아닙니다.")

# game_score = int(input("게임 점수를 입력하세요"))

# if game_score >= 10000:
#     print("고수 입니다.")
# else:
#     print("입문자 입니다.")

# num1 = int(input("정수1을 입력하세요 : "))
# num2 = int(input("정수2을 입력하세요 : "))

# if num1 == num2:
#     print("두 값이 일치합니다.")
# else:
#     print("두 값이 일치하지 않습니다.")

# year = int(input("연도를 입력하시오 : "))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(year, "년은 윤년입니다.")
# else:
#     print(year, "년은 윤년이 아닙니다.")


# print("동전 던지기 게임을 시작합니다.")
# coin = random.randrange(2)
# if coin == 0:
#     print("앞면입니다.")
# else:
#     print("뒷면입니다.")
# print("게임이 종료되었습니다.")

# print("주사위 던지기 게임을 시작합니다.")
# dice1 = int(randrange(1, 7))
# dice2 = int(randrange(1, 7))

# Player1 = input("Player1 의 이름 : ")
# Player2 = input("Player2 의 이름 : ")

# print("------ 주사위를 굴립니다 ------")
# print("{0}의 주사위는 {1}".format(Player1, dice1))
# print("{0}의 주사위는 {1}".format(Player2, dice2))

# if dice1 > dice2:
#     print("{0}이 이겼습니다.".format(Player1))
# elif dice2 > dice1:
#     print("{0}이 이겼습니다.".format(Player2))
# elif dice1 == dice2:
#     print("비겼습나다.")


# t = turtle.Turtle()
# t.shape("turtle")

# t.penup()             # 펜을 올려서 그림이 그려지지 않게 한다.
# t.goto(100, 100)      # 거북이를 (100, 100)으로 이동시킨다.
# t.write("거북이가 여기로 오면 양수입니다.")
# t.goto(100, 0)
# t.write("거북이가 여기로 오면 0입니다.")
# t.goto(100, -100)
# t.write("거북이가 여기로 오면 음수입니다.")

# t.goto(0, 0)          # (0, 0) 위치로 거북이를 이동시킨다.
# t.pendown()           # 펜을 내려서 그림이 그려지게 한다.

# s = turtle.textinput("", "숫자를 입력하시오: ")
# n = int(s)

# if n > 0:
#     t.goto(100, 100)
# if n == 0:
#     t.goto(100, 0)
# if n < 0:
#     t.goto(100, -100)

# turtle.done()


# import turtle

# t = turtle.Turtle()
# # 커서의 모양을 거북이로 한다.
# t.shape("turtle")

# # 거북이가 그리는 선의 두께를 3으로 한다.
# t.width(3)
# # 거북이를 3배 확대한다.
# t.shapesize(3, 3)

# # 무한 루프로 진입한다. 이 루프는 Ctrl+C를 입력받아 종료된다.
# while True:
#     command = input("명령을 입력하시오: ")
#     if command == "l":      # 사용자가 "l"을 입력하였으면
#         t.left(90)          # 왼쪽으로 90도 회전
#         t.forward(100)
#     if command == "r":      # 사용자가 "r"을 입력하였으면
#         t.right(90)         # 오른쪽으로 90도 회전
#         t.forward(100)


# x, y = map(float, input('점의 좌표 x, y를 입력하시오 : ').split())
# if x*x + y*y > 5*5:
#     print('원의 외부에 있음')
# else:
#     print('원의 내부에 있음')

# id = "ilovepython"
# s = input("아이디를 입력하시오: ")
# if s == id:
#     print("환영합니다.")
# else:
#     print("아이디를 찾을 수 없습니다.")

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# s = turtle.textinput("", "도형을 입력하시오: ")
# if s == "사각형":
#     s = turtle.textinput("", "가로: ")
#     w = int(s)
#     s = turtle.textinput("", "세로: ")
#     h = int(s)
#     t.forward(w)
#     t.left(90)
#     t.forward(h)
#     t.left(90)
#     t.forward(w)
#     t.left(90)
#     t.forward(h)
# elif s == "삼각형":
#     s = tutle.textinput("", "가로: ")
#     w = int(s)
#     s = turtle.textinput("", "세로: ")
#     h = int(s)
#     t.forward(w)
#     t.left(120)

# turtle.done()


# t = turtle.Turtle()

# t.circle(100)       # 반지름이 100인 원을 그린다.
# t.left(60)          # 60도 만큼 터틀을 왼쪽으로 회전시킨다.
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# turtle.done()


# t = turtle.Turtle()
# t.shape("turtle")

# for i in range(30):
#     length = random.randint(1, 100)
#     t.forward(length)
#     angle = random.randint(-180, 180)
#     t.right(angle)

# turtle.done()


t = turtle.Turtle()
# 거북이의 속도는 0으로 설정하면 최대가 된다.
t.speed(0)
t.width(3)

length = 10	            # 초기 선의 길이는 10으로 한다.
# while 반복문이다. 선의 길이가 500보다 작으면 반복한다.
while length < 500:
    t.forward(length)   # length만큼 전진한다.
    t.right(89)         # 89도 오른쪽으로 회전한다.
    length += 5	        # 선의 길이를 5만큼 증가시킨다.
turtle.done()
