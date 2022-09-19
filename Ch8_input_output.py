# 표준 입출력
# sep : seperate -> ','가 들어가는 부분에 원하는 문자열을 넣을 수 있음
# end : 문장의 끝부분을 어떻게 출력할 지 지정할 수 있음

print("Python", "Java", "JavaScript", sep=", ")
print("Python", "Java", "JavaScript", sep=" vs ", end="? ")
print("무엇이 더 재미있을까요?")

# stdout : 표준 출력        stderr : 표준 에러
# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 시험 성적 정렬 출력
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # 8칸 확보 후 왼쪽 정렬(ljust),  4칸 확보 후 오른쪽 정렬(rjust),  ':'로 구분

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
# 3칸 확보 후 값이 없는 부분을 0으로 채움(zfill)

# 사용자 입력을 통해 값을 받으면 항상 문자열 형태로 저장된다.
# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")


# 다양한 출력 포맷
# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되. 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))

# 3자리 마다 ','를 찍어주기
print("{0:,}".format(1000000000000000))

# 3자리 마다 ','를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(1000000000000000))
print("{0:+,}".format(-1000000000000000))

# 3자리 마다 ','를 찍어주기, +- 부호도 붙이기, 자릿수 확보
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
print("{0:^<30,}".format(1000000000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3))
