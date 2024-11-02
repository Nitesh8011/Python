import os
import os.path
import shutil

# os.mkdir('folder2')
# a = os.listdir('.')
# print(a)


# x = os.path.exists('folder1')
# print('Path exits:',x)

# os.rmdir('folder1')
# a = os.listdir('.')
# print(a)

shutil.rmtree('folder1')
a = os.listdir('.')
print(a)