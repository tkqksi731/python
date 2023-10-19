# a = []

# for i in range(1, 100+1):
#     if i % 3 == 0:
#         a.append(i)

#         print(a)

# a = [ i for i in range(1, 100+1) if i % 2 == 0] 한줄로 만들기

# print(a)

# result = []
# for i in range(1, 1+2):
#     el = []
#     for j in range(1, 2+1):
#         el.append(j)
#     result.append(el)

# print(result)

# result = [ [ x for x in range(1, 2+1)] for i in range(2) ]

# print(result)

# exam

result = [ i for i in range(1, 100+1) if i % 3 == 0]

print(result)

a_list = [[ x for x in range(1, 3+1)] for _ in range(3) ]

print(a_list)