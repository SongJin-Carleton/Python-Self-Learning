#a = 200
a = [100]

def test(num):
    num += num  # in python num+=num is not equal with num = num+num, 
                # just for int value they are same
                # num = num + num ===> [100]+[100] = [100,100], now num points to
                # new list [100,100],in the global original value won't change.
                # num+=num we can treat it to change the value in the num
    print(num)

test(a)

print(a)