# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋ")
print("ㅋ"*9)

# boolean 참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
# 애완동물을 소개해 주세요 -> 변수를 사용하지 않아 초코의 이름을 다른 이름으로 바꿀 때 번거로워지기 때문에, 변수에 값을 저장하여 사용
animal = "강아지"
name = "초코"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는", age, "살이며,", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

# Quiz) 변수를 이용하여 다음 문장을 출력하시오
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

# 연산자
print(1+1)  # 2
print(3-2)  # 1
print(5*2)  # 10
print(6/3)  # 2

print(2**3) # 2^3
print(5%3)  # 2
print(10%3) # 1
print(5//3) # 몫 = 1
print(10//3)# 몫 = 3

print(10 > 3)   # True
print(4 >= 7)   # False
print(10 < 6)   # False
print(5 <= 5)   # True

print(3 == 3)   # True
print(4 == 2)   # False
print(3 + 4 == 7)   # True

print(1 != 3)   # True
print(not(1 != 3))  # False

print((3 > 0) and (3 < 5) )   # True
print((3< 0) & (3 < 5))     # True

print((3 > 0) or (3 > 5))   #True
print((3 > 0) | (3 > 5))   #True

print(5 > 4 > 3)    # True
print(5 > 4 > 7)    # False













