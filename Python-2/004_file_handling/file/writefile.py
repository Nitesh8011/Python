file = open('file.txt','w')
file.write("You work in Gurugram??")

file = open('file.txt','r')
content = file.read()

print(content)
file.close()