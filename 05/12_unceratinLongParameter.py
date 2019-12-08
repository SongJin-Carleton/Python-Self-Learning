def sum2nums(a,b,*args):
    # print(a)
    # print(b)
    # print(args)
    # result = a + b
    # print("result = %d" %result)
    result = a + b
    for num in args:
        result += num
    print("result = %d" %result)
    

sum2nums(100,200,300,400,500,600)
sum2nums(11,22,33)
sum2nums(11,22)
