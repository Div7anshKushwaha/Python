# Write the whole stdin to a temporary file
import tempfile, sys
_, filename = tempfile.mkstemp(prefix="zigzag_")
with open(filename, "w") as f:
    f.write(sys.stdin.read())




# Read the file using the variable filename, and print the result in the output.


with open(filename) as f:
    lines = f.read().splitlines()

z = int(lines[0])
chars = lines[1:0]
if z == 1:
    for c in chars:
        print(c)
else:
    spaces = 0
    direction = 1


    for c in chars:
        print(" "*spaces + c)

        spaces += direction
        if spaces == z-1:
            direction = -1
        elif spaces == 0:
            direction = 1    

