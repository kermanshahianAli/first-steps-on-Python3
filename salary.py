h = float(input("working hour(s) : "))
range = [0,0]

if h<=160 :
    range[0] = h
elif 160<h:
    range[0] = 160
    range[1] = h-160
elif 200<h :
    range[0] = 160
    range[1] = 40

salary = range[0]*100 + range[1]*50
print("salary : "+ str(salary) + "T")
# thanks for your time ;)

