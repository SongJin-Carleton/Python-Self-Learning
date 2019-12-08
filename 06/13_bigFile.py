f = open("original.txt","r")

print(f.readlines()) # readlines() reading whole file and return a list. 
                     # everyline is a element in the list 
                     
#print(f.readline()) # readline() reading a line and return a string
f.close()