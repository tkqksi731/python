# def print_hello_world():
#     print("Hello world!")

# print_hello_world()

# def add_4(a):
#     return a + 4

# result = add_4(5) # 9

# print(result)

# def add(a, b):
#     return a + b

# result = add(5, 5)

# print(result)

# step 파라미터까지 받는 함수를 완성시켜보세요.

# def para(a, b, c):
#     print(c)

# # 앞의 첫 숫자가 위치인자 값, 2,3번째가 변이인자 위치인자는 앞에 b=1등을 할 수 없음
# test(1, 2, 3)

# # *args=패킹이라고함 원하는 숫자의 제한 없이 넣을 수 있음
# def sum_all(*args):
#     return sum(args)

# print(sum_all(1, 2, 3, 4, 5, 6))

# def print_f_name(father, mother, sister, brother):
#     print("아버지 이름은 ", father)
#     print("아머니 이름은 ", mother)
#     print("언니 이름은 ", sister)
#     print("동생 이름은 ", brother)

# print_f_name(father="홍길동", mother="김말숙", sister="하니", brother="둘리", cat="나비")


# # **kwargs=이것도 패킹 키워드 인자는 ** 넣는 갯수를 모를때 패킹을 함
# def print_f_name(**kwargs):
#     for key in kwargs:
#         print(key, "의 이름은 ", kwargs[key])

# print_f_name(father="홍길동", mother="김말숙", sister="하니", brother="둘리", cat="나비")

# likes = []

# def input_like():
#     likes = []
#     like = input(" 좋아하는걸 하나 입력하세요 ")
#     likes.append(like)
#     print(likes)

# input_like()
# input_like()
# input_like()

# 재귀함수

# 팩토리얼
# n! => n * (n-1) * (n-2) * ... * 1

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= 1
#         return result

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(5) == 1 * 2 * 3 * 4 * 5)