
# 반복문

# 동일한 작업을 반복해서 수행하는 경우에 사용하는 제어문
# while, for문 두 가지가 존재한다.

# while : 몇 번 반복할지 정해져있지않고, 특정 종료조건을 알 때
# for   : 반복하는 횟수가 정해져있거나, 데이터를 순회할 때
# 구현하기 편하다


# while
# 기본 형태

# while 조건문:
#   반복 실행 코드

# 사실상 사용하는 형태
n = 1       # 조건식에 사용할 변수 선언
while n < 5: # 변수가 들어간 조건식
    print(n)
    n += 1 # 조건식에 사용하는 변수의 값을 변화시키는 증감식


# for문
# 기본형태
# for i in iterable:
#   반복실행할 코드

# iterable
# 시퀸스 자료형     : index를 가진 컬렉션
# 비시퀸스 자료형   : index가 없는 컬렉션

for i in "hello":
    print(i)
for i in [1,2,3]:
    print(i)

# range() 함수
# 정수의 범위데이터를 가진 iterable을 만들어주는 함수

# range(시작값, 종료값, 증감값)
print(range(10)) # range(0, 10)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10):
    print(i)

# 비시퀸스 자료형

# set
for i in {"가위", "바위", "보"}:
    print(i)
# 완벽하게 원하는 순서대로 요소를 가져오지 않기때문에
# for문에서 많이 사용하지는 않는다.


# dict
# 기본적으로 key의 요소를 들고와서 for문을 실행한다.
d = {"key" : "value", "key2" : "value2"}

for i in d:
    print(i)


for i in d:
    print(d.get(i))
    print(d[i])

for i in d.items():
    print(i)

# 파이썬 unpacking 기능


for key, value in d.items():
    print(key, value)


# 리스트 내포
li = [i for i in range(10)]
print(li) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

li = []
for i in range(10):
    li.append(i)


li = [i * 3 for i in range(10)]
print(li) # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
li = []
for i in range(10):
    li.append(i * 3)

li = [i * 3 for i in range(10) if i % 2 == 0]
print(li) # [0, 6, 12, 18, 24]

li = []
for i in range(10):
    if i % 2 == 0:
        li.append(i * 3)
print(li) # [0, 6, 12, 18, 24]




















































































