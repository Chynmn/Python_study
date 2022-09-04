# 문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱 : 가져오고 싶은 정보만 잘라서 가져오기
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연도 : " + jumin[0:2])     # 0 부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])    # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])   # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])   # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())   # 소문자 출력 함수
print(python.upper())   # 대문자 출력 함수
print(python[0].isupper())  # 대문자 확인하는 함수
print(len(python))      # 문자열 길이 함수
print(python.replace("Python", "Java"))     # 값 대체 함수

index = python.index("n")   # 문자의 위치를 알려주는 함수
print(index)
index = python.index("n", index + 1)    # 2번째 n을 찾는 함수
print(index)

print(python.find("n"))     # 문자의 위치를 알려주는 함수
print(python.find("Java"))  # 찾는 값이 없으면 -1을 반환
# print(python.index("Java")) # index는 찾는 값이 없으면 프로그램 오류가 뜸

print(python.count("n"))    # 문자가 몇번 사용 됐는지 알려주는 함수

# 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법1
print("나는 %d살 입니다." % 20)
# = print("나는 %s살 입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법2
print("나는 {}살 입니다.".format(25))
print("나는 {}색과 {}색을 좋아해요.".format("검은", "하얀"))
print("나는 {1}색과 {0}색을 좋아해요.".format("검은", "하얀"))    # 순서를 지정하는 방법

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 23, color = "blue"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "blue", age = 23))

# 방법4 (v3.6 이상~)
age = 21
color = "green"
print(f"나는 {age}살이며, {color}색을 좋아해요.")













