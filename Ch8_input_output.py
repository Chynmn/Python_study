# sep : seperate -> ','가 들어가는 부분에 원하는 문자열을 넣을 수 있음
# end : 문장의 끝부분을 어떻게 출력할 지 지정할 수 있음

print("Python", "Java", "JavaScript", sep=", ")
print("Python", "Java", "JavaScript", sep=" vs ", end="? ")
print("무엇이 더 재미있을까요?")

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

answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")
