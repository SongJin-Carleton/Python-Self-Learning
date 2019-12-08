print("=" * 50)
print("          Business Card Management SYstem")
print("1. Add a new Business Card")
print("2. Delet a Business Card")
print("3. Modify a Business Card")
print("4. Look for a Buiness Card")
print("5. Exit System")
print("=" * 50)


collections = []

while True:
    
    num = int(input("Please input a number :"))
    find_flag = 0 #indicate whether we find the person

    if num == 1:
        name = input("Please input a name :")
        address = input("Please input your address :")
        age = int(input("Please input your age :"))
        new_Card = {"name":name,"address":address,"age":age}
        collections.append(new_Card)
        print(collections)
    elif num == 2:
        print("2")
    elif num == 3:
        print("3")
    elif num == 4:
        find_name = input("Please input a name :")
        for item in collections:
            if find_name == item["name"]:
                find_flag = 1
                print("Yes,he's here")
                break
        if(find_flag == 0):  
            print("He's not here")
    elif num == 5:
        break
    else:
        print("Please input a number between 1 and 5")