
# Coffee 클래스
# 생성자 __init__()
# 인스턴스 메소드 coffee_info : 원두의 정보를 출력하는 메서드
# 인스턴스 변수 : bean

# Espresso 클래스
# 상속받는 class : Coffee
# 생성자 __init__()
# 인스턴스 메소드 espresso_info() : 원두와 물의 양을 출력하는 메서드
# 인스턴스 변수 : water

# coffee = Espresso('콜롬비아',30)
# coffee.espresso_info()
# [출력결과]
# 원두 : 콜롬비아
# 물 : 30ml


class Coffee:
    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print(f'원두 : {self.bean}')


class Espresso(Coffee):
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print(f'물 : {self.water}ml')

coffee = Espresso('콜롬비아',30)
coffee.espresso_info()

class Americano(Espresso):
    def __init__(self, bean, water, more_water):
        super().__init__(bean, water)
        self.more = more_water

    def americano_info(self):
        super().espresso_info()
        print(f'에스프레스에서 물을 {self.more}만큼 추가')

coffee = Americano('콜롬비아',30, 200)
coffee.americano_info()
# 원두 : 콜롬비아
# 물 : 30ml
# 에스프레스에서 물을 200만큼 추가



# Shape라는 추상 클래스를 정의하고,
# 이를 상속받는 Rectangle, Circle 클래스를 만들어서 면적을 계산하는 프로그램을 작성해보자
# 여기서 pi값은 3.14로 취급한다.
# shape : area() 메서드만 가지고있다.
# Rectangle, Circle : 생성할 때 필요한 길이(가로, 세로, 반지름 등)을 입력받고
#                    면적을 계산하는 area() 메서드를 가진다.

# rectangle = Rectangle(10, 5)
# circle = Circle(7)
# print(rectangle.area())
# print(circle.area())
# [출력결과]
# 50
# 153.86

from abc import *
# import abc

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

rectangle = Rectangle(10, 5)
circle = Circle(7)
print(rectangle.area())
print(circle.area())



# __메서드__ --> 매직 메서드 (Magic methods, Dunder Methods)

# __init__
# __del__

# __str__ : 객체(인스턴스)가 가지는 문자열 값을 설정하는 메서드

print(circle) # <__main__.Circle object at 0x00000216B5BC7230>
# ---> 객체의 문자열 기본값


# class Temp:
#     # pass
#     def __str__(self):
#         return f'내가 객체를 표현하고 싶은 형태로 문자열을 반환'
#
#
# temp = Temp()
# print(temp) # 내가 객체를 표현하고 싶은 형태로 문자열을 반환


# __add__ : 두 객체를 더했을 때 실행할 연산처리 과정을 설정할 수 있다.
# __eq__ : 두 객체를 == 연산 했을 때 실행할 연산처리 과정을 설정할 수 있다.
#

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'<{self.x}, {self.y}>'

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return None

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return None


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2) # <4, 6>
print(p1 == p2) # False
print(p1 == p1) # True
print(p1) # <1, 2>

# 파이썬 속성 비공개화

p1.x = 100
print(p1.x) # 100

# 2가지 방식

# 1. _변수명의 형태로 속성 선언 : 이 속성 데이터는 굳이 건들지 마라

# 2. 맹글링(변경), __변수명으로 선언하는 것
#       시스템적으로 속성명을 _클래스명__변수명으로 변경시킨다.


class Temp:
    def __init__(self):
        self._secret = "12345"
        self.__secret = "123456"

    def get_secret(self) -> int: # -> int의 형태는 반환형 힌트
        return self.__secret

    def set_secret(self, data:int): # 매개변수 옆에 :자료형 형태로
        # 매개변수에 필요한 힌트 자료형을 작성할 수 있다.
        self.__secret = data

temp = Temp()
print(temp._secret) # 12345
# --> java protected 접근제어자와 비슷한 느낌
# 클래스와 클래스의 자식 클래스에서 자유롭게 접근

# print(temp.__secret) # 너 이변수 없어! 오류
# java private 접근제어자와 비슷한 느낌
# --> 클래스 내부에서만 접근할 수 있는 변수

print(temp._Temp__secret) # 123456
# 속성의 변수명을 알고 있다면 접근은 가능하다.
# print(temp._Temp) # 외부에서는 이 속성이 있는지 확인할 수 없다. 자동완성도 미지원


# getter, setter
# 비공개 변수에 대해 값을 얻거나 설정할 수 있도록 만든 메서드
#
p1.x = 1000
print(temp.get_secret()) # 123456
# 단순히 값을 저장하고 반환하는 것이 아니라 개발자가 원하는 과정을 거치게 만들 수 있다!!


# 시스템이 데이터를 확인하고 자동으로 자료형을 지정
temp.set_secret("aasd")
# 매개변수에 지정한 자료형 힌트와 다른 데이터를 입력하였다면 compile과정에서 주의 표시를 띄워준다.
















































































