x = ("reza","mahsa",12,3,4,9,"neda")
y = (125,12,1,0,"sasan","reza")
x = set(x)
y = set(y)
a1 = x.intersection(y) # or we can use x & y
a2 = x.difference(y)
a3 = y.difference(x)
print("inter section:",a1 , '\n' 
        "difference between x and y:",a2,'\n' 
            "difference between y and x:",a3)
# thanks for your time ;)