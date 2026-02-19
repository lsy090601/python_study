

# 메서드
# 특정 객체(데이터)가 가지고 있는 함수를 의미한다.

# 함수와 달리 특정 객체가 가지고 있는 함수이기 때문에 호출(사용)하려면 특정 객체(데이터)가 필요하다.

# append()              # 오류!
# list_data.append()    # O

# 문자열 메서드
# --> 문자열이 가지고 있는 함수!
# ex) format()


# count(찾을 문자열)
# 문자열 내부에서 찾는 문자열의 개수를 반환해주는 메서드

s = '내가 그린 기린 그림은 목 긴 기린 그림이고...'
print(s.count("기린"))# 2

# 인덱스를 지정해서 내가 찾을 범위를 지정할 수 있다.
# count(찾을 문자열, 시작인덱스, 종료인덱스)
# 시작 인덱스는 생략 시 0이 지정
# 종료 인덱스는 생략 시 문자열의 끝까지지정된다.

print(s.count("기린", 10)) # 1

# @ find(찾을 문자열) 메서드
# 내가 찾는 문자열의 위치(index)를 반환해주는 메서드
print(s.find('기린')) #  6
# 찾는 문자열이 여러 개 존재한다면 가장 먼저 나오는 문자열의 index를 반환한다.
# 문자열의 시작 인덱스만 반환해준다.

print(s.find('a')) # -1
# 문자열 내에 찾는 문자열이 없으면 -1을 반환한다.

# count와 마찬가지로 찾는 index범위를 지정할 수 있다.
# find(찾을 문자열, 시작인덱스, 종료인덱스)

# 3. 대소문자 변환 메서드
# upper()       : 모든 영문자를 대문자로 변환
# lower()       : 모든 영문자를 소문자로 변환
# capitalize()  : 첫 글자를 대문자로 나머지는 소문자로 변환
s = 'PYthon'

print(s.upper()) # PYTHON
print(s.lower()) # python
print(s.capitalize()) # Python


# @ str.join(iterable) 메서드
# 전달한 iterable의 각 요소 사이에 str을 추가해서 새로운 문자열을 생성하여 반환하는 메서드

print('-'.join('python')) # p-y-t-h-o-n
print('+'.join(['a','b','c','d'])) # a+b+c+d
print(''.join(['a','b','c','d'])) # abcd
# 딕셔너리같은 경우에는 key값만 가져와서 연결한다.
print()


# @ split(구분자) 메서드
# 하나의 문자열을 전달한 구분자를 기준으로 여러 개의 문자열로 분리하여 요소로 저장한 리스트를 반환해주는 메서드

s = "Study is too hard"
print(s.split()) # ['Study', 'is', 'too', 'hard']
# 구분자를 생략하면 기본적으로 공백(space)가 기본값으로 지정된다.

s = '010-1234-5678'
print(s.split('-')) # ['010', '1234', '5678']

# @  replace() 메서드
# 문자열의 일부 문자열을 다른 문자열로 바꿔서 반환해주는 메서드
# replace(바꾸고 싶은 문자열, 바꿔 넣을 문자열)

s = 'hello world'
print(s.replace('hello', 'goodbye')) # goodbye world


s = 'hello hello world'
print(s.replace('hello', 'goodbye')) # goodbye goodbye world
# 바꾸고 싶은 문자열의 개수 상관없이 모두 바뀌어버린다.

s = '010-1234-5678'
print(s.replace('-','')) # 01012345678
# 필요없는 문자열을 삭제할때에도 사용가능하다.

# strip(문자열) 메서드
# 문자열의 양 끝에 있는 불필요한 문자를 제거하는 메서드

s = '                data'
print(s)
print(s.strip()) # data
# 문자열을 전달하지않으면 기본값으로 공백이 지정되어있다.

s = '<<<<<<<<<<<<data<<<<<<<'
print(s)
print(s.strip('<'))

s = '<<<<<<<<<>><<<data<<<>><<<<'
print(s.strip('<')) # >><<<data<<<>>
# 지정한 문자가 나오지않을 때 까지 삭제하는 메서드!

# lstrip    : 왼쪽 부분에 대해서만 strip
# rstrip    : 오른쪽 부분에 대해서만 strip
s = '<<<<<<data<<<<<'
print(s.lstrip("<")) # data<<<<<
print(s.rstrip("<")) # <<<<<<data



















































