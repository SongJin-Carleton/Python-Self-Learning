a = [11,22,33]
b = [44,55]
c = ["aa","bb","cc"]

a.extend(b) #extend paramater just for list
print(a)

a.append(c)#append treat paramater as a whole one paramater
print(a)
a.append("vvv")
print(a)