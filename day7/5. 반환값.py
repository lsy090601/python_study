# 반환값
# 함수 호출 결과를 반환값(return value)
# 반환값이 있으면 함수 내부에서 return문을 통해 값을 반환할 수 있고,
# 반환값이 없으면 함수 내부에 return문을 작성할 필요가 없음

# 1. 반환값이 있는 함수

def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str


print(address())


# 2. 반환값이 없는 함수
def address2():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    print(str)


print(address2())


# 3. 함수의 종료를 위한 return
# 반환값이 있으면 return문을 사용해 반환하고, 반환값이 없으면 return문을 생략해도 된다.
# 반환값이 없을 때도 return문을 작성하는 경우 -> 함수를 종료할때

def charge(energy):
    if energy <= 0:
        print('0이하의 에너지는 충전이 불가능합니다.')
        return  # charge() 함수의 종료를 의미
    print('에너지가 충전되었습니다.')


charge(1)
charge(-1)

# 4. 파이썬의 함수는 객체 자료형이다.
print(charge)  # <function charge at 0x0000017D3E73C7C0>


# 5. 함수안에 함수선언도 가능
def print_greet(name):
    def get_greet():
        return "안녕하세요"

    print(name + '님 ' + get_greet())


print_greet('김철수')
