
def exercise1():
    array2D = [[1,2,3],[4,5]]
    sum = 0
    for i in array2D:
        for k in i:
            sum += k
    print (sum)

exercise1()    

def exercise2():
    array = []
    for i in range(1,21):
        x = i ** 2 
        array.append(x)
    print(array)

exercise2()

def exercise3(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(exercise3(2, 3, 4))

import operator
def exercise4(array1, array2):
    c = list(map(operator.add, array1,array2))
    print(c)

a = [1, 2, 3]
b = [4, 5, 6]
exercise4(a,b)

def exercise5(array):
    tuple = ()
    for i in array:
        for k in i:
            if k % 3 == 0:
                tuple.append[k]
    index = tuple.index(k)
    print(index)

    
array = [[1, 3, 1, 1, 4],
         [2, 4, 3, 1, 2],
         [3, 5, 4, 1, 1],
         [4, 6, 2, 1, 4]]

exercise5()