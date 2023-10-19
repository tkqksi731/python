# 사전 만들기
my_info = {
    "이름": "NamHoSeok",
    "나이" : 24,
    "연락처" : "010-1234-1234"
}

# 추가하기
my_info["email"] = "tkqksi731@gmail.com"

# items는 key와 values의 값을 다 보여줌
# key 값은 이름 등등
# values 값은 내 이름 등등
for el in my_info:
    print(el, end=" : ")
    print(my_info[el])