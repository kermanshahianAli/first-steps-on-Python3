from math import * 

print("In this program we want to calculate the solution(s) of this equation (ax**2 + bx + c)")
print("please enter the Coefficients :")

a = float(input("a = "))
while(a==0):
    print("Coefficient of a couldn't be 0 ")
    a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = (b**2) - (4*a*c)
if 0<delta :
    x1 = ( (-b) + sqrt(delta) ) / (2*a)
    x2 = ( (-b) - sqrt(delta) ) / (2*a)
    print("equation has 2 solutions : " , x1 , " and " , x2 )

elif delta==0 :
    x = (-1*b) / (2*a)
    print("equation has 1 solution : " , x)

elif delta<0 :
    print("This equation has no answer.")

# thanks for your time ;)