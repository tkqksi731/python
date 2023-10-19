import operator as op

try:
    from models import operators
except ImportError:
    operators = None

try:
    from models import Number
except ImportError:
    Number = None
    
default_operators = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.truediv
    }
    
operators = operators if operators else default_operators
num_format = Number if Number else float

def select_operator():
    print("계산한 연산을 선택해주세요.")
    for i, op in enumerate(operators):
        print("{simbol} 연산".format(
            simbol=op,
        ))
    try:
        op = operators[input('연산자 입력 : ')]
    except KeyError:
        print("연산자를 바르게 입력해주세요")
        return select_operator()
    return op


def select_number(n):
    print("계산할 {n}번째 숫자를 선택해주세요.".format(n=n))
    number = num_format(input('숫자입력 : '))
    return number


if __name__=='__main__':
    print("지정 표현 맞춤형 계산기 프로그램 작동!")
    while True:
        print("종료는 Ctrl + c")
        try:
            op = select_operator()
            num1 = select_number(1)
            num2 = select_number(2)
        except KeyboardInterrupt:
            break
        print('연산 결과는 {}입니다. '.format(op(num1, num2)))