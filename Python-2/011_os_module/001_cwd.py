import os


# cwd = os.getcwd()

# current working directory(cwd)
# print("Current working directoryis: ", cwd)


# Changing cwd

def current_path():
    print("current working directory:")
    print(os.getcwd())
    print()


current_path()
os.chdir('../')
current_path()