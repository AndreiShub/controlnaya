def addition(num):
    while len(str(num)) > 1:
        num = str(num)
        print(num)
        new_num = 0
        for i in list(num):
            new_num += int(i)
        num = new_num
    return num

print(addition(38))