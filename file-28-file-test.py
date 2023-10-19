# 파일을 만들어서 "Hello world!"를 10줄 써 넣으세요
# 파일을 append 모드로 열어서 "Hellp pypthon!"을 10줄 추가하세요
# 파일을 읽어 온 뒤에 파일내용에 hello world를 20번
# hello python을 10번 출력해보세요

# f = open("./hellotest.txt", "a")
# for _ in range(10):
#     f.write("Hello Python!\n")
# f.close()

# f = open("./hellotest.txt", "r")
# for _ in range(10):
#     print(f.readline())

# f.seek(0)

# print(f.read())

# f.close()

# key값이 최소 3개 이상인 dictionary를 최소 3개 포함한 리스트를
# csv파일로 만들어서 저장하는 함수를 만드세요
# 저장한 csv 파일을 불러와서 다시 dictionary로 변환하는 함수를 만드세요
import pprint

values = [{
    "이름":"홍길동",
    "나이": "25",
    "생일":"0607"
} for _ in range(3) ]

def to_csv(value):
    keys = []
    for el in value[0]:
        keys.append(el)
    #   keys = ["이름", "나이", "생일"]
    results = []
    for d in value:
        result = []
        for el in d.values():
            result.append(el)
        results.append(result)
    # result = [
    #     ["이름":"홍길동", "나이": 25, "생일":"0607"]
    #     ["이름":"홍길동", "나이": 25, "생일":"0607"]
    #     ["이름":"홍길동", "나이": 25, "생일":"0607"]
    # ]
    content = ', '.join(keys) + '\n'
    for result in results:
        content += ', '.join(result) + '\n'
    f = open("./csv_file.txt", "w")
    f.write(content)
    f.close()

to_csv(values)
