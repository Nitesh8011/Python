import re

# ^ means starts with a && $ means end with e
pattern = '^a...e$'
test_string = 'abyse'
result = re.match(pattern, test_string)

if result:
    print("Search successfully")
else:
    print("Unsuccessful")


# https://www.programiz.com/python-programming/regex
