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
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입ㄴ디ㅏ.".format(balance))
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


# 기본값 설정
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#           .format(name, age, main_lang))        # 한 줄의 코드가 너무 길어질 때 '\'로 다음 줄로 넘겨줄 수 있다.
#
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 반, 같은 수업이라면 나이와 주 사용 언어가 같으므호
def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
          .format(name, age, main_lang))

profile("유재석")
profile("김태호")


