# set1 = {1, 2, 3, 4, 4, 4, 5, 5}

# nuion 합치기
# difference set1에 없는 것을 보여줌
# intersection 공통 된 것

# set1 = ser() => class set
# ex) set3 = {} => class dict

# exam
set1 = set()
set2 = set()
set3 = set()

for set_1 in range(1, 100+1):
    if set_1 % 3 == 0:
        set1.add(set_1)
    # elif 사용시 15의 배수가 안 들어가짐
    if set_1 % 5 == 0:
        set2.add(set_1)
    if set_1 % 15 == 0:
        set3.add(set_1)

print(set1.union(set2))
print(set3.difference(set1))