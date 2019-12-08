def test(a,b,c=33,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

A = (100,200,300,400)
B = {"name":"harry","age":28}

test(11,22,44,A,B)
print("=" * 30)
test(11,22,44,*A,**B)