f1 = open("test.py","w") #"r", reading, the file has to exist
                         #"w", writing, the file can exist or not
                         #"a", appending writing, write to end of file

print(f1)

f1.write("Hello")
f1.close()