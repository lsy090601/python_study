

# 정적 메서드 (static method)
# 정적 --> 변화가 없다.

# 클래스에 소속되어있는 메서드지만, 인스턴스 또는 클래스에 영향을 주지않고, 영향을 받지않는 메서드이다.
# ---> 클래스에서 self, cls를 모두 사용하지않는 메서드
# --------> 일반함수와 동일하다

# 특징
# 인스턴스 또는 클래스에서 호출이 가능하다.
# ==> 클래스에서 호출해서 사용한다.
# ----> 인스턴스 없이 사용이 가능하다!
# 반드시 작성하는 매개변수가 없다.
# @staticmethod를 작성한다.

# 인스턴스 또는 클래스의 데이터에 상관없이 결과만 구할 때 사용하는 메서드
# ------> 일반함수와 동일한 효과를 가진 메서드

# 일반함수와 동일한데 왜 굳이 클래스에 넣어서 정적 메서드로

def sum(*num):
    result = 0
    for i in num:
        result += i
    return result



def devide(*num):
    result = num[0]
    for index, data in enumerate:
        if not index:
            result /= data
    return result


# 이런 식으로 비슷한 류의 여러 함수들을 따로 관리하고 사용하는 것보다
# 하나의 이름 (클래스)으로 묶어두고 사용하거나 관리하기 위해 만드는 메서드


class Calculator:

    @staticmethod
    def sum(*num):
        result = 0
        for i in num:
            result += i
        return result

    @staticmethod
    def devide(*num):
        result = num[0]
        for index, data in enumerate(num):
            if not index:
                result /= data
        return result




Calculator.sum()
# 비슷한 류의 메서드 관리하기도 편하고
# 정확한 메서드명을 몰라도 클래스명만 알고있다면 찾아서 사용하기도 편하다!






































