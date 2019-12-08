name = ["Tommy","Jimmy","Harry",100,"Cooper","Alex"]
#append()
name.append("Luca")
print(name)
#insert()
name.insert(3,"Maria")
print(name)
name2 = ["laoda","laoer","laosan","laoxiao"]
name3 = name + name2
print(name3)
#extend()
name.extend(name2)
print(name)

#pop() delete the last one 
name.pop()
print(name)
#remove() delete the ceratain one
name.remove("laoda")
print(name)
print(name[2:5])
#del
del name[2:5]
print(name)

#change
name[0] = "Erfan"
print(name)

if "Cooper" in name:
    print("We found it!")

if "Kimmy" not in name:
    print("He's not here")