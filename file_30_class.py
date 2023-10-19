# MY_MONEY = [0]

# def spend(m):
#     if MY_MONEY[0] > m:
#         MY_MONEY[0] -= m
#         print("{}를 사용했습니다. 남은 잔액 : {}".format(m, MY_MONEY[0]))
#     else:
#         print("가지고 있는 돈이 부족합니다.")

# def income(m):
#     MY_MONEY[0] += m
#     print("{}를 벌었습니다. 남은 잔액 : {}".format(m, MY_MONEY[0]))

# wallet = {
#     "money": MY_MONEY,
#     "spend": spend,
#     "income": income
# }

class Wallet:
    money = 0

    def __init__(self, name):
        print("{}님 환영합니다.".format(name))
        self.owner = name

    def __str__(self):
        return "{}의 지갑입니다.".format(self.owner)

    def __repr__(self):
        return "{}의 지갑입니다.".format(self.owner)

    def print_owner_name(self):
        print("owner name is", self.owner)

    def print_now_money(self):
        print("현재 잔액은 : ", self.money)

    # 쓰는돈 w.spend()
    def spend(self, m):
        if self.money < m:
            print("돈이 부족 합니다.")
            self.print_now_money()
        else:
            self.money -= m
            print("{}를 지출했습니다.", format(m))
            self.print_owner_name()

    # 들어오는 돈 w.income()
    def income(self, m):
        self.money += m
        self.print_now_money()


# 생성하는 법
# sol_wallet = Wallet("sol")
# suzy_wallet = Wallet("suzy")

# sol_wallet.print_owner_name()

# 현재 나의 돈
# swl_w.money

# 부모 속성을 상속을 함
# class ChildWallet(Wallet):
#     pass

class Account(Wallet):
    def __init__(self, name, account_number):
        self.account_number = account_number
        super().__init__(name)
    
    def __str__(self):
        return "{}의 계좌입니다. 계좌번호는 : {}".format(self.owner, self.account_number)

    def __repr(self):
        return "{}의 계좌입니다. 계좌번호는 : {}".format(self.owner, self.account_number)

    def __add__(self, another):
        return self.money + another.money

    def awns_money(self, money, to):
        if self.money > money:
            to.money += money

    def send_money(self, money, to):
        if self.money > money:
            to.money += money
            self.money -= money
            print("{}원을 {}에게 보냈습니다.".format(money, to.owner))
            self.print_now_money()