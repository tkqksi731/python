# list = []쓰고
# list는 list[0] = 0을 넣으면 변경이 되지만
# tuple = () 씀
# tuple는 tuple[0] = 0을 넣으면 변경이 안 됨

# dict 만들기

# 나의 정보
my_info = {
    "나이": 24,
    "생일": "7월 6일",
    "연락처": "010-1234-1234"
}

# 가족 정보
family_info = [{
    "나이": 61,
    "생일": "5월 15일",
    "연락처": "010-4321-4321"
    },
    {
    "나이": 55,
    "생일": "3월 9일",
    "연락처": "010-5678-5678"
    },
    {
    "나이": 25,
    "생일": "3월 6일",
    "연락처": "010-7890-7890"
    }]

# keys = [key for key in family_info[0]]
# csv = keys

# for el in family_info:
#     info = []
#     for 



# 알파벳 출현 횟수
PEP_20 = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

PEP_20 = PEP_20.lower()

word = {}

for i in 










# List Compreshension

# a = [ i for i in range(1, 6+1)]
# print(a)

# b = [ 7-i for i in range(1, 6+1)]
# print(b)

# c = [[ i for i in range(1, 3+1)] for _ in range(3)]
# print(c)

# d = [[x+i for i in range(1, 3+1)] for x in range(0,8,3)]
# print(d)

