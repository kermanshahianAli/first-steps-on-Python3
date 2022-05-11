# Caesar code
text = input("enter your text: ")
code=""
for i in text:
    t = ord(i)+80
    code += chr(t)
print(code)
