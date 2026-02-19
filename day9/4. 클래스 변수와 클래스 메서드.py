

# 클래스 변수
# 클래스를 기반으로 생성한(하는) 모든 인스턴스들이 공유하는 변수

# 인스턴스마다 다른 값을 가져야하는 경우에는 인스턴스 변수로
# 모든 인스턴스가 동일한 값을 가져야한다같은 경우에는 클래스 변수로 정의 해서 값을 공유하는 것이 좋다.

class Korean:
    country = "한국"
    # 클래스에서 변수를 선언하면 그 변수는 클래스 변수가 된다.

    def __init__(self, name):
        self.name = name

student = Korean("홍길동")
print(student.name)
print(student.country) # 한국
# 인스턴스를 생성할 때 생성자에서 따로 country 변수를 선언하지 않았는데 변수를 가지고 있다

person = Korean("유재석")
print(person.country) # 한국
print()

student.country = "대한민국"
print(student.country) # 대한민국
print(person.country) # 한국
# 인스턴스에서는 클래스 변수의 값을 변경할 수 없다!
# --->  인스턴스 변수 country를 선언한 것!
# student 인스턴스는 인스턴스 변수와 클래스 변수 country 두 개의 변수를 가지게 된 것

print(student.__class__.country) # 한국
# 인스턴스에서 클래스에 접근하여 클래스변수를 호출하였다

# 클래스 변수는 인스턴스 뿐 아니라 클래스에서 접근이 가능한 변수이다.
# 따라서, 기본적으로 클래스에서 접근해서 사용하는 변수이다.
print(Korean.country) # 한국
## 인스턴스(객체)를 생성하지 않아도 사용할 수 있는 변수!
print()


Korean.country = "대한민국"
print(Korean.country) # 대한민국
print(person.country) # 대한민국

# 1. 모든 인스턴스들이 값을 공유하는 변수!
# 2. 클래스에서 직접적으로 사용할 수 있는 변수!
# ---> 인스턴스를 생성하지않아도 사용할 수 있는 변수!!

# 인스턴스 변수의 생성시점
# 아무리 빨라도 객체(인스턴스)를 생성한 시점부터 생성할 수 있다.

# 클래스 변수의 생성시점
# 프로그램이 시작하면서 class를 읽어들이는 시점에 값의 초기화가 일어난다.
# --> 변수가 생성된다!


# 클래스 메서드
# 클래스 변수를 사용하는 메서드를 의미한다.
# --> cls라는 매개변수를 사용하는 메서드

class Korean2:
    country = "한국"

    # @~~~
    # 데코레이터(decorator)
    # 시스템에 추가적으로 정보를 알려주는 코드
    # 코드를 꾸미는 기능을 한다.

    @classmethod # 내가 작성한 메서드는 클래스 메서드야!
    def trip(cls, country):
        if cls.country == country:
            print("국내 여행")
        else:
            print("해외 여행")
        # cls : class명을 대신해서 사용하는 대명사 키워드

    # @classmethod  # 내가 작성한 메서드는 클래스 메서드야!
    def trip2(cls, self, country):
        if cls.country == country:
            print("국내 여행")
        else:
            print("해외 여행")
#       cls는 class를 뜻하는 cls가 아니라 매개변수 cls가 되어버리고
#       self가 활성화되면서 trip2은 인스턴스 메서드가 된다


    def trip3(self):
        print(Korean2.country)
        Korean2.trip("한국")

    @classmethod
    def trip4(cls, instance):
        print(instance.data)


person3 = Korean2()
person3.trip("한국") # 국내 여행
Korean2.trip("일본") # 해외 여행
# 클래스 메서드 또한 클래스에서 직접 호출이 가능하다.
# ---> 사용에 인스턴스가 필요없다!
# 주로 객체(인스턴스)에서 호출하지않고 클래스에서 직접 사용한다.

'''
주의점
클래스 메서드에서는 인스턴스 변수와 인스턴스 메서드를 사용할 수 없다!

---> 인스턴스 변수와 메서드 및 클래스 변수와 메서드의 생성시점 차이때문!!

# 클래스 변수와 메서드의 생성 시점은
# 프로그램이 클래스의 정의를 읽어들일 때 생성된다.

반면, 인스턴스 변수는 인스턴스를 생성하고, 인스턴스 변수에 값을 초기화 하는 시점에 생성된다
그리고 인스턴스 메서드는 인스턴스 변수를 사용하는 메서드를 뜻한다
---> 인스턴스의 존재가 필수적!

따라서, 클래스 메서드의 생성시점에는 인스턴스가 존재하지않기 때문에
인스턴스 변수와 인스턴스 메서드는 클래스 메서드에서 사용할 수 없다.
'''


person3.trip2("self매개변수에 들어갈 데이터", "국가")


person3.data = "data!"
Korean2.trip4(person3) # data!
# 클래스 메서드에 매개변수로 인스턴스를 받아서 인스턴스 메서드나 변수를 사용할순 있다.
# 이렇게 사용할바에는 인스턴스 메서드로 생성해서 사용한다!






















































































































































