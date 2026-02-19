

# class 클래스

# 객체를 만들어 내는 도구의 틀 또는 객체의 설계도
# ----> 사용자가 만드는 자료형

# 하나의 클래스를 만들어두면 그 클래스를 통해서 동일한 구조를 가진 여러 개의 객체를 생성할 수 있다.
# 같은 클래스로 만든 객체라 하여도 객체들은 서로 다른 값을 가질 수 있다.

# 예시) 붕어빵 기계

# 객체 (Object)?
# 여러가지 항목(데이터)를 하나에 묶어서 표현한 데이터
# 숫자 (123) 같이 문자 그대로의 뜻만 가진 데이터 : 리터럴 데이터
# 이런 문자 그대로의 뜻만이 아니라 기능(메서드)나 추가적인 데이터를 가진 데이터 ---> 객체

# ex) 객체는 보통 붕어빵에 비유한다.

# 인스턴스 (instance)
# 클래스를 이용해서 생성한 객체를 가르키는 용어

# 붕어빵기계로 생성한 붕어빵
# ---> 붕어빵은 붕어빵기계의 인스턴스이다.

# 거푸집으로 생성한 주석
# 주석은 거푸집의 인스턴스이다.
# 붕어빵은 거푸집의 인스턴스가 아니다!



# 클래스 도입의 필요성 (객체의 필요성)


# 학생들의 정보를 저장하고 사용해야한다.
name = "홍길동"
Kor = 92
Math = 84
Eng = 88

def student_info(name, kor, math, eng):
    print(name, kor, math, eng)

student_info(name, Kor, Math, Eng)

name2 = "홍길동2"
Kor2 = 92
Math2 = 84
Eng2 = 88
student_info(name2, Kor2, Math2, Eng2)

# 1. 학생의 수가 늘어날수록 관리해야하는 변수의 개수가 엄청 늘어나서 관리하기가 힘들다!

# 데이터 하나하나 변수로 하지말고 1명에 대한 컬렉션 데이터로 만들자!

students = [
    {'name' : "홍길동", 'kor' : 92, 'math' : 78, 'eng' : 86},
    {'name' : "홍길동", 'kor' : 92, 'math' : 78, 'eng' : 86},
    {'name' : "홍길동", 'kor' : 92, 'math' : 78, 'eng' : 86},
]


for student in students:
    score_sum = student["kor"] + student["math"] + student["eng"]
    score_avg = score_sum / (len(student) - 1)
    print(f'{student["name"]}의 점수 합계 : {score_sum}, 평균 : {score_avg:.2f}')

def create_student(name, kor, math, eng):
    return  {'name' : name, 'kor' : kor, 'math' : math, 'eng' : eng}

students = [
    create_student("홍길동", 92, 78, 86),
    create_student("홍길동", 92, 78, 86),
    create_student("홍길동", 92, 78, 86)
]
# 데이터 입력할 때 key값 신경쓰지않고 value만 신경쓰면되네

def student_get_sum(student):
    return student["kor"] + student["math"] + student["eng"]

def student_get_avg(student):
    return student_get_sum(student) / (len(student) - 1)

def student_to_string(student):
    return f'{student["name"]}의 점수 합계 : {student_get_sum(student)}, 평균 : {student_get_avg(student):.2f}'


for student in students:
    print(student_to_string(student))


# 지금까지 만들었던 함수들 다 사용하려면 다 student라는 데이터를 사용하게되네?
# 우리가 만드는 student 데이터랑 함수들을 묶어서 관리하자

# 데이터와 함수 등을 묶은 데이터는 객체라는 이름으로 만들자
# 객체의 설계도(형태) --> 클래스
# 클래스가 가지고 있는 함수 ---> 메서드


# 클래스의 정의(선언, 생성)
# class 키워드를 사용해서 클래스를 선언할 수 있다.

# 기본 형태
# class 클래스이름:
#       클래스가 가지고 있는 데이터 코드

class Temp:
    pass

# 클래스 객체 생성
# 클래스를 정의하였다면 다음과 같은 형식으로 객체를 생성할 수 있다.
# 변수 = 클래스명()

temp = Temp() # Temp클래스를 이용한 객체를 생성해서 temp에 저장!
print(temp) # <__main__.Temp object at 0x000001C008576F90>

temp2 = Temp() # # Temp클래스를 이용한 객체를 생성해서 temp2에 저장!
print(temp2) # <__main__.Temp object at 0x00000231BFD64E10>
# 생성할 때 마다 새로운 객체가 생성된다!


# 클래스 이름
# 프로그래밍에서 보통 변수나 이름을 정할 때 snake_case를 사용하고
# 클래스명 같은 경우에는 보통 pascal_case를 사용한다.

## 많이 사용하는 이름짓기(단어구분) 규칙 3가지 ##

# 1. snake Case
# 각 단어를 연결할 때 _(언더바)를 사용해서 연결하는 방식
# ex) snake_case, SNAKE_CASE

# 2. pascal Case (Upper camel Case)
# 각 단어의 시작을 대문자로 표현하는 방식
# ex) PascalCase

# 3. camel Case (lower camel Case)
# 첫 글자를 제외한 각 단어의 첫 글자를 대문자로 표현하는 방식
# ex) camelCase

# 정리
# 클래스 : 객체를 만들기 위한 템플릿
# 객체   : 클래스에 기반을 두고 있으며, 여러가지 데이터가 조합되어있는 데이터
# 인스턴스 : 클래스로부터 생성된 구체적인 사례(실체, 객체)를 가르킨다.

# 클래스를 기반으로 데이터를 담은 객체를 생성하는 과정을 "인스턴스화"라고한다.












































































