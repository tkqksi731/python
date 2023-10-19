# 정답지
import random

num = random.randint(1, 100)
 
number = input("예상 숫자를 입력하세요. ")
number = int(number)

if abs(num - number) <= 10:
    print("아깝네요.")
elif number != num:
    print("틀렸습니다.")
else:
    print("정답")
