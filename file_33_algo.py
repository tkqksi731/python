from random import choice

# raw_list = list(range(0, 100+1))

# target = []
# for _ in range(100):
#     target.append(choice(raw_list))

# print(target)

# def selection_sort(A):
#     result = []
#     while len(A) != 0:
#         min_num = 100
#         for i in A:
#             if min_num > i:
#                 min_num = i
#         result.append(min_num)
#         A.remove(min_num)
#     return result

# print(selection_sort(target))

raw = [0, 1]

target = []
for _ in range(1000):
    target.append(choice(raw))

def solution(A):
    length = len(A)
    sum_1 = sum(A)
    string_value = "0" * (length - sum_1) + "1" * sum_1
    return list(map(int, list(string_value)))

print(solution(target))