



# 컬렉션

# 변수 : 1개의 데이터를 저장할 수 있는 메모리 공간
a = 10
b = 20
c = 30
# ...
# 데이터의 개수만큼 변수를 생성해야한다.

# 컬렉션   : 데이터들을 한 개의 이름(변수)에 저장할 수 있도록 만들어진 자료형

# 기본 컬렉션 4가지
# list, tuple, set, dict

# list
# 여러 값을 저장할 때 가장 보편적으로 사용되는 컬렉션 형태
# 저장하고자 하는 데이터들의 자료형이 달라도 하나의 리스트에 저장할 수 있다.
# 대괄호 [], 또는 list() 형변환 함수를 이용해서 생성한다.

li = [] # 빈 리스트
li2 = [1, 2, 3] # 정수로만 이루어진 리스트
# 각각의 데이터는 ,를 기준으로 구분한다.
# 컬렉션에서 저장하고 있는 각각의 데이터는 요소라고도 한다.

print(li)   # []
print(li2)  # [1, 2, 3]

li3 = [1, 2, 3, "a", True]
# 아무 자료형의 데이터라도 리스트에 저장할 수 있다.
li4 = [1, 2, 3, "a", True, [4,5,6]]
# 이중 리스트 (리스트의 요소로 리스트데이터를 가지고 있는 것)

print(li3) # [1, 2, 3, 'a', True]
print(li4) # [1, 2, 3, 'a', True, [4, 5, 6]]

# 인덱싱!
# 컬렉션 데이터들도 생성될 때 데이터(요소)별로 인덱스를 가지게 된다.

print(li3[3]) # a
print(li4[5]) # [4, 5, 6]
print(li4[5][1]) # 5
# 이중 리스트안에 존재하는 값에 접근하고자 할 때에는 먼저 요소의
# 리스트를 인덱싱으로 가져온다.
# 그 후 요소 리스트에서 한번 더 인덱싱을 사용하여 원하는 데이터를 가져올 수 있다.

# 슬라이싱
#  list[start:stop:step]

# [1, 2, 3, 'a', True, [4, 5, 6]]
print(li4[0:3]) # [1, 2, 3]
print(li4[:3]) # [1, 2, 3]
print(li4[:]) # [1, 2, 3, 'a', True, [4, 5, 6]]
print(li4[::2]) # [1, 3, True]
print(li4[-1]) # [4, 5, 6]

# 요소의 수정
a = 5
print(a)
a = 10
print(a)
# list에서 인덱싱으로 내가 원하는 데이터 공간을 가져와서 새로운 값을 대입할 수 있다.
print(li4[0]) # 1
li4[0] = 10 # 리스트 li4의 첫 번째 공간(메모리)에 10을 저장할게
print(li4[0]) # 10

li4[0] = "데이터 형태가 다른 데이터로 바꾸어도 상관없다."
print(li4[0]) # 데이터 형태가 다른 데이터로 바꾸어도 상관없다.

# 요소의 추가와 삭제
# 메서드라는 것을 사용하여 요소를 추가하거나 삭제할 수 있다.

# 메서드   : 어떤 데이터가 존재해야만 사용할 수 있는 함수
# ex) 데이터.함수()의 형태로 사용한다.

# 함수    : 혼자 사용할 수 있는 명령어
# ex) print()

# 요소의 추가
# append(), insert() 메서드

# list데이터.append(data)의 형식으로 사용하고, 데이터를 마지막 요소로 추가한다.

# list데이터.insert(index,data)의 형식으로 사용하고, 데이터를 지정한 인덱스 위치에 데이터를 추가한다.
score = [30, 20, 50, 70]
print(score) # [30, 20, 50, 70]
score.append(90)
print(score) # [30, 20, 50, 70, 90]
score.append("문자")
print(score) # [30, 20, 50, 70, 90, '문자']

score.insert(2, 80) # 2번 인덱스에 80을 추가
print(score) # [30, 20, 80, 50, 70, 90, '문자']
# 인덱스 2의 위치에 80이 추가되고, 기존 데이터는 한 칸씩 밀려난다.

# 요소의 삭제
# pop() 메서드
# del() 함수

# pop(index)의 형식으로 사용하고, 전달한 인덱스 위치의 데이터를 삭제한다.
# index를 생략할 수 있는데, 생략 시 마지막 인덱스의 데이터를 삭제한다.
print(score) # [30, 20, 80, 50, 70, 90, '문자']
score.pop()
print(score) # [30, 20, 80, 50, 70, 90]
score.pop(1)
print(score) # [30, 80, 50, 70, 90]

# del() 함수
# 메모리에 저장된 데이터를 삭제하는 함수

del score[0]
print(score) # [80, 50, 70, 90]

del score[0:2]
print(score) # [70, 90]

del score
# print(score) # 변수 자체를 삭제하여 사용할 수 없어진다.
print()


# 튜플 tuple
# 소괄호 ()를 사용하고, tuple() 형변환 함수로 생성할 수 있다.
# 리스트와 마찬가지로 각 요소에 인덱스가 부여되고, 인덱싱, 슬라이싱이 사용가능하다.
# 한 번 생성되면 저장된 데이터의 값을 변경할 수 없는 컬렉션
# 파이썬에서 자동으로 생성해주는 컬렉션은 튜플의 형태를 가진다.

t1 = (1,2,3)
print(t1) # (1, 2, 3)

t2 = 1, 2, 3
# 여러 개의 데이터를 한 개의 변수에 저장하기 위해 컬렉션 데이터로 바꾸어서 데이터를 저장해준다!
print(t2) # (1, 2, 3)
# ---> 기본적으로 자동생성된 컬렉션 데이터는 튜플형태를 가진다!

t3 = (100)
print(t3) # 100

t4 = (100,)
# 데이터 1개로 튜플을 생성하는 경우 값과 ,를 함께 작성하여 컬렉션 데이터라고 알아볼 수 있도록 해야한다.
print(t4) # (100,)

print(t2[1]) # 2
print(t2[:]) # (1, 2, 3)

# t2[0] = 5 # 요소의 수정은 불가능하다, 오류발생!
# print(t2[0])

# (순서가 있는)컬렉션 연산 + *

li = [1,2,3]
li2 = ['a', 'b', 'c']
print(li + li2) # [1, 2, 3, 'a', 'b', 'c']
# 컬렉션데이터끼리 +연산을 진행하면 두 컬렉션의 요소가 하나로 연결된 새로운 컬렉션 데이터를 생성한다.
print("안녕" + "이건 문자열의 연산") # 안녕이건 문자열의 연산

print(li * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# 곱한 횟수만큼 컬렉션의 요소를 반복한 새로운 컬렉션 데이터를 생성한다.
print("*" * 7) # *******


# 세트 set
# 수학의 집합 개념을 자료형으로 구현한 컬렉션 데이터
# 순서(index)를 가지지않는다.
# -----> 인덱싱, 슬라이싱이 불가능하다
#### 중복된 데이터를 저장하지않는다. ####
# 중괄호 {} 또는 set() 형변환 함수를 통해 생성한다.

s = {10, 20, 30}
print(s) # {10, 20, 30}

s2 = {10, 10, 20, 30, 15}
print(s2) # {10, 20, 30, 15}

li = [1,2,2,2,1,5,3,2,6]
print(li) # [1, 2, 2, 2, 1, 5, 3, 2, 6]
s3 = set(li) # li를 set으로 형변환
print(s3) # {1, 2, 3, 5, 6}

# 요소의 추가 및 삭제

# 추가
# add(), update() 메서드를 사용한다.

# add(data)
# 입력한 data를 추가한다
s3.add(4)
print(s3) # {1, 2, 3, 4, 5, 6}
s3.add(4)
print(s3) # {1, 2, 3, 4, 5, 6}
# 이미 존재하는 데이터를 추가해도 값이 추가되지않는다.

# update(컬렉션 데이터)
# 여러 개의 데이터를 한번에 입력할 때 사용, 기본적으로 list를 많이 사용한다.
s3.update([8,9,12,24,4])
print(s3) # {1, 2, 3, 4, 5, 6, 8, 9, 12, 24}

# 요소의 삭제
# remove(data), discard(data) 메서드를 사용한다.
s3.remove(24)
print(s3) # {1, 2, 3, 4, 5, 6, 8, 9, 12}

s3.discard(3)
print(s3) # {1, 2, 4, 5, 6, 8, 9, 12}

# s3.remove(10) # 존재하지않는 데이터를 삭제하려고해서 오류가 발생한다.
# --> 이미 존재하는 데이터를 삭제할 때 사용하는 메서드

s3.discard(10)
print(s3) # {1, 2, 4, 5, 6, 8, 9, 12}
# 없는 data를 삭제하는 동작에도 정상적으로 작동한다.
# set에 data가 존재하지않는다를 보장받고 싶을 때 사용하는 메서드
print()


# dict 딕셔너리 (dictionary) --> map
# 사전처럼 데이터(요소)가 이름(key)와 의미(value)의 한 쌍으로 이루어진 컬렉션
# 인덱스가 존재하지않는다.
# 대신에 key값을 이용해서 인덱싱과 비슷한 결과를 얻을 수 있다.
# list[0] ---> dict[key]
# key값을 알면 그에 대응되는(저장되어있는) value값을 알 수 있는 컬렉션
# 중괄호 {}를 사용하고, dict() 함수로 생성할 수 있다.

# s = {1, 2, 3} ==> set
# dict = {key : value, key2 : value2}

d = {"a" : "apple", 'b' : "banana"}
# :을 기준으로 왼쪽 data가 key값이 되고, 오른쪽 data가 key에 대응되는 value값이 된다.
# key value 한 쌍의 묶음이 1개의 요소로 취급된다.
print(d) # {'a': 'apple', 'b': 'banana'}

# value의 사용(접근)
# 인덱싱을 인덱스 대신 key값을 이용하여 사용한다.
print(d['a']) # apple

# get() 메서드
# get(key, default)의 형식으로 사용하는 메서드, default는 생략이 가능하다.
print(d.get('b')) # banana
# print(d["c"]) # 저장되어있지 않은 key에 대해 접근하면 오류가 발생!
print(d.get('c')) # None
print(d.get('c', 'cat')) # cat
print(d.get('b', 'cat')) # banana
# key 값이 없는 데이터라면 default로 입력한 값을 반환해주는 메서드
# default를 생략했다면 None이 기본적으로 저장된다.
# default를 지정해도 이미 존재하는 key값이라면, key에 대응되는 value값을 가져온다.


# 요소의 추가, 수정 및 삭제

# 요소의 추가 및 수정
# key와 value값을 조합해서 작성을 한다.

d[1] ="first"
# 저장되어있지 않은 key값에 접근하여 value를 입력하면 요소의 추가로 인식한다.
print(d) # {'a': 'apple', 'b': 'banana', 1: 'first'}
d[1] ="second"
print(d) # {'a': 'apple', 'b': 'banana', 1: 'second'}
# 이미 존재하는 데이터에 대해 접근하여 value를 입력하면 값의 수정으로 인식한다.

# setdefault(key, value) 메서드
d.setdefault('c', 'cat')
print(d) # {'a': 'apple', 'b': 'banana', 1: 'second', 'c': 'cat'}
d.setdefault('d')
print(d) # {'a': 'apple', 'b': 'banana', 1: 'second', 'c': 'cat', 'd': None}
# value값을 생략할 수 있는데 생략하면 None값이 입력된다.

d.setdefault('a', '사과')
print(d) # {'a': 'apple', 'b': 'banana', 1: 'second', 'c': 'cat', 'd': None}
# 이미 존재하는 key, value에는 영향을 주지않는 메서드


# update(dict 데이터) 메서드
d.update({'d' : 'delete', 'e' : 'enter'})
print(d) # {'a': 'apple', 'b': 'banana', 1: 'second', 'c': 'cat', 'd': 'delete', 'e': 'enter'}

# 요소의 삭제
# pop(key) 메서드, del 함수
d.pop(1)
print(d) # {'a': 'apple', 'b': 'banana', 'c': 'cat', 'd': 'delete', 'e': 'enter'}

del d['d']
print(d) # {'a': 'apple', 'b': 'banana', 'c': 'cat', 'e': 'enter'}

# clear() 메서드
# d.clear()
# print(d) # {}
# dict의 모든 요소를 삭제하는 메서드

# 딕셔너리의 key값만 얻기
# keys() 메서드
print(d.keys()) # dict_keys(['a', 'b', 'c', 'e'])

# 딕셔너리의 value값만 얻기
# values() 메서드
print(d.values()) # dict_values(['apple', 'banana', 'cat', 'enter'])

# items() 메서드
print(d.items())
# dict_items([('a', 'apple'), ('b', 'banana'), ('c', 'cat'), ('e', 'enter')])
# 각각의 key와 value값을 튜플에 묶어서 모아놓은 컬렉션 데이터를 얻는 메서드




























