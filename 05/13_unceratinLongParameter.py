def test(a,b,c=33,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

test(11,22,300,400,500)
print("="*30)
test(11,22,400,600,700,800,task=1000,finish=500)