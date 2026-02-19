

# 파일 입력

# 1. 작업할 파일지정
# file = open('../day12/output/sample.txt')
file = open('../day12/output/sample.txt', 'rt', encoding="utf-8")
# 생성했을 때 지정한 인코딩 방식과 읽어들일 때의 인코딩 형식이 같아야한다.


# 1) read() 메서드
# 형식
# file객체.read(size)

# 파일 객체로부터 데이터를 읽어오는 메서드
# 입력한 size만큼의 데이터를 읽어온다.
# size를 생략하면 파일 전체의 데이터를 읽는다.
# 파일을 읽을 때 남은 데이터가 없다면 빈 문자열("")을반환한다.

# size
# 텍스트 모드    : 읽어들일 최대 문자의 개수
# 바이너리 모드   : 읽어들일 최대 바이트의 양

# print(file.read())
# print(file.read(4))
# print(file.read(10))

# read()를 사용하면 읽어오는 데이터 크기만큼의 메모리 공간이 필요하다!
# 읽어들일 파일의 크다면 파일의 일부를 읽어들이는 작업을 반복해서 파일 전체를 읽도록 구현하는 것이 좋다.
# buff = 5
# with open('../day12/output/sample.txt', encoding="utf-8") as file :
#     text = file.read(buff)
#     count = 1
#     while text != "": # --> while not text == "" --> while not text
#         print(text, end="")
#         text = file.read(buff)
#         count += 1
#     print(f'\n파일을 읽기위해 반복 실행할 횟수 {count}')



# 2) readline() 메서드
# 파일의 데이터를 읽을 때 한 줄의 데이터씩 읽어들이는 메서드

# with open('../day12/output/sample.txt', encoding="utf-8") as file :
#     text = file.readline()
#     count = 1
#     while text != "":
#         print(text, end="")
#         text = file.readline()
#         count += 1
#     print(f'\n파일을 읽기위해 반복 실행할 횟수 {count}')


# 3) readlines() 메서드
# 파일 전체를 읽어서 각 라인(한 줄) 단위로 list의 요소로 저장해서 리스트를 반환하는 메서드

# with open('../day12/output/sample.txt', encoding="utf-8") as file :
#     text = file.readlines()
#     print(text) # ['with문의 코드\n', 'helloworlditerable요소 입력하기']
#
#     # for row in text:
#     #     print(row, end="")
#
#     print(file.read())
#     print(f'file.read() : {file.read()}') # 빈 문자열이 출력된다.

    # 프로그램으로 파일을 열었어도 가상의 커서가 존재한다.
    # 파일을 한번 읽어들이면 가상의 커서도 읽어들인만큼 이동을한다.
    # open한 파일에서 작업을 하면 그 가상의 커서위치에서부터 작업을 시작한다.

# 파일의 가상의 커서를 옮기는 메서드 seek()

# 형식
# 파일객체.seek(size, 기준점)

# size
# 기준점에서 커서를 움직일 크기

# 기준점
# 0 : 파일의 시작점
# 1 : 현재 위치하는 가상의 커서 위치
# 2 : 파일의 맨 끝으로 커서를 이동

# with open('../day12/output/sample.txt', encoding="utf-8") as file :
#     text = file.readlines()
#     print(text) # ['with문의 코드\n', 'helloworlditerable요소 입력하기']
#
#     # for row in text:
#     #     print(row, end="")
#
#     print(file.read())
#     print(f'file.read() : {file.read()}') # 빈 문자열이 출력된다.
#
#     file.seek(0,0)
#     print(file.read())
#
#     file.seek(3, 0)
#     print(file.read())



# 파일 복사해보기
# 복사할 파일을 binary형식으로 파일을 읽어서 그 파일을 그대로 다른경로, 다른이름으로 출력하면 그게 복사가 된다!

buffer_size = 1024  # 한 번에 읽어들일 바이트 양(1Kb)

# 1. 복사할 파일 열기
with open('./input/images.jpg', 'rb') as source:
    # 2. 복사본을 출력할(저장할) 파일 경로 지정
    with open('./output/copy.jpg', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer: # != ""
            # 읽어들인 데이터가 ""이면 while문을 끝내라!
            # ---> 복사가 끝났다
                break
            copy.write(buffer)
            # 읽어들인 데이터를 그대로 출력한다.
print("복사가 완료되었습니다.")



# 동요 '엄마돼지 아기돼지'의 가사가 저장되어 있는 '엄마돼지아기돼지.txt' 파일을 읽어서 '꿀' 이라는 글자가 몇 번 나오는지 찾는 프로그램을 만들어보자
# 인코딩 형식은 utf-8로 지정해서 읽어들인다!

# [출력 결과]
# 꿀단어가 몇 번 나오는 지 출력해주세요
# 50개

with open("./input/엄마돼지아기돼지.txt", "rt" , encoding="utf-8") as file:
    count = 0

    # 반복문
    # while True:
    #     string = file.read(1)
    #     if not string:
    #         break
    #     if string == "꿀":
    #         count += 1
    # print(f"꿀은 총 {count}개 이다")

    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     for string in line:
    #         if string == "꿀":
    #             count += 1
    # print(f"꿀은 총 {count}개 이다")

    # count() --> 문자열에서 내가 찾는 문자열이 몇번 나오는지 알려주는 메서드

    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     count += line.count("꿀")
    # print(f"꿀은 총 {count}개 이다")

    # print(f"꿀은 총 {file.read().count("꿀")}개 이다")









































