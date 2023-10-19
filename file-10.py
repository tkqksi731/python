import random

num = random.randint(1, 100)
 
number = int(input("예상 숫자를 입력하세요. "))

print(abs(num - number))

if abs(num - number) > 0 and abs(num - number) <= 10:
    print("아깝네요.")
elif abs(num - number) >= 10:
    print("틀렸습니다.")
else:
    print("정답")
