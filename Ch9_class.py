# # Starcraft
# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(
#         name, location, damage))


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

class Unit:     # 부모 클래스
    def __init__(self, name, hp, speed):   # __init__ : 생성자. 객체가 생성될 때 호출
        self.name = name                    # 멤버 변수 : 클래스 내에서 정의된 변수
        self.hp = hp
        self.speed = speed
        # self.damage = damage
        # print("{0} 유닛이 생성 되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))


# marine1 = Unit("마린", 40, 5)       # self를 제외한 부분을 입력
# marine2 = Unit("마린", 40, 5)       # Unit class의 인스턴스
# tank = Unit("탱크", 150, 35)        # 함수에 정의된 정보를 모두 입력해야 함

# # 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에겐 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)      # 클래스의 생성자를 통해 작성
# # 클래스 외부에서 멤버변수를 통해 사용
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True             # 클래스 외부에서 객체에 추가로 변수를 만들어 쓸 수 있음

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


# 메소드(함수)) - 공격유닛
# 상속  -  공격을 하지 않는 유닛
# 메딕 : 의무병
class AttackUnit(Unit):     # 자식 클래스
    def __init__(self, name, hp, speed, damage):
        # self.name = name
        # self.hp = hp
        Unit.__init__(self, name, hp, speed)   # 상속을 통해 다른 클래스의 변수를 받음
        self.damage = damage

    def attack(self, location):         # 메소드 앞에는 항상 self
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


# 다중 상속
# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)      # 0 -> 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):   # move 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 발키리 : 공중 공격 유닛, 한 번에 14 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6*14, 5)
# valkyrie.fly(valkyrie.name, "3시")


# 메소드 오버라이딩 : 자식 클래스에서 정의한 메소드를 사용하는 것
# 벌처 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력과 공격력이 굉장히 좋음
battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecrusier.fly(battlecrusier.name, "9시")    # 지상인지 공중인지 직접 검토해야하는 귀찮음
# 메소드 오버라이딩을 통해 공중 유닛도 지상 유닛처럼 move 명령어를 통해 이동할 수 있도록 처리
battlecrusier.move("9시")
