num = int(input('0~9까지 숫자를 하나 입력하세요'))

if num > 8:
    print("입력하신 값이 8보다 큽니다.")
elif num > 5:
    print("입력하신 값이 8보다 같거나 작고, 5보다는 큽니다.")
elif num > 2:
    print("입력하신 값이 5보다 같거나 작고, 2보다는 큽니다.")
else:
    print("입력하신 값이 2보다 같거나 작습니다.")