n = int(input("n: "))
m = int(input("m: "))
x=[]
for i in range(n):
    y=[]
    for j in range(m):
        a = float(input("a: "))
        y.append(a)
    x.append(y)

sum = 0
for i in range(len(x)):
    for j in range(len(x[0])):
        if i==j:
            sum += x[i][j]
print(sum)