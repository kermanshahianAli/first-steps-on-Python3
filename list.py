x = [10,-5,9,23,12,1]
# A
i = x.index(23)
j = x.index(12)
x[i+1:j] = ["reza"]
print(x)
x = [10,-5,9,23,12,1]
# # B
x.remove(23)
x.remove(9)
print(x)
x = [1,10,-5,1,9,23,12,1]
# # # C
n=x.count(1)
for i in range(n):
    f = x.index(1)
    x[f] = "ali"
print(x)