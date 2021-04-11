import random
m = int(input())
n = int(input())
k = int(input())

x = n * m
y = m * k 

matrix1= [[random.randint(0, 20) for i in range(x)] for j in range(x)]
matrix2= [[random.randint(0, 20) for i in range(y)] for j in range(y)]




for i in range(x):
    for j in range(y):
        print(matrix1[i][j], end=' ')
    print()

print("---------------------------------------")

for i in range(x):
    for j in range(y):
        print(matrix2[i][j], end=' ')
    print()

print("------------------------------------")
print()
res = [[0 for x in range(x)] for y in range(y)]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):

# resulted matrix
            res[i][j] += matrix1[i][k] * matrix2[k][j]

print (res)





