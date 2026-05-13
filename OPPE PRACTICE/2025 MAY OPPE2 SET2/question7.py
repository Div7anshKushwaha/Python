# This writes the stdin to the input file
import tempfile
import sys
_, filename = tempfile.mkstemp(prefix="case")
with open(filename, 'w') as f:
    f.write(sys.stdin.read())




# Write your code to read the file and print the result.
# use the variable filename for the name of the file.

vowels = "aeiou"
vowel_count = 0  # cumulative vowel counter

with open(filename) as f:
    lines = f.read().splitlines()

k = int(lines[0])        # first line is k
text_lines = lines[1:]   # remaining lines are text

for line in text_lines:
    new_line = ""

    for ch in line:
        if ch.lower() in vowels:
            vowel_count += 1

            # Check if this is the k-th vowel
            if vowel_count % k == 0:
                new_line += ch.upper()
            else:
                new_line += ch.lower()
        else:
            new_line += ch

    print(new_line)
