
s = "hello world"
# 인덱싱으로 문자열의 뒤쪽에 있는 문자를 가져올 때
# 일일이 인덱스를 세기가 힘들다

# 마이너스 인덱스
# 문자열의 뒤쪽에서부터 순서를 세아리는 인덱스
# 단, 마이너스 인덱스의 시작은 -1이다.
# ==> -1인덱스는 문자열의 가장 마지막 문자의 인덱스
print(s[-1]) # d
print(s[-2]) # l
print(s[-3]) # r

# 문자열의 슬라이싱 (slicing)
# 인덱스를 활용해서 한 문자이상의 단어나 문장을 추출할 때 사용한다.

# 사용형태
# 문자열데이터[start:stop:step]

# start     : 시작 인덱스를 지정하는 데이터, 생략하면 0이 지정된다.
# stop      : 종료 인덱스를 지정하는 데이터, 생략하면 문자열의 끝까지 추출한다.
# step      : 인덱스의 증감값을 지정하는 데이터, 생략하면 1이 지정된다.
print(s) # hello world

print(s[1:7]) # ello w
# stop의 종료 인덱스는 슬라이싱의 범위에 포함되지않는다.
# --> 사실상 start ~ stop - 1 범위의 문자열을 가져온다!
print(s[0:5]) # hello
print(s[:5]) # hello
print(s[:]) # hello world
print(s[::]) # hello world

print(s[::2]) # hlowrd
# step에 2를 지정해서 한 문자를 출력한 후에 다음 index문자를 스킵하고
# 다음 글자를 가져왔다!

# 문자열 슬라이싱에서도 -인덱스를 사용할 수 있다
# hello world
print(s[6:]) # world
print(s[-5:]) # world
print(s[-5:-6]) #   --> 빈 데이터를 가져온다.
# start 보다 end의 데이터인덱스가 더 앞에 위치하고있어서 인덱스를 이동할 필요없이 이미 슬라이싱이 완료되었다고 생각한다.

print(s[::-1])
# dlrow olleh
print(s[::-2])
# drwolh



a='Hello World'
b='phyton is easy'

# 1. a변수의 문자열 중에 'Hello'만 출력하세요
print(a[0:5])
print(a[:5])
# 2. b변수에 저장된 문자열중에 'is'만 출력하세요
print(b[7:9])
print(b[-7:9])
print(b[-7:-5])

# 3. a변수와 b변수의 문자를 조합해서 'Hello phyton'이 출력될 수 있도록하세요
print(a[:5],b[:6]) # Hello phyton

print(a[:5], end=" ")
print(b[:6])
# 4. 슬라이싱을 이용해서 'is easy'만 출력하세요
print(b[7:])
print(b[-7:])
# 5. 슬라이싱을 이용해서 'World'만 출력하세요
print(a[-5:])
print(a[6:])
# 6. 슬라이싱을 이용해서 'World is easy'를 출력하세요
print(a[6:],b[7:])

print(a[6:], end=" ")
print(b[7:])




























