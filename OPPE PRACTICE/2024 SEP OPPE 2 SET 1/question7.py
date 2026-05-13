import tempfile
import sys

# This writes the stdin to the input file
_ , filename = tempfile.mkstemp(prefix="case")
with open(filename, 'w') as f:
    f.write(sys.stdin.read())

# Write your code to read the file and print the result.
with open(filename) as f:
    # preserves line structure without trailing '\n'
    lines = f.read().splitlines()   

# Define vowels (Checking lower allows us to handle Upper case logic dynamically)
vowels = "aeiou"
vowel_count = 0   

for line in lines:
    new_line = [] # Using a list is generally more efficient for string building
    for ch in line:
        # Check lower case version to catch 'A', 'E', etc.
        if ch.lower() in vowels:
            vowel_count += 1
            
            # Determine prefix based on odd/even count
            prefix = "ub" if vowel_count % 2 == 1 else "dub"
            
            # Add prefix + original character
            new_line.append(prefix + ch)
        else:
            new_line.append(ch)
            
    # Join the list back into a string and print
    print("".join(new_line))