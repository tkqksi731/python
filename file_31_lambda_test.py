# # + 1 해주는 함수
# # 3개의 값을 더해주는 함수
# # 2개의 값을 각각 제곱해서 더해주는 함수
# a = lambda x: x + 1

# print(a(3))

# b = lambda x, y, z: x + y + z

# print(b(1, 2, 3))

# c = lambda x, y: (x**2) + (y**2)

# print(c(2, 3))

# print("-"*10)

# # 1개의 숫자를 받아서 2의 배수이면 True, 아니면 False 리턴하는 함수
# # 0~n개의 정수를 받아서 다 합쳐주는 함수

# d = lambda x : True if x % 2 == 0 else False
# print(d(30))

# e = lambda *x : sum(x)
# print(e(1,2,3))


# map 함수 이용

# a = list(range(1, 10+1))

# result = []
# for el in a:
#     result.append(el+1)

# print(result)

# result = map(lambda x : x+1, a)
# print(list(result))

# 1~100이 담긴 리스트를 fizzbuzz하기
# 3의 배수이면 fizz 5의 배수이면 buzz 15의 배수이면 fizzbuzz
# b = list(range(1, 100+1))

# result = map(lambda x : "fizzbuzz" if x % 15 == 0 else
# ("fizz" if x % 3 == 0 else('buzz' if x % 5 == 0 else x)), b)

# print(list(result))

# filter

# f = list(range(1, 100+1))

# result = filter(lambda x: x > 50, f)
# result = filter(lambda x: x % 2 == 0, result)

# print(list(result))

# 1~10까지 가진 리스트에서 각 요소의 제곱을 더하세요.

from functools import reduce

g = list(range(1,10+1))

result = reduce(lambda x, y: x**2+y**2, g)

print(result)

