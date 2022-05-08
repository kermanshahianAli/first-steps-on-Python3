str = "Python is a programming language that lets you work quickly and integrate systems more effectively."
ban = ["python","systems","programming"]
for i in ban:
    str = str.lower().replace(i,len(i)*"*")
print(str)