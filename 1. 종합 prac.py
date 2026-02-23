# 1번
'''
[문제]
문자열 슬라이싱으로 출력결과와 같도록 출력해보자.

mystr = 'GOOD NIGHT'

[출력결과]
OO
 NIGHT
GH
OD

'''
from fileinput import close
print("문제 1번 \n")

mystr = 'GOOD NIGHT'
print(mystr[1:3])
print(mystr[4:])
print(mystr[7:9])
print(mystr[2:4])

print("\n\n\n")

# 2번
'''
1, 2, 3, 4...를 계속 더해나가는 프로그램이 존재한다.

숫자 하나를 입력받을 때,
즉, 1부터 n까지 더해나간다고 할 때
어디까지 더해야 입력한 수보다 같거나 커지는지 출력해보자 

[출력 결과]
숫자를 하나 입력해주세요 : 55
n : 10

[출력 결과 2]
숫자를 하나 입력해주세요 : 54
n : 10

[출력 결과 3]
숫자를 하나 입력해주세요 : 56
n : 11
'''
print("문제 2번 \n")

scan_num = int(input("숫자를 하나 입력해주세요 : "))
n = 0
total = 0
while scan_num > total:
    n += 1
    total += n
print(f'n : {n}')

print("\n\n\n")

'''
변수 num1에 input 함수를 이용해서 숫자를 입력받도록 한다.
변수 num2에 input 함수를 이용해서 숫자를 입력받도록 한다.

아래의 출력결과와 같이 출력하시오.
format 함수 포매팅, f 문자열 포매팅방식으로 표현하시오.


[출력결과]
첫번째 숫자를 입력하세요 : 10  
두번째 숫자를 입력하세요 : 20 
I eat 10 apples. You eat 20 apples.
I eat 10 apples. You eat 20 apples.

'''
print("문제 3번 \n")

num1 = input("첫번째 숫자를 입력하세요 : ")
num2 = input("두번째 숫자를 입력하세요 : ")
print(f'I eat {num1} apples. You eat {num2} apples.')
print(f'I eat {num1} apples. You eat {num2} apples.')

print("\n\n\n")


# 4번
'''
어떤 수들이 있을 때, 그 수들을 대표하는 값으로 가장 흔하게 쓰이는 것은 평균이다.
평균은 주어진 모든 수의 합을 수의 개수로 나눈 것이다. 예를 들어 10, 40, 30, 60, 30의 평균은
170 / 5 = 34가 된다.

평균 이외의 또 다른 대표값으로 중앙값이라는 것이 있다.
중앙값은 주어진 수를 크기 순서대로 늘어 놓았을 때 가장 중앙에 놓인 값이다.
예를 들어 10, 40, 30, 60, 30의 경우, 크기 순서대로 늘어 놓으면
10 30 30 40 60 이 되고 중앙값은 30이 된다.

다섯 개의 자연수를 요소로 가진 리스트를 인수로 전달하였을 때 이들의 평균과 중앙값을 출력하는 함수를 작성하시오.


실행 예:
avg_mid([10, 30, 30, 40, 60])
[출력 결과]
평균 : 34.0, 중앙값 : 30

'''

print("문제 4번 \n")

avg_mid = [10, 30, 30, 40, 60]
sum = 0
for i in range(len(avg_mid)):
    sum += avg_mid[i]
print(f'평균 : {sum/len(avg_mid)}, 중앙값 : {avg_mid[2]}')

print("\n\n\n")


# 5번
'''
input으로 숫자 n을 입력받고 아래 문자열을
길이 n씩 잘라서 리스트를 만드세요
만약, 숫자 n보다 길이가 짧다면 남은 문자열 그대로 저장하세요

"The quick brown fox jumps over lazy dogs"

[출력 결과 1]
숫자를 입력하세요 >>> 4
['The ', 'quic', 'k br', 'own ', 'fox ', 'jump', 's ov', 'er l', 'azy ', 'dogs']

[출력 결과 2]
숫자를 입력하세요 >>> 3
['The', ' qu', 'ick', ' br', 'own', ' fo', 'x j', 'ump', 's o', 'ver', ' la', 'zy ', 'dog', 's']

'''
print("문제 5번 \n")
s = "The quick brown fox jumps over lazy dogs"
n = int(input("숫자를 입력하세요 >> "))
result = []
for i in range(0,len(s),n):
    result.append(s[i:i+n])
print(result)
print("\n\n\n")


# 6 번
'''
[문제] 윤년 판단
년도를 입력받아 윤년인지 판정해주는 프로그램을 작성하시오.

- 년수가 4로 나누어 떨어지는 해는 윤년
- 그 중에서 100으로 나누어 떨어지는 해는 평년
- 다만 400으로 나누어 떨어지면 다시 윤년
- 2016년은 윤년, 2100년은 평년, 2000년은 윤년

[출력결과]
년도를 입력하세요 : 2020
윤년입니다!

'''
print("문제 6번 \n")
year = int(input("년도를 입력하세요 :"))
if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print("윤년입니다")
        else:
            print("평년입니다")
    else :
        print("윤년입니다")
else :
    print("윤년이 아닙니다")
print("\n\n\n")

# 7번
'''
7 - 1
for문을 이용해서 500과 1000사이에 있는 홀수의 합계 구하기

[출력결과]
500과 1000사이에 있는 홀수의 합계 : 187500



7 - 2
숫자 9284637913의 각 자리의 수의 합을 구하세요

[출력 결과]
52


7 - 3
input으로 숫자 n을 입력받고
입력한 숫자가 홀수면 1 ~ n 까지의 짝수의 합을 반환
입력한 숫자가 짝수면 1 ~ n 까지의 홀수의 합을 반환하세요

실행 예:
숫자 n : 11
1 ~ 11까지의 홀수의 합 : 36
'''
print("문제 7-1번 \n")
result = 0
for i in range(501,1000):
    if i % 2 == 1:
        result += i
print(f'500과 1000사이에 있는 홀수의 합계 : {result}')
print("\n\n\n")

print("문제 7-2번 \n")
str_num = 9284637913
total = 0
while str_num > 0:
    total += str_num % 10
    str_num //= 10
print(total)
print("\n\n\n")

print("문제 7-3번 \n")
n = int(input("숫자 n :"))
sum = 0
if n % 2 == 0:
    for i in range(n):
        if n % 2 == 0:
            sum += i
    print(f'1~{n}까지의 짝수의 합 :{sum}')

else :
    for i in range(n):
        if n % 2 == 1:
            sum += i
    print(f'1~{n}까지의 홀수의 합 :{sum}')

print("\n\n\n")

# 8번
'''
시간 계산

현재시간과 요리에 걸리는 시간을 초로 입력하면 종료되는 시간을 출력하는 프로그램을 만들어보자 

현재시간은 "시 분 초"의 형태로 입력하고,
요리에 걸리는 시간은 초의 형태로 입력한다.

check_time(현재시간, 초)

실행 예)
check_time("14 30 0", 200)

[출력 결과]
14시 33분 20초
'''

#
# def check_time(self, time, spendtime):
#         self.hour, self.minute, self.second = time.split(" ")
#         self.spendtime = spendtime
#
#
# check_time("14 30 0", 200)
# if self

# 9번
'''
유저 정보가 있을때
username과 password를 입력받고
아이디가 있고 비밀번호가 맞으면 "로그인에 성공하였습니다."
아이디가 있고 비밀번호가 틀리면 "비밀번호를 확인해주세요"
아이디가 없으면 "아이디를 확인해주세요"를 출력하세요

[출력결과 1]
아이디를 입력해주세요 >>> user1
비밀번호를 입력해주세요 >>> pas
비밀번호를 확인해주세요

[출력 결과 2]
아이디를 입력해주세요 >>> user
아이디를 확인해주세요

[출력 결과 3]
아이디를 입력해주세요 >>> user3
비밀번호를 입력해주세요 >>> password3
로그인에 성공하였습니다
'''
# import re
#
# users = {
#     "user1": "password1",
#     "user2": "password2",
#     "user3": "password3"
# }
# pattern = re.compile(users)
# username = str(input("아이디를 입력해주세요 >>>"))
# if pattern.match(username):
#     password = str(input("비밀번호를 입력해주세요 >>>"))
#     if pattern.match(password):
#         print("로그인에 성공하였습니다")
#     else :
#         print("비밀번호를 확인해주세요")
# else :
#     print("아이디를 확인해주세요")

# 10번
'''
영어로된 문자열을 입력하였을 때 그 문자열에 사용된 알파벳이 몇번 사용되었는지 출력하는 프로그램을 만들어보자
이 때 대소문자는 구분하지않고 소문자로 결과를 출력한다.
또한 공백(space)는 문자로 취급하지않는다.

실행 예 :
alphabet_count("Hello world")
[출력 결과]
사용된 알파벳은
'h' : 1회
'e' : 1회
'l' : 3회
'o' : 2회
'w' : 1회
'r' : 1회
'd' : 1회
입니다.

'''
# import re
# pattern = re.compile('[a-zA-Z]')
# alphabet_count = "Hello world"
# print(alphabet_count.lower())
# print(alphabet_count.replace(" ", ""))
# print(pattern.findall(alphabet_count))

# 11번
'''
369 게임을 출력하는 프로그램을 만들어보자
숫자를 입력하면 그 순번까지의 3 6 9 게임 결과를 출력하는 프로그램을 만들어보자

3 6 9 게임은?
여러 사람이 순서를 정한 후, 순서대로 수를 부르는 게임이다.
만약 3, 6, 9 가 들어간 수를 불러야 하는 상황이라면, 수를 부르는 대신 "박수(X)" 를 쳐야 한다.
33과 같이 3,6,9가 두 번 들어간 수 일때, "XX"과 같이 박수를 두 번 치는 형태도 있다. 

[출력 결과 1]
순번 : 9
결과 : 1 2 X 4 5 X 7 8 X

[출력 결과 2]
순번 : 33
결과 : 1 2 X 4 5 X 7 8 X 10 11 12 X 14 15 X 17 18 X 20 21 22 X 24 25 X 27 28 X X X X XX
'''

num = int(input("순번 : "))
result = []
for i in range(1,num+1):
    count = 0
    for ch in str[i] :
        if ch=='3' or ch=='6' or ch=='9':
            count += 1
    if count ==0 :
        result.append(str[i])
    else:
        result.append("X"*count)
print(f'결과 : {result}')

# 12번
'''
문자열 agobodw perosgwra2m4mser 에서
해당 인덱스의 글자를 없애고 출력하세요

index = [0, 3, 6, 9, 12, 14, 17, 19, 21]
'''


# 13번
'''
등차수열 또는 등비수열인 리스트를 넣었을 때
마지막 원소 다음으로 올 숫자를 return하도록 사용자 함수를 만들어 보자
단, 이 때 입력되는 리스트의 길이는 최소 3이다.

test([1,2,3,4])
[출력결과]
5

test([2,4,8])
[출력결과]
16.0

'''


# 14번
'''
다음 문자열을 뒤집어 출력하세요
'다니습셨하고수 간달한'

'''
str = '다니습셨하고수 간달한'
print(str[::-1])