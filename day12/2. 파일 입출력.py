


# 파일 입출력

# 데이터 저장을 위해 변수를 생성해서 저장을 한다.
# 하지만 프로그램이 종료되면 변수도 삭제된다
# 프로그램이 종료된 이후에도 데이터를 저장하고 싶다면 파일의 형태로 저장해야한다.


# 파일과 파일 경로
# 파일이 가지고 있는 속성 중 파일명과 파일의 경로가 존재한다.

# C:\python_vacation\day12\2. 파일 입출력.py
# 기본적으로 이런 파일 경로라면

# 2. 파일 입출력.py ---> 파일명
# C:\python_vacation\day12\ 이 파일이 존재하는 파일의 경로가 된다.

# 이 때 확장자명이 없는 C:, python_vacation, day12같은 이름은 모두 폴더(디렉터리)이다.
# 폴더 사이의 \는 파일(폴더)를 구분하는 구분자의 역할을 가진다.

# 윈도우에서는 기본적으로 폴더 구분을 "\"을 사용하고,
# 리눅스나 맥 os 등에서는 "/"를 이용해 폴더를 구분한다.
# 최근에는 프로그램이 업데이트되면서 아무거나 사용해도 인식해준다.

# 파일의 경로 작성법 2가지

# 1. 절대 경로
# 시작지점이 똑같은 경로 ---> 루트 폴더에서 시작하는 경로
# 루트 폴더?    : 모든 파일이 들어있는 폴더
# 윈도우에서는 C:이며, C드라이브라고 부른다.
# 맥 os, 리눅스 등에서는 "\"가 루트 폴더를 뜻한다.
# ex) C:\python_vacation\day12\2. 파일 입출력.py

# 2. 상대 경로
# 시작지점이 현재 작업중인 파일이 존재하는 폴더를 기준으로 시작하는 경로
# ex) .\2. 파일 입출력.py

# 실행 파일기준으로
# . : 현재 위치하고 있는 폴더를 의미한다.
# --> C:\python_vacation\day12

# ..    : 현재 폴더의 상위 폴더
# --> C:\python_vacation

# ...   : ..의 상위 폴더
# --> C:


# 프로그램으로 운영체제, 현재 파일경로 확인하기
from pathlib import Path # --> 경로 확인을 위한 import
import platform # --> 운영체제에 대한 정보가 담긴 모듈

print(Path.cwd()) # C:\python_vacation\day12
# 현재 파일이 위치한 디렉터리의 경로를 알려준다

print(platform.system()) # Windows
# 현재 사용중인 os를 알려준다.

# import os
# path = './output'
# # 현재 경로에 위치한 output폴더
#
# if not os.path.isdir(path):
#     # isdir(path) 경로에 파일이 있냐 없냐를 확인해주는 함수
#     os.mkdir(path)
#     # mkdir(path) 경로에 폴더를 생성하는 함수

# print(os.listdir('.'))
# ['.idea', '0. 복습.py', '1. 예외처리.py', '2. 파일 입출력.py', 'output']
# 현재 폴더에 존재하는 파일,폴더명을 요소로 가진 리스트를 반환한다.


# 파일 입출력 (File I/O)

# 입력 (input)은 파일에서 데이터를 읽어오는 과정
# 출력 (output)은 프로그램에서 데이터를 파일에 쓰는 과정

# 시스템에서 파일을 다루는 과정
# 1. 파일 열기 (작업할 파일 지정)
# 2. 열린 파일객체에 대해 작업을 진행
# 3. 작업이 끝나면 파일을 닫는다
# ---------------------------------


# 1. 파일 열기
# 입출력할 파일을 지정하는 것을 의미한다.
# ---> 파일의 객체 생성

# open() 함수

# 기본 형식
# 변수 = open(파일명, 모드)

# 1) 파일명
# 입출력할 파일을 의미한다.
# 파일명만 작성할 수 있고, 경로를 함께 작성할 수 있다.

# 파일명만 작성하는 경우 --> 파이썬 소스파일(실행파일)과 같은 폴더(경로)에 존재하는 경우
# ex) file = open("file.txt")

# 경로를 사용하는 경우
# 절대 경로
# ex) file = open("C:.../day12/file.txt")
# 상대 경로
# ex) file = open("./file.txt")


# 2) 모드
# 문자 2개를 조합해서 파일에서 작업할 작업형식을 지정한다.

# 2 - 1 (입출력)

# 입력
# r (read) 읽기
# 경로에 파일이 존재하지않으면 오류가 발생

# 출력
# w (write) 쓰기
# 경로에 파일이 없으면 새로 생성, 경로에 이미 동일한 파일명이 존재해도 새로 생성 (덮어쓴다.)

# a (append) 추가
# 경로에 파일이 없으면 새로 생성, 경로에 이미 동일한 파일이 존재한다면 그 파일의 끝에서부터 내용이 추가된다.

# x (exclusive) 베타적 추가
# 경로에 파일이 없으면 새로 생성, 경로에 이미 파일이 존재한다면 오류가 발생

# 생략 시 기본적으로 r이 지정된다.

# 2 - 2 (파일의 종류)
# t (text) 텍스트 파일
# b (binary) 바이너리 파일 (텍스트 이외의 모든 파일)

# 생략 시 기본적으로 t가 지정된다.

# 모드와 종류를 조합해서 어떤 작업을 할지 선택한다.
# ex)
# file = open("./sample.txt")
# file = open("./sample.txt", 'w')
# file = open("./sample.txt", 'at')
# file = open("./sample.txt", 'wb')

# file = open("./ouput")
# 파일명이 하나라도 틀리면 오류가 난다.

# file = open("./output/sample.txt", 'wt')


# 2. 작업하기
#
# 1) 출력

# write() 메서드
# 인수로 건네준 문자열을 파일에 그대로 작성하는 메서드
# file.write("hello world!!\n")
# file.write("hello world!!\n")
# file.write("한글!!\n")
# 파이참내에서 메모장을 열어서 한글을 보면 한글이 깨져서 보인다
# 인코딩 형식의 문제
# 파일을 생성(open)할 때 인코딩 형식을 지정할 수 있다.

# file = open("./output/sample.txt", 'wt', encoding="utf-8")
# # encoding의 기본값은 ANSI로 되어있다.
# file.write("hello world!!\n")
# file.write("hello world!!\n")
# file.write("한글!!\n")
#
#
# # 3. 파일 닫기
# # close() 메서드를 활용해서 파일을 저장하고 닫을 수 있다.
# file.close()
#
# file.write("추가적인 데이터\n")
# file.write("추가적인 데이터")
# close() 진행했다면 추가적인 작업 메서드는 적용되지않는다!


# with 문
# with문이 시작할 때 open한 파일에 대해서 with문이 끝나면 자동으로 close()를 진행해주는 구문

# 형식
with open("./output/sample.txt" , "wt", encoding="utf-8") as file:
    file.write("with문의 코드\n")
    file.writelines(["hello", "world", "iterable", "요소 입력하기"])
    # iterable의 요소들을 입력하는 메서드.

file.write("데이터 추가")









































































