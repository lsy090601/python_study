

# 제어문
# 프로그램의 실행흐름을 제어하는 구문

# if문 , 반복문...


# break, continue
# 반복문에서 사용하는 제어문


# break문
# 자신이 속한 코드블럭의 반복문을 강제로 종료하는 제어문

for i in range(10):
    print(i)
    # if i == 5:
    break


# while True:
#     num = int(input("숫자를 입력 0이면 종료"))
#     if num == 0: break
#     print(num)



# num = int(input("숫자를 입력하세요 >> "))
# n = 2 # 2부터 나누기 시작할꺼기 때문
# is_prime = True
#
# while n < num: # 2 ~ num - 1의 숫자까지
#     if num % n == 0:
#         is_prime = False
#         break # # 판별이 끝났으니 n - 1까지 판별할 필요가없다!
#     n += 1
#
# if is_prime:
#     print(f"{num}은 소수입니다.")
# else:
#     print(f"{num}은 소수가 아닙니다.")

print()
for _ in range(3): # [0,1,2]
    for i in range(4): # [0, 1,2,3]
        print(i)
        break
# break문이 영향을 주는 반복문의 개수는 1개이다.




# continue문
# 반복문에서 continue를 만나면 반복문의 시작지점으로 제어의 흐름을 옮긴다.
# --> 다음 회차의 반복을 실행한다.
# 반복문을 실행하다가 생략하거나 제외하고 싶은 코드가 있는 경우 사용한다.

print()
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# 짝수인 경우 continue를 만나 다음 반복이 실행된다.
# for문의 반복 시작지점은 iterable의 요소를 확인하고 요소를 변수에 대입하는 시점

print()
num = 1
while num < 5:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1

# while문 같은 경우에는 반복문의 시작지점이 조건식을 확인하는 것!
# 따라서 while문에서 continue를 사용할 때에는 증감식을 확인해서 코드의 무한루프를 조심해야한다.





# pass 문
# if True:
# print()
# 코드블럭을 열고 안에 아무 코드를 작성하지않고 코드블럭을 닫으면 오류발생!

if True:
    pass

# 코드블럭을 열었을 떄 아무 코드를 작성하기 싫을 때 사용하는 제어문
# 이름만 정의해두고 실행부분(코드블럭)을 나중에 구현할 때
# 특정 조건문이나 반복문에서 아무 동작도 구현하지않을때


# 알아두면 좋은 함수

# len(iterable) 함수
# 함수에 전달된 객체(데이터)의 길이(요소의 개수)를 반환해주는 함수

li = [1,2,3,4]
print(len(li)) # 4
print(len("hello world")) # 11
print(len({"key" : "value", "key2" : "value2"})) # 2
print()


# sorted(iterable)
# 전달된 iterable의 오름차순 정렬결과를 반환해주는 함수

li = [2,4,1,5,33,123,7]
print(li)       # [2, 4, 1, 5, 33, 123, 7]
print(sorted(li)) # [1, 2, 4, 5, 7, 33, 123]
print(li)       # [2, 4, 1, 5, 33, 123, 7]

# reverse 옵션
print(sorted(li, reverse=True)) # [123, 33, 7, 5, 4, 2, 1]
# reverse옵션을 활성화하면 내림차순 결과를 반환한다.


# enumerate(iterable)
# iterable에 저장된 요소와 해당 요소의 인덱스를 튜플로 묶어 iterable에 저장하여 반환한다.

li = ["가위", '바위', '보']
for i in enumerate(li):
    print(i)
# (0, '가위')
# (1, '바위')
# (2, '보')

for index, value in enumerate(li):
    print(f'번호 {index + 1}, data : {value}')



# eval() 함수
# 문자열로 된 연산식을 int데이터의 연산으로 취급해서 실행하는 함수
print("100" + "100") # 100100
print(eval("100 + 200")) # 300
print(eval("round(100.7) + 200")) # 301

# abs() 함수
# 숫자의 절대값을 반환해주는 함수
print(abs(-2)) # 2

# round()
# 반올림 함수
print(round(1.5)) # 2
print(round(3.141592)) # 3
# 소수점 1자리에서 반올림을 한다.

# round(반올림할 데이터, 반올림할 자리수)
# 반올림할 자리수는 생략 시 0이 지정된다.
print(round(3.141592,2)) # 3.14
print(round(3.141592,3)) # 3.142
print(round(3.141592,-1)) # 0.0


# min()
# max()

numbers = [45, 23, 67, 12, 89, 34, 56]
print(min(numbers)) # 12
print(max(numbers)) # 89

































