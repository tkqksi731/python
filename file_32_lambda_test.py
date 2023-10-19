# 1~10까지 가진 리스트에서 각 요소의 제곱을 더하세요.

# from functools import reduce

# g = list(range(1,10+1))

# result = reduce(lambda x, y: x**2+y**2, g)

# print(result)

# 다음 모듈의 기능을 이용하여서 함수의 실행시간을 측정하는
# 데코레이터를 만들어보세요.

from time import time

def print_start_end(func):
    def new_time(*args):
        start_time = time()
        result = func(*args)
        end_time = time()
        print("걸린 시간: ", end_time - start_time)
        return result
    return new_time


@ print_start_end
def sum_1_to_n(n):
    result = 0
    for i in range(1, n+1):
        result += 1
    return result

result = sum_1_to_n(123413)
print(result)

@print_start_end
# 가우스 방식
def gauss_sum(n):
    return (n * (n+1))/2

result = sum_1_to_n(123413)
print(result)