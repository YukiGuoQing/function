# def num_user(num1, num2 , num3):
#     print("num1 =", num1)
#     print("num2 =", num2)
#     print("num3 =", num3)
#     return num1 + num2 + num3
#
# print(num_user(1, 3, 4))

# def print_greeting():
    # return "hello"

# print(print_greeting())

# def sum(num_1=0,num_2, num_3):
#     return num_1 + num_2 + num_3
# print(sum(1, 2))

def sqaure(val):
    """
    Square the value.
    """
    val = val * val
    print(val)
    return val


num = 6
num = sqaure(num)
print(num)

help(sqaure)