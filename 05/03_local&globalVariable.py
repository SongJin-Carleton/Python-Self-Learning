# def get_temperature():
#     temp = 33
#     return temp

# def print_temp():
#     print("Temp is %d " %get_temperature())

# print_temp()

temp = 0

def get_temp():
    global temp
    temp = 33

def print_wendu():
    print("Temp is %d" %temp)

get_temp()
print_wendu()
