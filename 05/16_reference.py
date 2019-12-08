a = 100
b = a
c = 500

A = [100,200,300]
B = A
A.append(1000)



print(id(a))
print(id(b))
print(id(c))
print("=" * 30)
print(A)
print(B)
print(id(A))
print(id(B))
