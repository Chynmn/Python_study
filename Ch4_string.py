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