import re
text = "Please call 010-2345-1234"

# group() 기능을 테스트하는 코드, 2개의 그ㅂ 생ㅓ
regex = re.compile('(\d{3})-(\d{4})-(\d{4})')

match_obj = regex.search(text)

print(match_obj.group())

# 1그룹
print(match_obj.group(1))

# 2그룹
print(match_obj.group(2))


txt1 = "Life is too short, you need python."
txt2 = "The best moments of my life"
txt3 = "My Life My Choice."
# 메타문자
# | : or
# [ - ] : 범위 지정
# ^ : 문자열 처음
# $ : 문자열 끝에
# . : 어떤 한개의 문자가 와도 상관없다.
# * : 앞 문자가 몇 번 반복되어도 상관없다.
# ? : 앞 문자를 0~1번 반복돤 패턴에 매치.
# + : 앞 문자가 1회 이상 반복되는 패턴에 매치
print(re.search('Life|life', txt2))  # Life 또는 life
print(re.search('[Ll]ife', txt2))   # [] 문자 선택의 범위를 표현

print(re.search('^Life', txt1))
print(re.search('^Life', txt2))
print(re.search('^Life', txt3))
print(re.search('life$', txt2))

print(re.search('A..A', 'ABA'))
print(re.search('A..A', 'ABBA'))
print(re.search('A..A', 'ABBBA'))

print(re.search('AB*', 'A'))
print(re.search('AB*', 'AA'))
print(re.search('AB*', 'J-HOPE'))
print(re.search('AB*', 'X-MAN'))
print(re.search('AB*', 'CABBA'))
print(re.search('AB*', 'CABBBBBA'))

print(re.search('AB?', 'A'))
print(re.search('AB?', 'AA'))
print(re.search('AB?', 'J-HOPE'))
print(re.search('AB?', 'X-MAN'))
print(re.search('AB?', 'CABBA'))
print(re.search('AB?', 'CABBBBBA'))

txt = "abc@facebook.com와 bbc@google.com에서 이메일이 도착하였습니다."
output = re.findall('\S+@[a-z.]+', txt)
print('추출된 이메일 :', output)
