

# datetime 모듈을 이용한 시간계산

import datetime

date = datetime.datetime.now()
print(date)
date2 = datetime.datetime(2026, 2, 10, 10, 50, 20)
print(date2)


print(date - date2) # 13 days, 0:04:41.794775
# timedelta 클래스의 객체로 반환된다
# timedelta가 가지고 있는 total_seconds() 메서드로 초로 반환할 수 있다.
print((date - date2).total_seconds()) # 1123554.800982

# datetime 객체 - datetime 객체 --> timedelta 객체
# datetime 객체 + datetime 객체 ---> X
#
# datetime 객체 기준으로 더하면 년도나 월 일 등 원하는 기준이 너무 복잡해서 시스템으로 막아두었다!
#
# datetime + timedelta ---> datetime 객체
# datetime - timedelta ---> datetime 객체

from datetime import timedelta

# timedelta() 생성자
# 모든 매개변수는 디폴트 매개변수
# days, seconds, microseconds, millisecond, minutes, hours, weeks

temp = timedelta(days=10, hours=1)
temp = timedelta(10) # == timedelta(days=10)
# 첫 번째 매개변수days
print(temp)

print(date + temp)  # 2026-03-05 11:03:54.491334
print(date - temp)  # 2026-02-13 11:03:54.491334

# 날짜 데이터 포메팅
print(f'{date.year}년 {date.month}월 {date.day}일')
# 2026년 2월 23일

# datetime의 strftime() 메서드
# strftime("포메팅할 형식")

print(date.strftime("%y년 %m월 %d일")) # 26년 02월 23일
print(date.strftime("%Y년 %m월 %d일")) # 2026년 02월 23일


# %a : 요일을 축약된 영문으로 표기 ex) Sun, Mon
print(date.strftime("%a")) # Mon

# %A : 요일을 영문 전체로 출력 ex) Sunday
print(date.strftime("%A")) # Monday

# %d : 월중 일(몇일인지) 0으로 채워진 10진수로 표기 ex) 08, 07
print(date.strftime("%d")) #

# %b : 월을 축약된 영문으로 표기 # Jan, Feb...
print(date.strftime("%b")) # Feb

# %B : 월을 영문 전체으로 표기 #  February
print(date.strftime("%B")) # February

# %m : 월을 0이 포함된 숫자로 표기
print(date.strftime("%m")) # 02

# %y : 세기가 없는 년도를 0이 포함된 10진수
print(date.strftime("%y")) # 26

# %Y : 세기가 포함된 년도를 0이 포함된 10진수
print(date.strftime("%Y")) # 2026

# %H : 24시간 기준 시간 표기
print(date.strftime("%H")) # 11

# %I : 12시간 기준 시간 표기
print(date.strftime("%I")) # 11

# %p : AM PM 표기
print(date.strftime("%p %I")) # AM 11

# %M    : 0으로 채워진 분
# %S    : 0으로 채워진 초

# strptime()
# 문자열 데이터를 날짜(datetime)데이터로 변환시키는 메서드
# strptime("날짜 문자열", 문자열의 포메팅형식)

#ex)
date = datetime.datetime.strptime("2026/02/23 11:15", "%Y/%m/%d %H:%M")
print(date) # 2026-02-23 11:15:00





# jetbrain - IDE에서
# 라이브 템플릿 livetemplates
# 개발자가 지정한 코드단축키(약어?)

# 반복 사용하는 코드의 틀을 저장해두고 쉽게 불러와서 사용할 수 있도록 해주는 기능
# 설정 (setting) - 에디터(Editor) - 라이브 템플릿(livetempates) - python(사용구역)
# +-로
# Abbreviation(약어) : 단축키로 저장할 단어
# Description(설명글) : 템플릿에 대한 설명글
# Template text : 단축키를 실행했을 때 출력할 코드
# Define(정의) : 이 IDE에서 이 템플릿을 사용할 수 잇는 범위 지정

# Loren Ipsum n: 의미없는 문자열의 나열, 공백 채우기용 문자열
























































































