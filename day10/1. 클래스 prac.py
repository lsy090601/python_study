

# Area 라는 클래스를 만들어보자
# Area를 선언할 때 가로길이 a와 세로길이 b를 받아서 인스턴스 변수에 저장한다.
# Area 클래스는 메서드로 square() 메서드와 triangle() 메서드를 가지고 있다.
# 가지고 있는 a와 b를 사용해서 square()는 사각형, triangle()는 삼각형의 넓이를 반환한다
'''
area = Area(10, 20)
print(area.square())
print(area.triangle())

[출력 결과]
200
100.0
'''


class Area:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def triangle(self):
        # return (self.a * self.b) / 2
        return self.square() / 2

area = Area(10, 20)
print(area.square())
print(area.triangle())





# 가방 객체을 만들 때마다 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스를 만들어 보자
# 가방 객체를 삭제하면 Bag count가 줄어든다!
# 현재 가방 개수를 볼 수 있는 now 메서드를 만들어보자
'''
print(f'현재 가방 {Bag.now()}개')
# 1. Bag 클래스에서 호출하는 메서드 --> 클래스 메서드 or 정적 메서드
# 3. 메서드에서 변수값을 출력하는 중 --> 클래스 변수
bag1 = Bag()
bag2 = Bag()
# 4. 인스턴스 "생성 시" 클래스 변수의 값이 증가한다. ===> 생성자
print(f'현재 가방 {Bag.now()}개')
# 2. 인스턴스만 생성하고 똑같은 메서드를 실행했는데 값이 바뀌었다. --> 무조건 클래스 메서드
del bag1
# 5. 인스턴스 소멸 시 클래스 변수의 값이 감소한다. ==> 소멸자
print(f'현재 가방 {Bag.now()}개')

[출력결과]
현재 가방 0개
현재 가방 2개
현재 가방 1개
'''

class Bag:
    count = 0

    def __init__(self):
        Bag.count += 1

    def __del__(self):
        Bag.count -= 1

    @classmethod
    def now(cls):
        return cls.count

print(f'현재 가방 {Bag.now()}개')
bag1 = Bag()
bag2 = Bag()
print(f'현재 가방 {Bag.now()}개')
del bag1
print(f'현재 가방 {Bag.now()}개')






# Shop 클래스를 구현해보자
# shop은 떡볶이 -> 3000원, 순대 -> 2500원, 튀김 -> 500원, 김밥 -> 2000원 으로 팔고있다.
# sales 메서드를 가지고 있다
# sales 메서드는 메뉴와 주문개수를 인수로 받는다
# 주문 개수가 1개라면 메뉴명만 인수로 받아도 상관없다!
'''
Shop.sales('떡볶이')
# --> 클래스에서 메서드를 호출 ---> 클래스 메서드 or 정적 메서드
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)
print(f'총 매출 {Shop.total}원') #  ---> 클래스 변수를 호출했는데 매출에 영향이갔네 

[출력결과]
총 매출 9500원
'''

class Shop:
    total = 0
    menu = {"떡볶이" : 3000, "순대" : 2500, "김밥" : 2000, "튀김" : 500}
    @classmethod
    def sales(cls, menu, count=1):

#         1. if문
#         if menu == "떡볶이":
#             cls.total += 3000 * count
#         elif menu == "순대":
#             ...

#         2. match - case
#           match menu:
#               case "떡볶이":
#                   cls.total += 3000 * count
#               case "순대":
#                   ...

#         3. 클래스에 변수로 menu를 생성
#             cls.total += cls.menu[menu] * count
            cls.total += cls.menu.get(menu) * count

Shop.sales('떡볶이')
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)
Shop.sales('튀김', 120)
print(f'총 매출 {Shop.total}원') # 총 매출 69500원

































































































