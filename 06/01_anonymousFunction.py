nums = [1122,12,3,12,31,100,50,23,1,34134,250,332211]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)

info = [{"name":"kelvin","age":18},{"name":"Harry","age":8},{"name":"Charli","age":20}]
info.sort(key=lambda x:x['name'])#Anonymous Function
print(info)
info.sort(key=lambda x:x['age'])#Anonymous Function
print(info)
