me = { 'name': 'Yujin', 'birth': '0301', 'phone': '010-4399-0000' }
dad = {'name': 'Hantae', 'birth': '0409', 'phone': '010-3271-0000' }
mom = {'name': 'Hyanwoo', 'birth': '0813', 'phone': '010-4199-0000' }

family = [dad,mom,me]

for el in family:
    print(el)
#--------------------------------------------------------------------    
    
#문제4. csv 만들기
#Familly변수에 들어가 있는 list정보를 csv형태로 출력하세요.

csv = "이름, 생일, 전화번호\n"

for el in family:
    for el2 in el:
        csv += el[el2] + ", "
    csv = csv.strip(", ")
    csv += "\n"

print(csv)
#--------------