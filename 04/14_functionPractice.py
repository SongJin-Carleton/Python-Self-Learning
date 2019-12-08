def get_3_paramaters(a,b,c):
    result = a + b + c
    print("Sum of three numbres is %d" %result)
    return result

def average_3_numbers(num1,num2,num3):
    average = get_3_paramaters(num1,num2,num3) / 3
    print("Average is %d" %average)




num1 = int(input("Please input the first number :"))
num2 = int(input("Please input the second number :"))
num3 = int(input("Please input the third number :"))
average_3_numbers(num1,num2,num3)