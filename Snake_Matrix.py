n = int(input())
for i in range(0, n):
    i = i+1
    for j in range(0, n-i):
        print(end=" ")
    for j in range(0, n):
        j = j+1
        print((i*n+j-n), end=" ")
    print()
