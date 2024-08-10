# Open Module

# Read File
file = open('/home/personal/Documents/Git/Python/Modules/file.txt', 'r')
print(file.read())


# Write File
file = open('/home/personal/Documents/Git/Python/Modules/file.txt', 'w')
file.write("Thanks")
file.close()


# Append File
file = open('/home/personal/Documents/Git/Python/Modules/file.txt', 'a')
file.write("\nThis is for testing.\nThe open module function")
file.close()