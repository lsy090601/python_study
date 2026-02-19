

# 파일 입력
# read(size) 메서드
# size 크기만큼의 데이터를 읽어오는 메서드
# 생략하면 모든 데이터를 읽어들인다.
# 읽을 내용이 없다면 ""을 반환한다.

# size
# t 모드  : 최대 문자의 수
# b 모드  : 최대 바이트의 양

# readline()
# 파일의 데이터 한 줄씩 읽어들이는 메서드

# readlines()
# 파일의 모든 데이터를 읽어서 각 라인 단위로 list에 저장해서 반환해주는 메서드


# 프로그램에서 파일을 열어도 가상의 커서가 존재한다.
# 파일을 한 번읽으면 커서는 읽은만큼 이동을 한다.
# 이어서 읽기 작업을 진행하면 커서의 위치에서부터 다시 읽기 시작한다.

# seek() 메서드
# 파일의 커서를 옮기는 메서드


# csv 파일
# 쉼표로 구분된 데이터 파일

# 장점
# 단순한 파일
# 텍스트 편집기(메모장)에서도 간단히 수정할 수 있으며 관리할 수 있다.

# 모든 데이터는 문자열데이터로 취급한다.

# csv 모듈
import csv

# reader 객체 생성
# file = open("../day13/input/13일차 수업자료/학생명단.csv")
# reader = csv.reader(file)
#
# for line in reader:
#     print(line)
# file.close()
#
#
# file = open("../day13/output/sample.csv")
# writer = csv.writer(file)
# writer.writerow(["속성1", "속성2", '속성3'])
# writer.writerow(["data1", "data2", 'data3'])
# file.close()


# DictWriter DictReader
# 속성(헤더행)이 있는 csv파일을 조금 더 편하게 다룰 수 있는 객체
# 데이터를 속성을 key값으로 한 dict데이터로 다룬다.


































































































































