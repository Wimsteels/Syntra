def exercise1():
    for i in range(2000,3200):
        if i % 3 == 0 and i % 5 != 0:
            print(i, end=',')
         
#exercise1()


def exercise2():
    array = []
    for i in range(1,21):
        x = i ** 2 
        array.append(x)
    print(array)

#exercise2()

def exercise3():

    matrix =[ [ 12 , 12 , 12 , 13 ] ,
              [ 43 , 43 , 43 , 54 ] ,
              [ 44 , 44 , 44 , 23 ] ,
              [ 99 , 34 , 12 , 12 ] ]

    sum = 0
    for i in range(len(matrix)):
        if i != 0 and i != len(matrix)-1:
            x = matrix[i][0] + matrix[i][-1]
            sum += x
        else:
            x = sum(matrix[i])
            sum += x
    print(sum)

exercise3()