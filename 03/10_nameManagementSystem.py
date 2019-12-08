print("=" * 50)
print("    Name Management System")
print("1. Add a new name")
print("2. Delete a name")
print("3. Change a name")
print("4. Look for a name")
print("5. Exit System")
print("=" * 50)


names = [];


while True:

    num = input("PLease input a number :")
    num = int(num)

    if num == 1:
        new_name = input("Please input a new name :")
        names.append(new_name)
        print(names)
    elif num == 2:
        pass
    elif num == 3:
        pass
    elif num == 4:
        find_name = input("Please input a name which your are looking for :")
        if find_name in names:
            print("Yes,it's in the list")
        else:
            print("Sorry, it's not in the list!")
    elif num == 5:
        break 
    else:
        print("Please input a number between 1 and 4")