r = [  [ [[],[],[]] , [[],[],[],[]] , [[],[]] ]  ,
    [ [[],[],[]] , [[],[],[],[]] , [[],[]] ]  ,
   [ [[],[],[]] , [[],[],[],[]] , [[],[]] ]  ]
n=0
#limit = 3*3*27*30 = 7290
while n<7290:
    room_class = input("Enter the room class[A-B-C]: ").lower()
    while room_class!="a" and room_class!="b" and room_class!="c" :
        room_class = input("invalid entery..." + '\n' + "enter room class[A-B-C]: ").lower()
    room_class_id=-1 
    if room_class=="a":
        room_class_id = 0
    if room_class=="b":
        room_class_id = 1
    if room_class=="c":
        room_class_id = 2
    room_size = int(input("How many beds[1-3]: "))
    while room_size!=1 and room_size!=2 and room_size!=3 :
        room_size = int(input("out of range..." + '\n' + "how many beds[1-3]: "))
    room_size -= 1
    for i in r[room_class_id][room_size]:
        print(i)
    first_day = int(input("Enter the date of the first day[1-30]: "))
    while first_day<1 or 30<first_day:
        first_day = int(input("invalid date..."+ '\n' +"Enter the date of the first day[1-30]: "))
    last_day = int(input("Enter the date of the last day[1-30]: "))
    while last_day<1 or 30<last_day:
        last_day = int(input("invalid date..."+ '\n' +"Enter the date of the last day[1-30]: "))
    if last_day<first_day:
        temp = first_day
        first_day = last_day
        last_day = temp
    days = []
    flag=0
    sign=0
    for i in range(first_day,last_day+1):
        days.append(i)
    for i in r[room_class_id][room_size]:
        for k in i:
            if first_day<=k<=last_day:
                sign=1
                break
        if sign==1:
            sign=0
            continue
        print("please enter your information : ")
        fname = input("first name: ")
        lname = input("last name: ")
        for m in days:
            i.append(m)
        print("the room is your's",fname,lname,"  in  ",first_day,"-",last_day)
        flag =1
        break
    if flag==0:
        print("we do not have rooms in the date and class you want..."+'\n'+"try again")
    else:
        n += len(days)
    # thanks for your time ;)