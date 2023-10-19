# 경로에는 상대경로, 절대경로
# ./ 이 폴더 안에
# w, r, a

# f = open("./hello.txt", "w")
# f.write("Hello World!")

# f.close()

# f = open("./hello.txt", "a")
# for i in range(2, 10+1):
#     content = "\n" + str(i) + "번째 줄입니다."
#     f.write(content)

# f.close()

f = open("./hello.txt", "r")
content = f.read() # f.write(), f.a
print(content)
# print(f.read())

# 커서를 0번째로 옮겨줘
f.seek(0)
print(f.read())

f.close()

