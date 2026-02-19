

# for문

# 값의 범위나 반복하는 횟수가 정해져있을 때
# 특정 데이터를 순회할 때 (컬렉션 데이터의 모든 요소를 확인(접근)할 때)
# 사용하면 편리한 반복문

# 파이썬에서 for문은 java의 foreach문의 동작 방식을 가진다.

# 기본 형태
# for i(for문에서 사용할 변수명) in iterable(반복 가능 객체):
#   반복할 코드 작성

# ex)
for i in [1,2,3]:
    print(i)
# 1
# 2
# 3

# 동작 순서
# 1. 프로그램이 for문에 도착한다.
# 2. iterable에 남은 요소가 있는지 확인
# 3. 요소가 남았다면, iterable에서 요소를 하나 가져와서 변수(i)에 대입한다
# 4. 그 후에 반복 코드를 실행한다.
# 5. 2번으로 이동한다.

# for문은 기본적으로 iterable의 요소의 개수만큼 반복문을 실행한다.
# 이 때 요소를 가져오는 순서는 기본적으로 index를 따른다.


# 1 ~ 10 출력
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

print(i) # 10
# for문을 실행하면서 변수를 생성하였기 때문에
# for문이 종료되어도 변수를 사용할 수 있다.
# 이 때 변수의 값은 for문의 마지막 실행 때 사용된 요소가 들어있다.

for _ in [1,2,3,4,5,6,7,8,9,10]:
    print("hello")
# 변수가 필요없다면 변수 선언위치에 _를 사용하여 변수 생성없이 사용할 수 있다.

for num in [1,2,3,4,5,6,7,8,9,10]:
    print(num)
# 변수명은 자유롭게 설정할 수 있다.


# 반복 가능객체 (iterable)
# 1. 시퀸스 자료형 : 순서(index)가 있는 컬렉션
# 문자열, 리스트, 튜플, range()... 등

# 2. 비시퀸스 자료형 : 순서(index)가 없는 컬렉션
# 세트, 딕셔너리... 등


# 시퀸스 자료형

# 1. 문자열
for ch in "안녕하세요":
    print(ch)

# 문자열은 문자 하나하나가 요소 1개로 취급된다.
# --> 반복하는 횟수는 문자열의 길이가된다.


# 2. 리스트
for i in [1,2,3]:
    print(i)

# 3. 튜플
for i in (1,2,3):
    print(i)

# for문으로 1 ~ 100 출력

# for i in [1,2,3,4,5,....100]


# 4. range() 함수
# for문 단짝 함수
# 정수의 범위를 만들어주는 함수
# 결과값은 iterable 데이터로 반환한다.

# 기본형태
# range(초기값, 종료값, 증감값)
# ---> 슬라이싱과 사용방법이 동일하다.

print(range(10))# range(0, 10)
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. 초기값부터 종료값 - 1의 숫자들로 컬렉션 데이터를 만들어주는 함수
#      (초기값 <= n < 종료값)
# 2. 초기값을 생략하면 0이 지정된다.
# 3. 종료값을 생략할 수 없다.
# 4. 증감값을 생략하면 1이 지정된다.

# print(list(range(0,10,2))) # [0, 2, 4, 6, 8]
#
# # 1 ~ 100 출력
# for i in range(1, 101):
#     print(i)
#
# # 10번 반복 하고싶다.
# for _ in range(10): # range(0, 10)--> [0,1,2,3,4,5,6,7,8,9]
#     print("hello")

# for i in range(5, 0, -1):
#     print(i)
#
# for i in range(5, 0, 1): # 실행 X
#     print(i)

# 비 시퀸스 자료형

# 1. set
# for i in {1,2,3}:
#     print(i)


for i in {'가위', '바위', "보"}:
    print(i)
# 요소의 개수만큼 반복을 진행한다.
# 문자열요소일 때 가져오는 요소의 순서가 바뀐다.


# 딕셔너리 dict
# key와 value가 1개의 요소로 묶여있는 컬렉션
person = {'name' : "홍길동", 'age' : 25, 'addr' : '대구 중구'}
for i in person:
    print(i)
# name
# age
# addr

# dict는 요소 전체가 아닌 key값만 가져와서 반복문을 진행한다.

# for key in person:
#     print(person[key])
#     print(person.get(key))
# 가져온 key값을 이용해서 value에 접근한다.
print()

for value in person.values():
    print(value)
# 홍길동
# 25
# 대구 중구

for item in person.items():
    print(item)
    print(item[0]) # key값
    print(item[1]) # value 값
# ('name', '홍길동')
# ('age', 25)
# ('addr', '대구 중구')


# 심화

# 1. 파이썬의 unpacking 기능
li = [1,2,3,4]
# li의 요소를 각각의 변수에 나누어 저장하고 싶다.

data1 = li[0]
data2 = li[1]
print(data1, data2)

data1, data2, data3, data4 = li
print(data1, data2, data3, data4) # 1 2 3 4
# 컬렉션 데이터를 사용할 때 변수의 개수를 요소 개수에 맞추어서 대입하면
# 각각의 요소가 index 순서에 맞게 자동으로 변수에 대입되는 것

# data1, data2, data3 = li # 요소의 개수와 변수의 개수가 다르면 오류!

for key, value in person.items():
    print(key, value)

# name 홍길동
# age 25
# addr 대구 중구

# for문에서 가져오는 요소가 컬렉션 데이터라면
# 변수 선언 시 unpacking 기능을 사용할 수 있다.

# 심화 2번
# 이런게 있다 정도

# 리스트 내포
# --> 컬렉션 데이터를 생성할 때 for문을 사용할 수 있다.

# 기본형식
# li = [표현식 for 변수(i) in iterable]

# ex)
li = [i for i in range(1,11)]
print(li) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

li = [i + 3 for i in range(1,11)]
print(li) # [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# for문을 진행하면서 가져온 요소 i값에 대해 표현식의 결과들을 컬렉션에 저장하는 기능

li = [1 for _ in range(10)]
print(li) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

li = [i * 3 for i in range(1,11)]
print(li) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# if문 추가 작성
li = [i * 3 for i in range(1,11) if i % 2 == 0]
# for문을 실행하는데 if문에 적합한(True)인 데이터 i에 대해서만 표현식을 거처 컬렉션에 저장할게!
print(li) # [6, 12, 18, 24, 30]





















