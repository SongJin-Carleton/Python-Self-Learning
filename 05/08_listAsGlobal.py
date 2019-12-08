nums = [11,22,33]
info = {"name":"Harry"}

def test():
    nums.append(44)
    info["age"] = 18

def test2():
    print(nums)
    print(info)

test()
test2()
# when list and dictionary as gloabl variables, we don't need add "global" in the function.