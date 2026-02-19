# 1. 모듈이란
# 모듈 module이란 한 마디로 파이썬 파일(.py)

# 2. 모듈 생성
# converter.py 생성

# 3. 모듈의 사용
# 반드시 같은 디렉토리에 있어야 함.
# 모듈에 저장된 함수를 사용하는 방법
# 1. 모듈 전체를 가져오는 방법
# 모듈에 저장된 모든 클래스나 함수를 사용하고자 할 때
# 예) import 모듈

# import : 외부 or 내부의 모듈을 가져온다.
import converter

miles = converter.kilometer_to_miles(150)
print(f'150km = {miles}miles')

pounds = converter.gram_to_pounds(2500)
print(f'2500gram = {pounds}pounds')

# 2. 모듈에 포함된 함수 중에서 특정 함수만 골라서 가져오는 방법
# 예) from 모듈 import 함수
# 예) from 모듈 import 함수1, 함수2
# 예) from 모듈 import * : *은 모든것을 포함

print()
from converter import kilometer_to_miles # 모듈은 가져오지 않고 특정 함수만 가져온다.

miles = kilometer_to_miles(150)
print(f'150km = {miles}miles')

from converter import * # 모듈은 가져오지 않고 모든 함수를 가져옴

pounds = gram_to_pounds(2500)
print(f'2500gram = {pounds}pounds')

# 4. 별명 사용하기
# 모듈이나 함수를 import 하는 경우에는 원래 이름 대신 별명을 지정하고 사용가능
# 모듈이나 함수의 이름이 긴 경우에 주로 짧은 별명을 지정하고 긴 본래 이름 대신 사용
# 별명을 지정할 때는 as키워드를 사용

import converter as cvt

miles = cvt.kilometer_to_miles(150)
print(f'150km = {miles}miles')

from converter import kilometer_to_miles as k_to_m # 함수에도 별명을 지정 가능
miles = k_to_m(150) # 함수 이름 대신 별명을 사용
print(f'150km={miles}')



