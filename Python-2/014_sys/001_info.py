import sys

arg1=sys.argv[0]
arg2=sys.argv[1:]

print("Script name: ",arg1)
print(arg2)


if len(arg2) > 1:
    print("Number of args is more than 1")
    sys.exit()
else:
    print(arg2)