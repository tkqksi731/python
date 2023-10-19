from random import choice

raw_list = list(range(-50, 50+1))

target = []
for _ in range(100):
    target.append(choice(raw_list))

print(target)

def selection_sort(A):
    result = []
    while len(A) != 0:
        max_num = A[0]
        for i in A:
            if max_num < i:
                max_num = i
        result.append(max_num)
        A.remove(max_num)
    return result

print(selection_sort(target))