file = open('file.txt','a')
file.write("\nYes, I work as DevOps Engineer")

file = open('file.txt','r')
content = file.read()

print(content)
file.close()