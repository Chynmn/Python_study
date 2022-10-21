# -*- coding: utf-8 -*-

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

va = int(input("첫번째 정수를 입력하시오: "))
vb = int(input("두번째 정수를 입력하시오: "))

if vb > va:
    va, vb = vb, va

gcd_v = gcd(va, vb)
print("gcd_v= ", gcd_v)

lcm_v = lcm(va, vb)
print("lcm_v= ", lcm_v)