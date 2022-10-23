import operator
def exercise1(a, b):
    array3 = list(map(operator.add, a, b))
    print(array3)

a = [1, 2, 3]
b = [4, 5, 6]
#exercise1(a,b)

def exercise2():
    n = 5
    for i in range(n):
        for j in range(i):
            print("*", end='')
        print('')

    for i in range(n,0,-1):
        for j in range(i):
            print('*', end='')
        print('')
    
#exercise2()

def exercise3():
    array = []
    for i in range(5,8):
        Sarray = []
        for j in range(3):
            Sarray.append(i)
        array.append(Sarray)
    print(array)

#exercise3() 

def exercise4(array):
    NewArray = []
    for i in range(1, len(array)):
        for k in range(len(array[i])-1):
            if array[i][k] == "x":
                if array[i-1][k+1] == 1:
                    NewArray.append((i,k))
    print(NewArray)

array = [[1,  0,   1,  1,  0 ],
         [0, "x", "x", 0,  0 ],
         [1,  0,   1,  1, "x"],
         [0, "x",  0,  1,  0 ]]

#exercise4(array)

def exercise1(matrix):
    sum = 0
    for i in matrix:
        for j in i:
            sum += j
    print(sum)


matrix = [[11,12,13],
          [14,15,16],
          [17,18,19]]

#exercise1(matrix)

def exercise2(myList):
    print("myList heeft lengte", len(myList))
    for i in range(0, len(myList)):
        print("element met index", i, ":", myList[i])


myList = [3, 12, "pizza", 3, 4]
#exercise2(myList)

def exercise3(array):
    Newarray = []
    for i in array:
        Sarray = []
        if (isinstance(i, int)):
            for k in range(3):
                Sarray.append(i)
        if (isinstance(i, str)):
            for k in range(2):
                Sarray.append(i)
        Newarray.append(Sarray)
    print(Newarray)
    
a = [12, 43, "Y", 44, "X"]
#exercise3(a)

def exercise4(array):
    NewArray = []
    for i in range(len(array[0])):
        sum = 0
        for k in array:
            sum += k[i]
        NewArray.append(sum)
    print(NewArray)


array = [[1, 3, 1, 1, 4],
         [2, 4, 3, 1, 2],
         [3, 5, 4, 1, 1],
         [4, 6, 2, 1, 4]]
        
exercise4(array)

