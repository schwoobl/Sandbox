def test():
    value1 = 0
    value2 = 0
    value3 = 0
    print(value1,value2,value3)

    value1 += 1
    value2 += 2
    value3 += 3
    print(value1,value2,value3)

    return value1, value2, value3 

var1, var2, var3 = test()
print(var1, var2, var3)

