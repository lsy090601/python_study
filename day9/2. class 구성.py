


# 클래스의 구성
# 객체를 만들어내는 클래스는 객체가 가져야할 데이터와 기능을 가지고있다.

# ex) 사람
# 데이터   : 이름, 나이, 연락처...
# 기능    : 말하기, 밥먹기, 잠자기, 공부...

# 프로그래밍
# 데이터(값) ---> 변수를 사용해서 저장
# 기능    ----> 메서드(함수)를 이용해서 구현

# --> 클래스는 간단하게 보면 변수와 함수로 구성되어있는 집합체!
'''
클래스를 구성하는 변수는 속성 또는 멤버변수라고 말하며,
1) 모든 인스턴스들이 개별적으로 가지는 변수인 인스턴스 변수와
2) 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수인 클래스변수
로 구분이 된다.

클래스를 구성하는 함수는 메서드(method)라고 하며,
1) 인스턴스(instance) 메서드
2) 클래스(class) 메서드
3) 정적(static) 메서드
로 분류된다.
'''


# 인스턴스 변수와 인스턴스 메서드

# 인스턴스 변수
# 클래스를 기반으로 생성된 모든 인스턴스들이 각각 따로 값을 저장하는 변수
# 모든 인스턴스 변수는 self라는 키워드를 앞에 붙여서 클래스 내에서 사용한다.

# 인스턴스 메서드
# 인스턴스 변수(self)를 사용하는 메서드
# 인스턴스 메서드는 반드시 첫 번째 매개변수로 self를 선언해야한다.

# self
# class 내부에서 사용할 수 있는 키워드
# 인스턴스 메서드에서 사용할 수 있다.
# 해당 메서드를 호출하는 인스턴스를 가르키는 대명사


class Person:
    # 메서드 -> 클래스가 가진 함수
    def who_am_i(self, name, age):
        # self를 매개변수로 가진 메서드 --> 인스턴스 메서드

        self.name = name
        self.age = age
        # 인스턴스 변수 생성!

person = Person() # 인스턴스 person 생성
person.who_am_i("홍길동", 25)
# 인스턴스 메서드 who_am_i 사용

# self의 특징
# 매개변수로는 존재하지만
# 실제 사용할 때에는 인수값을 전달하지않는다.

print(person.name) # 홍길동
print(person.age) # 25
# 인스턴스.변수명으로 인스턴스 변수에 접근할 수 있다.

person.age = 27
print(person.age) # 27

person.data = 100
# 인스턴스 변수는 언제나 임의로 생성할 수 있다.
print(person.data) # 100

person2 = Person()
# print(person2.name)
# print(person2.age)
# print(person2.data)
# 인스턴스 변수가 생성(선언)되지않았다고 오류가 발생한다.
# 같은 클래스로 생성한 인스턴스라도 같은 인스턴스 변수를 가지지않는다.

# data = 10
# 파이썬에서 변수를 생성하는 시점은 데이터를 대입하는 시점이다!!
# ---> 인스턴스 변수가 객체(인스턴스)에 생성되는 시점은 인스턴스 변수에 값이 대입(초기화)되는 시점이다.

person2.who_am_i("홍길동2", 20)
print(person2.name) # 홍길동2
print(person2.age)  # 20


class Student:
    def create_student(self,name, kor, math, eng):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng

    def student_get_sum(self):
        return self.kor + self.math + self.eng

    def student_get_avg(self):
        return self.student_get_sum() / 3

    def student_to_string(self):
        return f'{self.name}의 점수 합계 : {self.student_get_sum()}, 평균 : {self.student_get_avg():.2f}'


student = Student()
student.create_student("홍길동", 92, 78, 86)
print(student.student_to_string())
student = Student()
student2 = Student()
student3 = Student()
student2.create_student("홍길동", 92, 78, 86)
student2.create_student("홍길동", 92, 78, 86)

students = [
    student,
    student2,
    student3
]














































































































