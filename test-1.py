# 거짓을 의미하는 표현식 10개
a = bool(0==True)
b = bool(1 < 0)
c = bool(1 == 0)
d = bool(2 <= 0)
e = bool(1 != 1)
f = bool(2 > 3)
g = bool(4 == 5)
h = bool(not 3)
i = bool(4 >= 6)
j = bool(1 == False)

# 참을 의미하는 표현식 10개
k = bool(1 == True)
l = bool(0 < 1)
m = bool(1 == 1)
n = bool(0 <= 2)
o = bool(1 != 0)
p = bool(3 > 2)
q = bool(5 == 5)
r = bool(0 <= 1)
s = bool(6 >= 4)
t = bool(0 ==  False)

# all(), any()
all_listf = [a, b, c, d]
all_listt = [k, l, m ,n]
all_ftmix = [a, k, b, l]

print(all(all_listf))
print(all(all_listt))
print(all(all_ftmix))

# all([])은 all(x)은 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴한다. and 개념

print(any(all_listf))
print(any(all_listt))
print(any(all_ftmix))

# any([])은 any(x)는 x 중 하나라도 참이 있을 경우 True를 리턴하고, x가 모두 거짓일 경우에만 False를 리턴한다.
# all(x)의 반대 경우라고 할 수 있다. or 개념

word = input("원하는 단어를 적어보세요. ")

reverse = ""

for a in word:
    reverse = a + reverse

print(reverse)

word = input("원하는 단어를 적어보세요. ")

pal = True
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        pal = False
        break

print(pal)
