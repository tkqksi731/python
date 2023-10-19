
csv_values = """
이름, 연락처, 나이, 이메일
철수, 010-1234-1234, 23, chuls@gmail.com
영희, 010-4321-4321, 30, 0h@gmail.com
"""

# strip은 원하는 것을 빼는 것
csv_values = csv_values.strip("\n")
# split은 원하는 기준을 나누는 것
csv_list = csv_values.split("\n")

keys = []

for el in csv_list[0].split(','):
    keys.append(el.strip(' '))

results = []
for val in csv_list[1:]:
    result_dict = {}
    i = 0
    for el in val.split(','):
        result_dict[keys[i]] = el.strip(' ')
        i += 1
    results.append(result_dict)

print(results)