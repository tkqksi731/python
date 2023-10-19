class Number(float):
    num1 = {
        0: "",
        1: "일",
        2: "이",
        3: "삼",
        4: "사",
        5: "오",
        6: "육",
        7: "칠",
        8: "팔",
        9: "구",
    }    
    num2 = [ "", "십", "백", "천", "만" ]

    def __repr__(self):
        str_num = str(self.real)
        temp = str_num.split(".")
        str_num = temp[0]
        floating_value = "" if temp[1] == "0" else "." + temp[1]

        if len(str_num) > 5:
            return str_num

        result = ""
        for i, n in enumerate(str_num):
            result += ( self.num1[int(n)] + self.num2[len(str_num) -i -1] if self.num1[int(n)] else "" )

        if not result:
            result = "영" + floating_value
        return result + floating_value

    
    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return Number(self.real + other.real)
    
    def __sub__(self, other):
        return Number(self.real - other.real)

    def __mul__(self, other):
        return Number(self.real * other.real)

    def __truediv__(self, other):
        return Number(self.real / other.real)
    