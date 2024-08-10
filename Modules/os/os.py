import os

print(os.name)

# Current working directory
cwd = os.getcwd()
print(f"Current working directory is : {cwd}")

# Change working directory
os.chdir("./..")
cwd = os.getcwd()
print(f"Current working directory is : {cwd}")

# make directory
os.mkdir("test")
if os.path.exists("test"):
    print("test directory exits")
else:
    print("test directory doesn't exits")

# remove directory
os.rmdir("test")
if os.path.exists("test"):
    print("test dir exit")
else:
    print("test directory doesn't exit")


# make directory with sub directory
## shutil can also be used to for recursive

path = "parent_dir/sub_dir"
os.makedirs(path)
if os.path.exists(path):
    print(f"{path} exits")
else:
    print(f"{path} does't exits")


# remove parent and sub directory
path = "parent_dir/sub_dir"
os.removedirs(path)
if os.path.exists(path):
    print(f"{path} exits")
else:
    print(f"{path} doesn't exits")


# remove file
file = "os-remove.txt"
path = "/home/personal/Documents/Git/Python/Modules/os/"
delete = os.path.join(path, file) 
os.remove(delete)