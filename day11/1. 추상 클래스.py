

# 추상 클래스

# 추상 클래스?
# 추상 메서드를 하나 이상 가지고 있는 클래스

# 추상 메서드?
# 메서드는 선언되어있지만 구현부가 구현되어있지않는 메서드
# 선언부   : def 함수이름(매개변수)
# 구현부   : 함수의 코드블럭 부분

# ---------------------------------------------

# 특징
# 1. 기본적으로 상속을 위해서 생성된 클래스

# 2. 추상 클래스는 인스턴스를 생성할 수 없다

# 3. 추상 클래스를 상속받은 자식(일반) 클래스는 추상 메서드를 구현하도록 시스템적으로 강제받는다!!
# ---> 장점
# 특정 메서드의 구현을 자식 클래스에서 강제해서 설계 오류 등을 방지할 수 있다.



# 추상 클래스의 사용

# abc 모듈
# abc : abstract base class

from abc import *

# import : 가져온다.
# *      : 전체

# 추상 클래스의 생성
# 클래스를 생성할 때 metaclass=ABCmeta를 상속받아 생성한다.

class Abstract_sample(metaclass=ABCMeta):
    a = 10

    @abstractmethod
    def temp_method(self):
        pass # 메서드의 구현부는 pass 키워드를 사용해서 구현하지 않는다.

    def instance_method(self):
        print("일반 메서드")

# temp = Abstract_sample()
# 추상 메서드 temp_method를 가지고 있어서 인스턴스를 생성할 수 없다.


class Temp(Abstract_sample):

    def temp_method(self):
        print("추상 메서드를 자식 클래스에 맞게 오버라이딩한다!")

temp = Temp()
temp.temp_method() # 추상 메서드를 자식 클래스에 맞게 오버라이딩한다!


# 강제성
# 특정 메서드의 구현을 자식 클래스에서 강제한다!
# 설계 오류 등을 방지하거나 특정 아이템을 구현할 때 안바뀌는 공통적인 부분은 코드를 완성해 두고 아이템별로 미세하게 바뀌는 부분을 추상 메서드로 구현해서 나중에 자식 클래스에서 추상 메서드만 구현해서 바로 사용하도록 하는 등

# class Animal:
#     def move(self):
#         print(f'동물이 이동합니다.')
#
# class Dog(Animal):
#     pass
#
# class Fish(Animal):
#     def move(self):
#         print("물고기가 헤엄쳐갑니다.")



print(isinstance(temp, Abstract_sample)) # True
# 추상 클래스는 자기 자신의 인스턴스를 직접 생성 못할 뿐
# 자식의 인스턴스는 자신의 인스턴스로 인식된다!




























































