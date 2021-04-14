import random
n = int(input())
m = int(input())
k = int(input())



matrix1= [[random.randint(0, 20) for i in range(n)] for j in range(m)]
matrix2= [[random.randint(0, 20) for i in range(k)] for j in range(n)]
res = [[0 for x in range(k)] for y in range(m)]


print("---------------------------------------")


for i in range(m):
    for j in range(n):
        print(matrix1[i][j], end=' ')
    print()

print("---------------------------------------")

for i in range(n):
    for j in range(k):
        print(matrix2[i][j], end=' ')
    print()

print("------------------------------------")
print()


for i in range(m):
    for j in range(k):
        for h in range(n):

# resulted matrix
            res[i][j] += matrix1[i][h] * matrix2[h][j]

print (res)





