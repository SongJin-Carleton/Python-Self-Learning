old_file_name = input("Please input which file you want to copy :")

position = old_file_name.rfind(".")
new_file_name = old_file_name[:position] + "[Copy]" + old_file_name[position:]

f = open(old_file_name,"r")
f1 = open(new_file_name,"w")

while True:
    content = f.read(1024)
    if len(content) == 0:
        break
    else:
        f1.write(content)
        

print(content)
f.close()
f1.close()



 