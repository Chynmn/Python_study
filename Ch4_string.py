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












