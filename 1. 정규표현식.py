



# 정규 표현식 Regular Expressions (RegEx, RegExp)
# 줄여서 정규식은 복잡한 문자열을 처리할 때 사용하는 기법이며 파이썬같은 프로그래밍에서 나온 문법이 아니라 문자열을 처리하는 모든 곳에서 사용할 수 있는 일종의 형식언어이다.

# 주민등록번호를 입력받는다
# 전화번호를 입력받는다.
# 이메일을 입력받는다.
# 비밀번호를 입력받는다.

# 문자열을 입력받을 때 if(조건문)으로 모든 경우를 판별하기가 힘들다!

# 정규표현식은 문자 그대로를 뜻하는 리터럴 문자와 메타문자를 종합해서 문자열을 표현하는 방식을 가진다.

# 리터럴 데이터
# 다른 추가적인 기능(메서드 등)이 없는 눈에 보이는 데이터값만 가진 데이터

# 메타 문자
# 문자가 가진 원래의 뜻이 아니라 특별한 의미로 사용되는 문자를 뜻한다.
# 정규표현식에서 다음과 같은 메타문자를 사용한다.

# . ^, $, * + ? {} [] \ | ()


# "문자열"

# [] 문자 클래스 (character class)
# ex) [abc] : 이 자리에 a 또는 b 또는 c가 들어올 수 있다.

# [abc] 기준
# a : a는 []에 속해있으니까 통과
# before : []는 한 글자에 대해서 지정한 문자기때문에 b로 시작해서 통과
# done  : d는 []에 포함되어있지 않아서 X

# [abcdefg...xyzABCD...XYZ]
# - : []에서 두 문자 사이에 -을 사용하면 두 문자 사이의 범위를 뜻하게된다.
# [a-z] == [abcd...xyz]
# [0-9] == [0123456789]

# . (dot)   : \n(개행)을 제외한 임의의 문자를 표현한 메타문자

# ex) a.b

# aab, abb, acb, a+b  ---> .위치에 아무 문자가 와도 통과!
# aaab, arab    --> X


# ^
# 문자열의 시작 문자를 지정하는 메타문자
# ^문자의 형식으로 사용한다.

# ex) ^[a-zA-Z] --> 영어로 시작하는 문자열만 통과!
#     ^a    : a로만 시작하는 문자열만 통과가능

# 단, 문자 클래스[] 안에서 ^을 사용하면 not의 의미를 가지게된다.
# ex) [^0-9]    : 숫자를 제외한 문자아무거나

# $
# 문자열의 마지막 문자를 지정하는 메타문자
# 문자$의 형식으로 사용한다.

# *
# 반복을 의미하는 메타문자
# 문자* 의 형태로 사용하고 문자가 0개부터 무한대까지 반복될 수 있다는 의미를 가진다.

# ex)
# ab*c
# ac, abc, abbc, abbbc, abbbbbbc, .... ---> 통과


# +
# 반복을 의미하는 메타문자
# 문자+ 의 형태로 사용하고 문자가 1개부터 무한대까지 반복될 수 있다는 의미를 가진다.

# ex)
# ab+c
# abc, abbc, abbbc, abbbbbbc, .... ---> 통과

# {}
# 반복을 표현하는 메타문자, 문자의 반복횟수를 지정할 수 있다.

# 1. {n}의 형태로 사용
# 문자{n}의 형태로 사용한다.
# 문자가 n번 반복되어야한다.

# ab{3}c
# abbbc : 통과

# 2. {n,m}의 형태
# 문자{n,m}의 형태로 사용한다.
# 문자가 n번 이상, m번 이하로 반복되어야한다.

# ex) ab{2,4}c
# abbc, abbbc, abbbbc : 통과

# n, m을 생략할 수 있다.
# n을 생략하면 0이 지정되고
# m을 생략하면 무한대가 지정된다.
# {,} == *

# ?
# 문자?의 형태로 사용한다.
# 문자가 0번 또는 1번만 사용되어야 한다는 뜻을 가진다.

# ex) ab?c
# abc, ac


# \
# 메타문자를 리터럴문자처럼 사용하기 위해서 쓰는 메타문자
# ex) \^, \?
print("\"")

# 문자와 조합하여 문자의 조합을 나타낼 수도 있다.
# 알아두면 좋은 특수문자
# \d    : 숫자를 의미하는 문자 == [0-9]
# \D    : 숫자를 제외한 문자를 의미한다. == [^0-9]

# \w    : 알파벳, 숫자, _의 클래스를 뜻하는 문자 == [a-zA-Z0-9_]
# \W    : 알파벳, 숫자, _를 제외한 클래스를 뜻하는 문자 == [^a-zA-Z0-9_]

# \s    : 화이트스페이스 문자를 뜻한다. == [ \t\n\r\f\v]
# \S    : 화이트스페이스를 제외한 문자를 뜻한다. == [^ \t\n\r\f\v]


# |
# or을 표현하는 메타문자
# A | B일 때 문자가 A 또는 B라는 뜻을 가진다.
# [ABC|DEF]

# ()
# 그룹을 만들 수 있는 메타문자


# 전화번호 정규식 표현
# 010 - 숫자3 or 숫자4 - 숫자 4
# "^010-[0-9]{3,4}-\d{4}$"



# 정규표현식 사용

# re 모듈 (regular expressions)
# 파이썬은 정규표현식을 지원하기 위해 re모듈이 기본 라이브러리로 설치되어있다.
import re

# 정규식 객체 생성하기
# compile() 함수
# 변수 = re.compile(정규식)

pattern = re.compile("[abc]")


# 객체가 가지고 있는 match() 메서드
# 입력한 문자열의 처음부터 정규식에 대해 매치(통과)되는지 확인해서 논리데이터(bool)를 반환하는 메서드

print(pattern.match("apple"))
# <re.Match object; span=(0, 1), match='a'>
# 정규식을 통과(매치)하면 match 객체를 반환한다.

print(pattern.match("papple"))
# None
# 정규식을 통과하지 못하면 None 데이터를 반환한다.

if pattern.match("banana"):
    print("match 되는 경우 실행할 코드")
else:
    print("match에 실패한 경우 실행할 코드")

# re.match(정규식, 확인할 문자열)
# 밑에 배울 모든 메서드는 re모듈이 함수로 가지고 있다.
# 단, 정규식을 저장하고 있지않아서 사용할 때 정규식을 추가로 작성해야한다.

# search() 메서드
# 문자열 전체를 확인해서 정규식에 매치되는 부분을 찾는 메서드

print(pattern.search("papplae"))
# <re.Match object; span=(1, 2), match='a'>
# 정규식을 통과하는 부분이 여러 개라도 처음에 찾은 매치데이터만 반환한다.

# findall()
# 정규식에 매치되는 모든 부분을 찾아주는 메서드
# 찾은 문자열(매치되는 부분)은 리스트의 요소로 담겨져 반환된다.

print(pattern.findall("apple is too bad")) # ['a', 'b', 'a']
print(pattern.findall(" ")) # []

# finditer()
# 문자열에서 정규식을 통과하는 모든 매치데이터를 iterable형식으로 반환한다.
print(pattern.finditer("apple is too bad"))
# <callable_iterator object at 0x000002AF3B961BA0>

for i in pattern.finditer("apple is too bad"):
    print(i)
# <re.Match object; span=(0, 1), match='a'>
# <re.Match object; span=(13, 14), match='b'>
# <re.Match object; span=(14, 15), match='a'>


# sub() 메서드
# 문자열 바꾸기 메서드
# sub(바꿔넣을 문자열, 대상 문자열)
# 대상 문자열에서 정규식에 매치되는 부분의 문자열을 바꿔넣을 문자열로 변경하는 메서드


pattern = re.compile("blue|red")
# 문자열에서 blue 또는 red를 찾는다.
print(pattern.sub("color", "red side and blue side"))
# color side and color side

# count 매개변수에 내가 바꿔놓을 문자열의 개수를 지정할 수 있다.
print(pattern.sub("color", "red side and blue side", count=1))
# color side and blue side


# 그룹화, ()
# ABCABCABCABC
# A*B*C* ---> X
# (ABC)* ---> O

pattern = re.compile("(ABC)*")
print(pattern.match("ABCABCABCABC"))
# <re.Match object; span=(0, 12), match='ABCABCABCABC'>

# 그룹화를 사용하는 더 중요한 이유
# 매치된 문자열 중에서 특정 부분의 문자열만 뽑아 낼 수 있다.

# ex)
# 이름 전화번호의 형태로 데이터를 입력받는다.

# pattern = re.compile("\\w{3,4}\\s01[01]-\\d{3,4}-\\d{4}")
pattern = re.compile(r"\w{3,4}\s01[01]-\d{3,4}-\d{4}")
# r"" : row string (원시 문자열)
# 문자열안에서 사용되는 \들을 이스케이프문자가아닌 일반 문자로 취급하는 문자열 --> 특수문자의 뜻이 아닌 리터럴문자로 인식하는 문자열
match_data = pattern.match("park 010-1234-5678")
print(match_data)
#<re.Match object; span=(0, 18), match='park 010-1234-5678'>


pattern = re.compile(r"(\w{3,4})\s(01[01])-(\d{3,4})-(\d{4})")
# 메타문자를 적용시키는 것뿐아니라 데이터를 가져오고 싶은 부분에 그룹화를 한다.
match_data = pattern.match("park 010-1234-5678")
print(match_data)
# <re.Match object; span=(0, 18), match='park 010-1234-5678'>

# group(n) 메서드
# 매치객체에서 사용할 수 있는 메서드
# 매치된 데이터에서 n번째 그룹에 해당하는 데이터를 반환하는 메서드
print(match_data.group(1)) # park
print(match_data.group(2)) # 010
print(match_data.group(3)) # 1234
print(match_data.group(4)) # 5678
print(match_data.group(0)) # park 010-1234-5678
# group(0)은 매치된 부분 전체의 데이터를 가지고 있다.


# 그룹화된 문자열 재참조 하기
# 정규식내에서 그룹이 생성되어있다면 생성된 그룹으로 들어오는 문자열을 참조하여 정규식에 사용할 수 있다.

# pattern = re.compile(r'(\w+) \1') # ---> (\w+) (\w+)와는 다르다!
# # \그룹인덱스
# # 작성한 그룹의 정규식에 매치되는 데잍와 일치하는 데이터일 때 통과되는 참조문
#
# print(pattern.match("korea korea"))
# # <re.Match object; span=(0, 11), match='korea korea'>
# print(pattern.match("korea it"))
# # None
#
# pattern = re.compile(r'(\w+) (\w+)')
# print(pattern.match("korea korea"))
# # <re.Match object; span=(0, 11), match='korea korea'>
# print(pattern.match("korea it"))
# # <re.Match object; span=(0, 8), match='korea it'>


# 그룹명 짓고 사용하기
# 형태
# (?P<그룹명>정규식)

pattern = re.compile(r'(?P<temp>\w+) (?P=temp)')
print(pattern.match("korea korea"))
# <re.Match object; span=(0, 11), match='korea korea'>
print(pattern.match("korea it"))
# None


# ex) sub

data = "123456-9876543"
# 주민등록번호
# "123456-9******"
pattern = re.compile(r"(\d{6})-(\d)(\d{6})")
# pattern = re.compile(r"(\d{6}-\d)(\d{6})")
print(pattern.sub(r"\1-\2******",data))
# 123456-9******
print(pattern.sub(r"\g<1>-\g<2>******",data))
# 123456-9******




# 사용자의 이메일의 일부분(아이디의 첫 5글자)을 마스킹 처리해보자

emails = [
    "user12345@naver.com",
    "johndoe123@gmail.com",
    "helloworld@daum.net"
]

# [출력결과]
# *****2345@naver.com
# *****oe123@gmail.com
# *****world@daum.net

# pattern = re.compile(r'^\w{5}\w+@.+')
pattern = re.compile(r'^[a-zA-Z0-9]{5}(\w+)(@\w+)')

for i in emails:
    print(pattern.sub(r"*****\1\2", i))

# *****2345@naver.com
# *****oe123@gmail.com
# *****world@daum.net


































