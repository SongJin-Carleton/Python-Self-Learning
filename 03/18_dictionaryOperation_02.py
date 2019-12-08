info = {"name":"aaa","age":22}


#keys()
print(info.keys())

if "name" in info.keys():
    print("Yes")
else:
    print("No")

#vaules()
print(info.values())

#items()
print(info.items())
for item in info.items():
    #print("Key = %s, value = %s" %(item[0],item[1]))
    temp1,temp2 = item
    print(("%s,%s") %(temp1,temp2))
