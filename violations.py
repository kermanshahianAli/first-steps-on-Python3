violations = {
    "g1": 10000     ,    "g2": 20000     ,    "g3": 30000,
    "b1": 50000     ,    "b2": 55000     ,    "b3": 60000,
    "y1": 100000     ,    "y2": 150000,
    "r1": 300000     ,    "r2": 400000
}
keys = list(violations.keys())
print("violations:",keys)
n = int(input("enter number of violations: "))
sum = 0
for i in range(n):
    code = input("code: ")
    sum += violations[code]
print("total penalties of violations:",sum)
# thanks for your timr ;)