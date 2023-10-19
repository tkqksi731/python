# 어떤 문자값을 받아 뒤에 느낌표가 오게 만들기
# def add(a):
#     return a + "!"

# print(add("python"))

# 1~9까지 숫자를 하나 선택하세요.
# 선택한 숫자에 2를 곱하세요.
# 5를 더하세요.
# 결과에 50을 곱하세요.
# 1769를 더한 다음.
# 그리고 자신이 태어난 년도를 빼세요.

# def cho_num():
#     number = input("1~9까지 숫자를 하나 선택하세요 ")
#     return int(number)

# def multi2(number):
#     return number * 2

# def add5(number):
#     return number + 5

# def multi50(number):
#     return number * 50

# def add1769(number):
#     return number + 1769

# def birth_year(number):
#     return number - 1995

# number = cho_num()
# number = multi2(number)
# number = add5(number)
# number = multi50(number)
# number = add1769(number)
# number = birth_year(number)
# print(number)


# 재귀함수
 # 정수 a와 n을 받아서 a에 n을 더하는 함수를
 # 재귀함수로 만들어보세요

def sum_fa(a, n):
    if n == 0:
        return a
    return 1 + sum_fa(a, n-1)

print(sum_fa(110, 7))

