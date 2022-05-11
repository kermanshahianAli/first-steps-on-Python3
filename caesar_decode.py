# Caesar decoder
text = input("enter your text: ")
decode=""
for i in text:
    t = ord(i)-80
    decode += chr(t)
print(decode)
