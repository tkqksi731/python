number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#10을 추가
number.append(10)
print(number)

print(number[0:1])
print(number[9:10])
print(number[0:3])

#부분 숫자 보이게 하기
print(number[0:2] + number[-2:])

#순서 반전
number.reverse()
print(number)

#짝수만 나오게 하는법
print(number[::2])