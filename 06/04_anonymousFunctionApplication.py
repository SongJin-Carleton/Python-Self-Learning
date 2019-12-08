def test(a,b,func):
    result = func(a,b)
    return result

#func_python2 = input("Please input a Anonymous Function :") #used for python2 

func_python3 = input("Please input a Anonymous Function :") #used for python3
func_python3 = eval(func_python3)  #used for python3,eval() change string to real function


num = test(11,22,func_python3) #Anonymous Function as a real parameters
print(num)