# i = 1

# result = 1

# while i <= 5:
#     result *= i
#     i += 1

# print(result)

def getNum(a):
    if a > 1:
        return a * getNum(a-1)
    else:
        return a

# def infinity(para):
#     if para == 1:
#         return 1
#     else:
#         return para * infinity(para - 1)

#print(infinity(4))

print(getNum(5))


