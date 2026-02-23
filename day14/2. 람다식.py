


# 람다식, 람다(lambda)
# 람다 함수는 함수형 프로그래밍에서 중요한 개념으로 익면 함수(anonymous function)이라고도 부른다.
# 일반적으로 함수를 한 번만 사용하거나 함수를 인수로 전달해야하는 경우에 유용하게 사용된다.

def my_sum(x, y):
    return x + y

print(my_sum(10, 20)) # 30

# 형식
# lambda argument: expression
# lambda 매개변수: 표현식(return 문)

print((lambda x, y: x + y)(10, 30)) # 40
print(my_sum)
# <function my_sum at 0x0000029D7FB51440>
lambda_obj = (lambda x, y: x + y)
print(lambda_obj)
# <function <lambda> at 0x000001DCE27F3BA0>
# 두 객체 모두 함수 객체 취급이 된다
print(lambda_obj(20,80)) # 100

# 함수를 간단하게 만들고, 코드의 가독성을 높일 수 있는 방식

def temp(func):
    print(func)
    print(func(10, 20))
temp(lambda x, y: x + y)
# <function my_sum at 0x0000017C29E01440>
# 30

# 간단한 함수 정의하기 싫어서 함수 1회용으로 사용하는 것

# 람다식을 사용하기 좋은 함수들이 존재
# --> 함수를 인수로 받아서 사용하는 형식

# map(함수, iterable)
# iterable의 요소들 각각에 함수를 적용시킨 결과를 iterable데이터로 반환하는 함수

li = range(5) # 0 ~ 4
# 각각의 요소에 + 3하고 싶다.
result = []
for i in li:
    result.append(i+3)
print(result) # [3, 4, 5, 6, 7]
li = list(li)
for idx, data in enumerate(li):
    li[idx] = data + 3
print(li) # [3, 4, 5, 6, 7]

new_result = map(lambda x: x + 3,range(5))
print(list(new_result)) # [3, 4, 5, 6, 7]

# map에서 사용하는 함수는 각 요소에 적용되는 함수이기 때문에 보통 매개변수가 1개인 함수


# filter (함수, iterable)
# iterable의 각 요소에서 조건(람다식)에 맞는 요소만을 추출해서 iterable데이터로 반환하는 함수
# 함수는 각 요소에 적용되는 함수이기 때문에서 매개변수는 1개를 사용하고 return(표현식)이 논리값으로 표현이 가능해야한다.

li = filter(lambda x : x % 2,range(10))
print(list(li)) # [1, 3, 5, 7, 9]

li = filter(lambda x : x % 2 == 0,range(10))
print(list(li)) # [0, 2, 4, 6, 8]


# sorted(iterable)
# iterable 데이터를 오름차순으로 정렬하는 함수
li = ["apple",  "good", "banana"]
print(sorted(li)) # ['apple', 'banana', 'good']

# 매개변수 key
# 어떤 데이터값을 기준으로 정렬할 것인지 정하는 매개변수 함수를 입력받는다.
print(sorted(li, key=lambda x: len(x)))
# ['good', 'apple', 'banana']

def temp(x):
    return len(x)
print(sorted(li, key=temp))
# ['good', 'apple', 'banana']


# functools 내장모듈
# 함수를 인수로 쓰는 함수들이 모여있는 모듈
from functools import reduce

# reduce(함수, iterable)
# iterable의 모든 요소에 대해 누적된 연산을 진행할 때 사용하는 함수
# 각각의 요소를지나면서 누적되는 계산결과를 담아 반환하는 함수

# 함수는 매개변수를 2개 받아서 작성한다.
# 요소데이터, 누적데이터

# 팩토리얼
result = reduce(lambda x, y : x * y, range(1,7))
print(result) # 720 == 6!

# 최대값
result = reduce(lambda x, y: x if x > y else y , range(1,11))
print(result) # 10




# 주어진 리스트에서 람다식을 이용하여 문자열의 길이가 3이상인 문자열만 추출해보자

word_list = ["사과", "고양이", "개", "비둘기", "사자", "물고기"]

# [출력 결과]
# ['고양이', '비둘기', '물고기']


result = filter(lambda x: len(x) >= 3, word_list)
print(list(result)) # ['고양이', '비둘기', '물고기']

def check_len(x):
    return len(x) > 2
result = filter(check_len, word_list)














































































































