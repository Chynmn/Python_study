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


# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")        # print와는 달리 write는 자동 줄바꿈이 없다.

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")        # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")        # print는 자동으로 줄바꿈을 하므로
# print(score_file.readline(), end="")        # end="" 를 통해 한 줄씩만 띄도록 할 수 있음
# print(score_file.readline(), end="")
# score_file.close()

# 파일 안의 내용이 몇 줄인지 모를 때
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# list 형태로 저장
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()


# pickle : 프로그램 상에서 사용하고 있는 데이터를 파일 형태로 저장하는 라이브러리
# pickle을 쓰기 위해서는 binary 타입을 정의해주여야 함
# import pickle                                   # encoding 할 필요x
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "골프"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)   # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# with : 파일을 열고, 처리 후, 닫는 과정을 편하게 해주는 라이브러리
# import pickle
# with open("profile.pickle", "rb") as profile_file:  # 파일을 열어 변수에 저장
#     print(pickle.load(profile_file))
# with문을 탈출하면서 자동으로 파일을 닫아주므로 파일을 닫을 필요가 없음

# pickle을 쓰지 않고 일반적인 파일을 with문으로 쓰고 읽기
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# Quiz 7) 당신의 회사에서는 매 주 1회 작성해야 하는 보고서가 있습니다.
"""
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.
"""

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")
