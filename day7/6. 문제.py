# 커피 자판기 프로그램.
# 1. 커피 자판기에 돈과 주문할 커피를 전달
# 2. 주문할 수 잇는 커피의 종류와 가격
# '아메리카노':1000,
# '카페라떼':1500,
# '카푸치노':2000
# 3. 없는 커피를 주문할 경우 입력한 돈을 그대로 반환
# 4. 구매 금액이 부족하면 입력한 돈을 그대로 반환
# 5. 정상 주문이면 주문한 커피와 잔돈을 반환
# 6. 함수만 만들면 된다.

# def coffee_machine(money, pick):
#     print(f'{money}원에 {pick}을 선택하였습니다.')
#     menu = {
#         '아메리카노': 1000,
#         '카페라떼': 1500,
#         '카푸치노': 2000
#     }
#     if pick not in menu:  # 없는 커피를 주문할 경우
#         print(f'{pick}은 판매하지 않습니다.')
#         return money, '없는 메뉴'
#     elif menu[pick] > money:  # 구매할 금액이 부족한 경우
#         print(f'{pick}은 {menu[pick]}원입니다.')
#         return money, '금액 부족'
#     else:  # 정상주문이라면
#         return money - menu[pick], pick
#
#
# order = input('커피를 선택하세요. (아메리카노, 카페라떼, 카푸치노) >>> ')
# pay = int(input('얼마를 내시겠습니까? >>> '))
#
# change, coffee = coffee_machine(pay, order)  # return 값은 ,로 2개를 줄 수 있다.
# print(f'잔돈 {change}원, 커피 {coffee}')

# 700원자리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하세요.
# 돈을 넣으면 몇 잔의 음료수를 뽑을 수 있는지 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 구현하세요.

# 함수 정의 : 알아서
# *반환값 : 없음
# 함수 이름 : vending_machine()
# 매개변수 : 정수 money

# 실행 예)
# 음료수 = 0개, 잔돈 = 3000원
# 음료수 = 1개, 잔돈 = 2300원
# 음료수 = 2개, 잔돈 = 1600원
# 음료수 = 3개, 잔돈 = 900원
# 음료수 = 4개, 잔돈 = 200원

def vending_machine(money):
    price = 700
    count = money // price
    for i in range(count + 1):
        change = money - i * price
        print(f'음료수 = {i}개, 잔돈 = {change}')


vending_machine(3000)
