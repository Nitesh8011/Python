# sys.stdin: Standard input
# sys.stdout: Standard output
# sys.stderr: Standard error

import sys

# Save the original standard output
original_stdout = sys.stdout

# Redirect standard output to a file
with open('output.txt', 'w') as f:
    sys.stdout = f
    print("This will be written to the file.")

# Restore the original standard output
sys.stdout = original_stdout
print("This will be printed on the console.")