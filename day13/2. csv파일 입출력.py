

# csv 파일 입출력

# CSV 파일이란?
# Comma Sepparated values의 약자 --> 쉼표로 구분된 값(데이터)들
#
# 데이터 베이스(DB)나 스프레드 시트(엑셀)을 저장하기 위해 사용되는 간단한 형식의 파일
# 내부는 실제 쉼표(,)를 이용해서 모든 항목이 구분되어있으며
# 쉼표로 구분된 각 항목들이 테이블을 구성하는 각각의 데이터가 되는 방식
# 메모장에서는 텍스트로 받을 수 있고, 엑셀에서는 각 셀로 나누어서 보인다.
# ---> 메모장으로 편집할 수 있는 엑셀시트

# 한국의 전자정보 프레임워크, 데이터 파일을 지원할 때 csv를 지원한다.
# 최근에는 JSON이 증가하는 추세


# 단점
# 값에 유형이 없다. 모든 데이터는 문자열 데이터 취급한다.
# 글꼴, 글자크기, 색상 등 설정할 수 없다.
# 여러 개의 스프레드 시트를 가질 수 없다.
# 셀의 넓이나 높이를 지정할 수 없다.
# 셀 병합 등 수정할 수 없다.
# 그림이나 차트 등은 사용할 수 없다.

# 장점
# 단순하다!
# 텍스트 편집기(메모장)에서도 보고 수정할 수 있으며, 관리하기 편하다
# 많은 프로그램에서 라이브러리 지원을 한다.


# csv는 데이터가 ,로 구분되어있는 텍스트 파일이기 때문에 기본 입출력과 문자열 메서드를 활용하면 별도의 모듈없이도 사용할 수 있다.

# 한 줄에 한 개의 데이터 묶음이 있기 때문에 보통 readline()을 이용해서 한 줄 씩 데이터를 읽는다.
# , 기준으로 데이터가 구분되기때문에 split()을 이용해서 데이터를 분리한다.


# with open("./input/13일차 수업자료/학생명단.csv" , 'rt') as file:
#     student_list = []
#
#     while True:
#         line = file.readline()
#         # print(line, end="")
#         if not line:
#             break
#         student = line.split(",")
#         # print(student)
#         student_list.append(student)
#
# print(student_list)
#
# for stu in student_list:
#     print(stu)
#     print(stu[0])


# ""를 없애기 위해
# strip(): 문자열의 양끝에서부터 내가 지정한 문자를 제거하는 메서드#
# 를 사용한다.


# with open("./input/13일차 수업자료/회원명단.csv" , 'rt') as file:
#     member_list = []
#     while True:
#         line = file.readline()
#         # print(line, end="")
#         if not line:
#             break
#         member = line.split(",")
#         # print(member)
#         member[0] = member[0].strip('"') # 데이터를 감싼 "제거
#         print(member)
#         member_list.append(member)
# print(member_list)

# 이런방식들로 내장모듈없이도 메서드를 이용해서 csv 파일을 사용할 수 있다


# 내장 모듈

# csv 모듈을 사용한다.
import csv

# 읽기
# reader 객체를 생성한다.
# csv.reader(파일객체)를 이용해서 reader객체를 생성할 수 있다.

# with open('./input/13일차 수업자료/학생명단.csv') as file:
#     reader = csv.reader(file) # file객체 기반의 reader가 생성된다.
#     print(reader) # <_csv.reader object at 0x000002D93B6730A0>
#     # __str__이 구현되지않아 객체 기본 출력
#     # data = list(reader)
#     # print(data)
#     # for line in data:
#     #     print(line)
#
#     for row in reader:
#         print(row)
#         print(f'Row : {reader.line_num} {row}')
#         print(f'{row[0]}')


# 쓰기
# write 객체 생성

# with open('./output/sample.csv', "w") as file:
#     writer = csv.writer(file)
#
#     writer.writerow(["apple", 'banana', "orange"])
#     writer.writerow(["apple2", 'banana2', "orange2"])

# 키워드 인자 delimeter (구분자), linetermenator(끝 맺음자)
# 구분자의 기본값은 ,이고, 끝맺음자의 기본값은 \n이다.
# writer, reader 객체 생성할 때 인자를 지정해서 값을 바꿀 수 있다.

# with open('./output/sample.tsv', "w") as file:
#     # tsv -> tab으로 데이터를 구분하는 파일
#     writer = csv.writer(file, delimiter="\t", lineterminator="\n")
#     writer.writerow(["apple", 'banana', "orange"])
#     writer.writerow(["apple2", 'banana2', "orange2"])


# quotechar
# 데이터에 구분자가 포함되어있을 때 데이터를 나누지 않고 묶어주는 역할을 하는 문자
# 기본값 "이 지정되어있다.

# with open('./output/sample.csv', "w") as file:
#     # writer = csv.writer(file, quotechar="~")
#     writer = csv.writer(file)
#     writer.writerow(["apple", 'banana', "orange", "2026-02-13, 11:07"])
#     writer.writerow(["apple2", 'banana2', "orange2", "2026-02-13, 11:07"])


# csv의 dictReder, dictWriter
# 헤더 행(속성 명)이 있는 CSV파일을 다룰 때 편한 객체

# DictWriter
# with open("./output/sample.csv", "w") as file:
#     dict_writer = csv.DictWriter(file, ["Name", "Age", "Pet"])
#     # 해더 행의 정보를 객체를 생성할 때 iterable의 데이터 형식으로 전달한다.
#     dict_writer.writeheader()
#     # 생성할 때 전달한 헤더행을 만드는 메서드
#     # 생성하지않는다면 전달한 헤더행은 파일을 닫을 때까지 내부적으로 키값으로만 사용하게 된다.
#
#     dict_writer.writerow({"Name" : "Alice", "Age" : 25, "Pet": "cat"})
#     dict_writer.writerow({"Name" : "Alice", "Pet": "cat", "Age" : 25})
#     dict_writer.writerow({"Name" : "Alice", "Pet": "cat"})
#     # 딕셔너리 데이터로 입력을 하기 때문에 데이터가 키값을 따라 입력된다.
#     # --> 데이터의 입력순서를 바꾸어도 상관이없다.
#     # 누락된 키값에 대응되는 데이터는 빈문자열이 자동으로 입력


# DictReader
# with open("./output/sample.csv", "rt") as file:
#     dict_reader = csv.DictReader(file)
#     for row in dict_reader:
#         # print(row)
#         print(row["Name"])
#         print(row.get("Age"))



# 다음은 지시사항에 따라 서울 특별시 마포구에 설치된 CCTV의 개수를 구하는 프로그램을 구현하세요

# 지시사항
# 1. cctv.csv 파일을 읽습니다.
# 2. 모든 라인에 존재하는 카메라 개수를 합한 결과를 출력합니다.

# 실행 예 :
# 서울특별시 마포구에 설치된 cctv는 총  2167대 입니다.


with open("./input/13일차 수업자료/cctv.csv", 'rt') as file:

    count = 0
    # reader 풀이
    # file.readline() # 커서를 헤더행 뒤로 옮기는 작업
    # reader = csv.reader(file)
    # for row in reader:
    #     count += int(row[4])
    # print(f"서울특별시 마포구에 설치된 cctv는 총  {count}대 입니다.")


    # DictReader
    # reader = csv.DictReader(file)
    # for row in reader:
    #     count += int(row["카메라대수"])
    # print(f"서울특별시 마포구에 설치된 cctv는 총  {count}대 입니다.")

    # 기본 입출력 사용
    line = file.readline() # 헤더행 제거
    while True:
        line = file.readline()
        if not line:
            break
        camera = line.split(',')
        count += int(camera[4])
    print(f"서울특별시 마포구에 설치된 cctv는 총  {count}대 입니다.")































































