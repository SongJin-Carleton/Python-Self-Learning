# nums = [11,22,33,44]

# for item in nums:
#     print(item)
#     break
# else:
#     print("=" * 10)

cards_info = [{"name":"aaa","Tel":111,"age":11},
              {"name":"bbb","Tel":222,"age":22},
              {"name":"ccc","Tel":333,"age":33}]

find_name = input("Please input a name: ")

for item in cards_info:
    if find_name == item["name"]:
        print("We find it")
        break
else:
    print("It's not here")