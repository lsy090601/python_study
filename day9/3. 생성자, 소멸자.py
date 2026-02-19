from random import sample


# 클래스내에서 __로 시작하는 메서드들이 존재한다.
# 기본적으로 클래스가 가지고 있는 어떤 기능과 역할이 부여되어있는 메서드들이며, "매직(magic) 메서드" 또는 "특별(special) 메서드"라고한다.


# 생성자 (__init__)

# class Candy:
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def print_info(self):
#         print(f'모양 : {self.shape}, 색 : {self.color}')

# candy = Candy()
# candy.set_info("원", '초록')
# candy.print_info() # 모양 : 원, 색 : 초록
# 인스턴스의 생성과 인스턴스 변수의 생성시점이 다르니까 불편하다!

# 파이썬의 모든 클래스는 __init__이라는 이름의 메서드를 가진다.
# 이 메서드는 생성자라고 하며 생성자는 인스턴스가 생성될 때 자동으로 호출(실행)되는 메서드이다.
# 주로 인스턴스의 생성과 인스턴스 변수에 값을 저장하는 프로세스를 한번에 실행하는 메서드이다.
class Candy:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def print_info(self):
        print(f'모양 : {self.shape}, 색 : {self.color}')

# candy = Candy() # 오류 발생!
# init 메서드에서 작성한 매개변수에 필요한 인수를 전달하지않아서 오류 발생!

candy = Candy("사각형", "보라색")
candy.print_info()
# 인스턴스가 생성되면서 인스턴스 변수를 가지고 태어나게된다!

# 소멸자 (__del__)
# 인스턴스가 소멸될 때 자동으로 실행되는 메서드

class Sample:
    def __init__(self):
        print("인스턴스 생성")

    def __del__(self):
        print("인스턴스 소멸")

sample = Sample()
print("임의의 코드")
del sample
print("임의의 코드")

class Student:
    def __init__(self,name, kor, math, eng):
        self.name = name
        self.kor = kor
        self.math = math
        self.eng = eng

    def student_get_sum(self):
        return self.kor + self.math + self.eng

    def student_get_avg(self):
        return self.student_get_sum() / 3

    def student_to_string(self):
        return f'{self.name}의 점수 합계 : {self.student_get_sum()}, 평균 : {self.student_get_avg():.2f}'

students = [
    Student("홍길동", 92, 78, 86),
    Student("홍길동", 92, 78, 86),
    Student("홍길동", 92, 78, 86)
]

for student in students:
    print(student.student_to_string())







# # 시계(Watch) 클래스를 만들어봅시다
# # Watch클래스는
# # what_time() 메서드와 see() 메서드를 가지고 있습니다.
# # what_time() 메서드는 사용자로부터 시간(시:분:초 의 형식)을 입력받아
# # 인스턴스 변수 hour, minute, second에 저장합니다.
# # see() 메서드는 저장된 시간을 출력합니다.
# # ex) '저장된 시간은 --시 -- 분 --초입니다.
# '''
# watch = Watch()
### watch.what_time('17:15:2')
# watch.what_time(17,15,2)
# watch.see()
#
# [출력결과]
# 저장된 시간은 17시 15분 2초입니다.
# '''

class Watch:

    # def what_time(self, hour, minute, second):
    def what_time(self, time):
        # time_list = time.split(":")
        # # print(time_list) # ['17', '15', '2']
        #
        # self.hour = time_list[0]
        # self.minute = time_list[1]
        # self.second = time_list[2]

        self.hour, self.minute, self.second = time.split(":")


    def see(self):
        print(f'저장된 시간은 {self.hour}시 {self.minute}분 {self.second}초입니다.')

watch = Watch()
watch.what_time('17:15:2')
#### watch.what_time(17,15,2)
watch.see()




























































































































