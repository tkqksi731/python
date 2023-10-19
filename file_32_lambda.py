# reduce

# from functools import reduce

# a = list(range(1, 10+1))

# result = reduce(lambda x, y: x+y, a)

# print(result)

def make_print_start_end(func):
    def new_func(*args, **kwargs):
        print("함수가 시작됩니다.")
        result = func(*args, **kwargs)
        print("함수가 끝났습니다.")
        return result
    return new_func

# decorator 기능
@make_print_start_end
def print_a_to_b(a, b, c):
    for i in range(a, b+1, c):
        if i < b:
            print(i, end=", ")
        else:
            print(i)

# new_func = make_print_start_end(print_a_to_b)
# new_func(1, 100, 2)
print_a_to_b(1, 100, 2)

@make_print_start_end
def sum_a_to_b(a, b):
    result = 0
    for i in range(a, b+1):
        result += i
    return result

result = sum_a_to_b(1, 100)
print(result)
# new_func2 = make_print_start_end(sum_a_to_b)
# print(new_func2(1, 10+1))