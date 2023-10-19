try:
    num = input("숫자를 입력하세요: ")
    num = int(num)
    print(10 / num)

# 특정에러 ValueError, ZeroDivisionError
except (ValueError, ZeroDivisionError):
    print("숫자를 숫자키로 입력하세요.. 한글, 영어 등 사용 안됨!, 0도 안되요!")

# 대표적인 Error
# TypeError
# NameError
# ZeroDivisionError