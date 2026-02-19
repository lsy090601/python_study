

# 연산자
# 값을 처리하는데 사용되는 기호나 단어


# 1. 산술 연산자
# ex) +-*/
a = 7
b = 2

print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')

#
print(f'{a} % {b} = {a % b}') # 7 % 2 = 1
# % : 나머지 연산자
print(f'{a} // {b} = {a // b}') # 7 // 2 = 3
# // : 몫 연산자 (나눗셈 이후 소수점 아래부분을 내림처리)
print(f'{a} ** {3} = {a ** 3}')
# ** : 제곱연산자

print()

# 대입 연산자 (=)
# =를 이용해서 변수의 값을 변경하는 것을 데이터를 대입한다 라고한다.

# 변수 = data
# 등호 오른쪽의 데이터(값, 수식)을 왼쪽 공간에 대입한다.
num = 10
num = 10 + 2 * 3
print(num) # 16
# data가 식인 경우 식의 계산(연산)을 끝낸 후에 대입을 진행한다.
print()

# 단항 연산자
# 산술연산자 + 대입연산자
# 이미 존재하는 변수에 대해서 추가적인 연산이 필요할 때 사용하는 연산자
num = 5
num = num + 15
print(num)

# 형식
# 변수 산술연산자= 계산할 값
num += 15
print(num)
# = 오른쪽의 데이터 값(수식)의 결과를 등호에 붙은 산술연산을 변수에 실행한다.

num -= 5
print(num)

num /= 2
print(num)

num *= 3
print(num)

num += 10 * 2 + 300 # --> num += 320
print(num)

# 비교 연산자 (관계 연산자)
# 데이터 A와 B의 관계를 연산한다.
# 결과값은 True False (논리 데이터)를 반환한다.
# ------> 부등호, 등호

num = 15
print(f'{num} > 10 : {num > 10}') # 15 > 10 : True
print(f'{num} < 10 : {num < 10}') # 15 < 10 : False

print(f'{num} >= 10 : {num >= 10}') # 15 >= 10 : True
print(f'{num} <= 10 : {num <= 10}') # 15 <= 10 : False
print(f'{10} <= 10 : {10 <= 10}') # 10 <= 10 : True
# 이상 이하를 표시할 때에는 부등호가 등호 앞에 위치한다.

print(f'{num} == 10 : {num == 10}') # 15 == 10 : False
# == : 같음을 확인하는 등호 연산자
print(f'{num} != 10 : {num != 10}') # 15 == 10 : True
# != : 다름을 확인하는 부등호 연산자

# ! --> not 연산자의 기호
print()

# 논리 연산자
# 비교연산자 또는 boolean(논리) 데이터의 값을 연결해 주는 연산자
# 결과값은 논리 데이터 (True, False)로 반환된다.

# and, or, not

# A와 B가 각각 비교연산 또는 boolean값일 때

# A and B   : A 와 B 모두가 True값인 경우에 True을 반환한다.
#               하나라도 False라면 False를 반환한다.

# A or B    : A 와 B 중 하나라도 True라면 True을 반환한다.
#             두 가지 모두 False여야 False를 반환한다.

# not A     : A가 False라면 True로, True라면 False로 변환

a = 15
b = 0
print(f'{a} > 10 and {b} > 0 : { a > 10 and b > 0 }')
# 15 > 10 and 0 > 0 : False
print(f'{a} > 10 or {b} > 0 : { a > 10 or b > 0 }')
# 15 > 10 or 0 > 0 : True

print(f'not {a} : {not a}')
# not 15 : False
# a는 값이 있는 데이터이기 때문에 boolean으로 변환하면 True

print(f'not {b} : {not b}')
# not 0 : True
# 0은 boolean False값의 대표값!

print(f'not {""} : {not ""}')
# not  : True



































































