# MILES, POUND는 단위 변환에서 사용하는 변수

MILES = 0.621371
POUND = 0.002205


def kilometer_to_miles(kilometer):  # 인수로 들어온 수를 매개변수를 통해 킬로미터를 마일로 변환
    return kilometer * MILES


def gram_to_pounds(gram):  # 그램을 파운드로 변환하는 함수
    return gram * POUND
