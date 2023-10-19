# exam
import random

n = random.randint(1, 100)


while True:
    guess = int(input("1~100까지의 정수를 하나 입력하세요. "))
    if n == guess:
        print("정답입니다.")
        break
    elif abs(n - guess) < 10:
        print("아깝습니다.")
    else:
        print("틀렸습니다.")