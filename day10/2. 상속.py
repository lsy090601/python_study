

# 상속

# 상속이란?
# 어떤 클래스가 가지고 있는 데이터(기능(메서드), 속성 등)을 그대로 물려받아서 사용할 수 있는 것을 말한다.
# 다른 클래스의 기능을 물려받을 때 "상속받는다"라는 표현을 사용한다.
# 상속 관계에 있는 클래스를 표현할 때 "부모 클래스"와 "자식 클래스"라는 말을 사용한다.

# 부모 클래스    : 상속해 주는 클래스 / 슈퍼 클래스 super class, 기반 클래스 base class
# 자식 클래스    : 상속 받는 클래스  / 서브 클래스 sub class, 파생 클래스 derived class


# 상속 관계의 구현
# 기본적으로 두 클래스가 상속 관게에 놓이려면 Is - A관계가 성립되어야한다.
# Is - A 관계는 "~~~은 ~~~이다" 라는 문장을 이용해서 일반화가 가능한 관계를 의미한다.
# ex) 학생은 사람이다. ---> Student is a Person
# 이 때 Student는 자식 클래스가 되고, Person은 부모 클래스가 된다.

# Has - A
# 구성(포함)을 뜻하는 관계
# 멤버변수로 구현을 하게된다.

# 상속의 구현(선언)
# 이미 존재하는 클래스의 데이터를 물려받는 것이기 때문에 클래스가 하나 존재해야한다.
# 서브 (자식) 클래스를 구현할 때 클래스명 옆에 ()를 이용해서 어떤 클래스의 데이터를 상속받는지 명시하여 상속을 표현할 수 있다.

class Person: # 부모 클래스
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name}이(가) {food}를 먹습니다.')

class Student(Person):
    # 자식 클래스를 정의할 때 상속받을 클래스를 명시한다.
    def __init__(self, name, school):
        super().__init__(name)
        # 부모 클래스의 생성자를 사용
        self.school = school

    def study(self):
        print(f'{self.name}은 {self.school}에서 공부합니다.')

# Student 인스턴스 생성
potter = Student("해리 포터", "호그와트")
print(potter.school)
potter.study() # 해리 포터은 호그와트에서 공부합니다.
potter.eat("고기") # 해리 포터이(가) 고기를 먹습니다.
# 자식 클래스에서 부모 클래스의 변수와 메서드를 모두 사용할 수 있다!

# super()
# 부모 클래스를 호출하는 것과 같다.
# 자식클래스에서 super 키워드를 사용해서 부모클래스에 존재하는 변수와 메서드를 사용할 수 있다.



# 서브 클래스의 __init__()
# 파이썬 같은 경우에는 부모 클래스의 생성자를 호출하지않아도 주의표시만 발생

# 부모클래스에 생성자가 존재한다면 서브 클래스의 생성자를 구현할 때 슈퍼클래스의 생성자를 먼저 호출하는 코드를 작성한다
# ---> 부모클래스에서 작성한 인스턴스 변수생성코드가 정상적으로 동작

# JAVA같은 경우에는 1개의 클래스가 1개의 부모클래스를 가진다.
# 반면 파이썬 같은 경우에는 상속을 받는데에 제한이 없다.

# 파이썬의 다중 상속

class Unit:
    def __init__(self):
        print("unit의 생성자")

    def temp_method(self):
        print("unit의 메서드")
    def temp_method2(self):
        print("unit의 메서드")

class FlyAble:
    def __init__(self):
        print("FlyAble의 생성자")

    def temp_method(self):
        print("FlyAble의 메서드")

class FlyAbleUnit(FlyAble, Unit):
    # 상속을 명시할 때 ,를 이용해서 한 번에 여러 클래스로부터 데이터를 상속받을 수 있다.
    def __init__(self):
        super().__init__()
        super().temp_method2() # unit의 메서드

unit = FlyAbleUnit() # FlyAble의 생성자
# super() 키워드는 모든 부모클래스의 데이터를 가지고있다!
# 하지만 부모 클래스에 동일한 데이터가 존재하는 경우 (똑같은 이름의 변수나 메서드 등)
# super()가 상속받을 때 명시한 부모 클래스의 순서대로 앞에 위치한 부모클래스의 데이터를 우선해서 가져온다
# ---> 시스템이 부모 클래스에 접근하는 순서는 명시한 부모클래스의 순서를 따른다.

# 클래스에서 데이터의 접근 순서를 알려주는 메서드 mro()
# method resolution order ---> 메서드 결정 순서
print(FlyAbleUnit.mro())
# [<class '__main__.FlyAbleUnit'>, <class '__main__.FlyAble'>, <class '__main__.Unit'>, <class 'object'>]

# object(객체) 클래스
# 프로그래밍에 존재하는 모든 클래스의 최상위 조상(부모) 클래스


# 메서드 오버라이딩 (method overriding), 메서드 재정의
# 슈퍼 클래스에서 존재하는 메서드를 자식 클래스에서 재정의 하는 것


class Animal:
    def move(self):
        print(f'동물이 이동합니다.')

class Dog(Animal):
    def move(self):
#         자식 클래스에서 부모 클래스에 존재하는 메서드와 똑같은 이름의 메서드를 선언하면 자동으로 오버라이딩이 실행된다.
        super().move()
        # super()를 이용해서 부모클래스가 가지고 있는 메서드를 가져올 수 있다.
        print(f'강아지가 달려갑니다.')

class Fish(Animal):
    def move(self):
        print("물고기가 헤엄쳐갑니다.")

dog = Dog()
dog.move() # 강아지가 달려갑니다.



# 자식 클래스의 인스턴스 (다형성)

# 다형성
# 한 개의 객체가 여러 클래스의 인스턴스가 될 수 있다는 것을 뜻한다.

# 부모클래스의 객체는 부모 클래스의 인스턴스이다.

# 자식클래스의 객체는 자식 클래스의 인스턴스이다.
# 부모 클래스의 인스턴스이기도 하다.

# 즉, 자식 클래스 Dog의 인스턴스 dog는
# 부모 클래스 Animal의 인스턴스 이기도 하다.
# dog 데이터는 Dog 자료형에도 담을 수 있고, Animal 자료형에도 담을 수 있다.
# ----> 형 변환(캐스팅)이 가능하다.


# 자식 인스턴스에서 부모 클래스로 형변환하는 업캐스팅은 가능하다.

# 자식 인스턴스에서 부모 클래스로 형변환한 객체(업스캐스팅한 객체)에 한해서는
# 부모 클래스에서 자식 클래스로 다운 캐스팅이 가능하다.

# 부모 인스턴스가 자식 클래스로 형변환하는 다운 캐스팅은 불가능하다.

# 어떻게 가능한가?
# 자식 클래스 ---> 부모 클래스의 모든 데이터(코드)를 상속받은 상태
# 따라서 부모 클래스(자료형, 설계도)에 필요한 모든 데이터(재료)를 자식 클래스는 가지고 있다.
# 자식클래스가 가지고 있는 데이터(재료)로 부모 클래스(설계도)대로 실체를 만들 수 있다.
# --> 자식 클래스의 인스턴스는 부모 클래스로 형변환이 가능하다.

# 반대로 자식 클래스(자료형, 설계도)의 데이터를 채우기에는 부모 클래스의 인스턴스가 가진 데이터(재료)가 부족하다.
# 부모 클래스의 인스턴스는 자식 클래스로 형변환이 불가능하다


# 데이터 관점
# 자식 클래스로 내려갈수록 클래스를 채우기위한 데이터가 많아진다. (메서드, 변수)
# 부모 클래스의 인스턴스가 가진 데이터로는 자식 클래스의 데이터를 모두 채울 수 없다.

# 개념적 관점
# 개념이 작은 자식 클래스의 인스턴스는 부모 클래스에 포함될 수 있다
# --> 일반화가 가능하다.
# 개념이 큰 부모 클래스의 인스턴스는 자식 클래스에 포함될 수 없다.
# ---> 일반화가 불가능하다

# isinstance(객체, 클래스명) 함수
# 내가 전달한 객체가 클래스의 인스턴스인지 아닌지를 확인해주는 함수

print(isinstance(dog, Dog)) # True
print(isinstance(dog, Animal)) # True

animal = Animal()

print(isinstance(animal, Dog)) # False
print(isinstance(animal, Animal)) # True

class Temp:
    pass

li = [
    dog, animal,Fish(), Temp(),
]

for i in li:
    if isinstance(i, Animal): # i가 Animal의 인스턴스 인가?
        i.move()




























































