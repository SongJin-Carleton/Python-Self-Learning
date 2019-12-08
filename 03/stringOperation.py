name = "Hello Python \tWunderful Python \tWorld"
#looking for from left
print(name.find("Python"))
print(name.find("Dajngo"))
#looing for from right
print(name.rfind("Python"))
print(name.rfind("Dajngo"))
#looking for index
print(name.index("Python"))
#print(name.index("Dajngo"))
#counting number of words appeared in sentence
print(name.count("Python"))
#replace word
print(name.replace("Python","Java"))
print(name.replace("Python","Java",1))
#cutting
print(name.split(" "))
#Start/End with
print(name.startswith("Hello"))
print(name.endswith("Java"))
print(name.lower())
print(name.upper())
print(name.partition("Wunderful"))
print(name.rpartition("Python"))
print(name.isalpha())
print(name.split(" "))
answer = name.split()
print(answer)
print(" ".join(answer))
print("".join(answer))