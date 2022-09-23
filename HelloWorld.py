from random import *
print("HelloWorld")

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

print("주사위 던지기 게임을 시작합니다.")
dice1 = int(randrange(1, 7))
dice2 = int(randrange(1, 7))

Player1 = input("Player1 의 이름 : ")
Player2 = input("Player2 의 이름 : ")

print("------ 주사위를 굴립니다 ------")
print("{0}의 주사위는 {1}".format(Player1, dice1))
print("{0}의 주사위는 {1}".format(Player2, dice2))

if dice1 > dice2:
    print("{0}이 이겼습니다.".format(Player1))
elif dice2 > dice1:
    print("{0}이 이겼습니다.".format(Player2))
elif dice1 == dice2:
    print("비겼습나다.")
