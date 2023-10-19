import operator

def shap(x, y):
    return x + y + 100

def custom_sub(x, y):
    return x - y + (y + x) # (2 * x)


operators = {
    "+" : operator.add,
    "-" : custom_sub,
    "*" : operator.mul,
    "/" : operator.truediv,
    "#" : shap
}