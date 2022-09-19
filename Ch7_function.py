# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


# 전달값과 반환값
def deposit(balance, money):    # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):   # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance


def withdraw_night(balance, money):     # 영업시간외 출금
    commission = 100    # 수수료 100원
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))


# 함수에서 기본값 설정
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#           .format(name, age, main_lang))        # 한 줄의 코드가 너무 길어질 때 '\'로 다음 줄로 넘겨줄 수 있다.
#
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 반, 같은 수업이라면 나이와 주 사용 언어가 같으므호
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
          .format(name, age, main_lang))


profile("유재석")
profile("김태호")


# 키워드 값을 이용한 함수 호출
def profile2(name, age, main_lang):
    print(name, age, main_lang)


profile2(name="유재석", main_lang="파이썬", age="20")
profile2(main_lang="자바", age=25, name="김태호")


# 가변 인자를 이용한 함수 호출
# def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile3(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile3("유재석", 20, "Python", "Java", "C", "C#", "Swift")
