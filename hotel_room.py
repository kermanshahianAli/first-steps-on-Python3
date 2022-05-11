def check_out(d,h):
    if d<1 or 30<d:
        print("invalid date; please enter again[1-30]: ")
        while(d<1 or 30<d):
            d=int(input("date: "))
    if h<9 or 20<h:
        print("invalid date; please enter again[9-20]: ")
        while(h<9 or 20<h):
            h = int(input("hour: "))
    return (d,h)

def check_in(d,h):
        print("the time you selected was reserved . . ." + '\n' + "please enter another time: ")
        print(r)
        d = int(input("date: "))
        h = int(input("hour: "))
        return (d,h)
r = []
n = 0
while n<361:
    print(r)
    d = int(input("enter date [1-30]: "))
    h = int(input("enter hour [9-20]: "))
    c = check_out(d,h)
    while(True):
        if c in r:
            c=check_in(d,h)
        if c not in r:
            print("please enter your information: ")
            fname = input("first name: ")
            lname = input("last name: ")
            pnumber = input("phone number: ")
            r.append(c)
            print(fname,lname,"date:",d,"hour:",h,"phone number:",pnumber)
            break
    n += 1