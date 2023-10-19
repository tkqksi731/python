class Wallet:
    money = 0

    def __init__(self, name):
        self.owner = name

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