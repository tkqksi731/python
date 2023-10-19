# exam

for i in range(1, 1000+1):
    key = True
    for j in range(2, i):
        if i % j == 0:
            key = False
            break
    #실행

    if key:
        print(i)
