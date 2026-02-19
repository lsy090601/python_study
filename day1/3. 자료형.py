

# 자료형
# 프로그래밍할 때 사용되는 숫자, 문자 등 어떤 데이터의 형태를 형식화 해둔 것

# 기본적인 자료형 4가지
# int(정수), float(실수), bool(논리값), str(문자열)

# 다른언어
# char : 문자 데이터 (문자 하나)
# boolean의 줄임말 bool
# String의 줄임말 str


# 정수 자료형 int
print(10) # 10
print(10 + 10) # 20
# print(10 + "10") # 자료형이 다른 데이터의 연산에서 오류 발생!

# 자료형(data) 함수
# data를 자료형의 데이터로 형변환 시켜주는 함수
print(10 + int("10")) # 20

print(int(True))        # 1
print(int(False))       # 0
print(int(3.141592))    # 3
# int는 소수점 아래의 데이터를 저장할 공간이없어서 데이터가 사라진다.

# print(int("123@ㅁㄴㅇ"))
# 변환할 수 없는 데이터를 형변환하면 오류가 발생한다.

# 진수변환
num = 94
print(bin(num)) # 2진수로 변환된 결과를 반환 # 0b1011110
print(oct(num)) # 8진수로 변환된 결과를 반환 # 0o136
print(hex(num)) # 16진수로 변환된 결과를 반환 # 0x5e
# 진수변환된 데이터는 문자열의 데이터다!

# int("진수변환된 데이터", 진수) --> 데이터를 10진수로 변환해준다.
print(int("0b1011110", 2)) # 94
print(int("0o136", 8)) # 94
print(int("0x5e", 16)) # 94

# float (실수)
# 소수점부분이 있는 데이터

# float(data) : data를 float로 형변환해주는 함수
print(float(True)) # 1.0
print(float("3.14")) # 3.14
print(float(1))     # 1.0

# 보통 소수점 8 ~ 12자리정도의 데이터에서까지만 사용한다.
print(0.1 + 0.2) # 0.30000000000000004

# 그 이상의 작은 수나 정밀한 계산이 필요한 경우에는 문자열을 이용한다.
print()

# bool(boolean, 논리 데이터)
# 논리 데이터 : 참(맞다)과 거짓(틀리다)를 뜻하는 True, False
# 파이썬에서는 첫 글자를 대문자로 작성해야한다.
# print(True)
# print(true)

# True      : 값이 있는 모든 경우, 대표값 1
# False     : 값이 없는 모든 경우, 대표값 0
#           ex) "", [](빈 리스트) 등이 포함된다.

# bool(data) : bool형식의 데이터로 변환해주는 함수
print(bool(0)) # False
print(bool(1)) # True
print(bool("")) # False
print(bool(-1)) # True
print(bool(100)) # True
print(bool(" ")) # True

# str(String, 문자열 데이터)
# 기본적으로 '', ""로 묶여져 있는 모든 데이터는 문자열로 취급한다.
# 파이썬에서는 한 글자(문자)거나 여러 글자(문자열) 상관없이 ''와 ""를 사용한다.
# ---> '' 와 "" 구분하지않는다.
data = 'A'
data = "A"

# 문자열 내에서 '와 "를 표현하기가 쉽다.
print("문자열\" 데이터 ") # 문자열" 데이터
print('"문자열" 데이터 ') # 문자열" 데이터
print("it's me") # it's me

# str(data) : data를 문자열로 형변환해주는 함수
print(str(100)) # 100
print(str(True)) # True
print(str(3.14)) # 3.14

# ----------------------------------------
# 문자열   : 문자의 배열
# 문자    : 단일 문자 자료형(char)
# ---> str은 배열의 기능을 가지고있다

# 문자열의 인덱싱(indexing)
# 문자열이 생성되면 데이터는 문자에 자동으로 index(순서)를 매긴다.
s = "hello"
# 인덱싱 : 인덱스를 지정해서 그 인덱스에 위치한 데이터를 가져오는 것
# 형태
# 문자열데이터[인덱스]
print(s)  #hello
print(s[3]) # l
print(s[4]) # o
# 컴퓨터는 숫자를 0부터 시작한다.
# 인덱스도 0부터 시작한다!
# print(s[5]) 범위를 벗어난 인덱스를 가져오려고 하면 오류가 발생한다!











































