# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway= ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정유장에서 다음 칸에 탐
subway.append("하하")
print("subway")

# 정형돈씨를 유재석씨와 조세호 사기에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)
#
# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함꼐 사용 가능
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)


# 사전 Dictionary -> key(중복x), value
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
# print(cabinet[5]) -> 없는 키는 프로그램 오류 발생

print(cabinet.get(3))
print(cabinet.get(5))   # 없는 키는 None을 반환
print(cabinet.get(5, "사용 가능"))  # 값이 없을 때 값을 주는 방법

print(3 in cabinet)     # True  -> key가 있는지 없는지를 확인
print(5 in cabinet)     # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}  # 문자열 key도 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새로운 손님(key 생성 및 업데이트)
print(cabinet)
cabinet["C-20"] = "조세호"     # key가 없다면 새로 생성, 원래 있는 key는 값을 update
cabinet["A-3"]  = "김종국"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 모두 출력
print(cabinet.keys())

# value 모두 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)






