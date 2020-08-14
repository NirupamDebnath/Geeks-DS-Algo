# iterative solution
# def len_integer(num):
#     i = 0
#     while (num != 0):
#         num = num // 10
#         i += 1
#     return i

# recursive solution
# def len_integer(num):
#     if num == 0:
#         return 0
#     return 1 + len_integer(num // 10)


# Logarithmic solution
from math import floor, log10
def len_integer(num):
    return floor(log10(num) + 1)

print(len_integer(12345))
