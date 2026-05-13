# This writes the stdin to the input file
import tempfile
import sys
_, filename = tempfile.mkstemp(prefix="case")
with open(filename, 'w') as f:
  f.write(sys.stdin.read())



suffixes = [
    'wards', 'ations', 'ation', 'tions', 'tion', 'asions', 
    'asion', 'sions', 'sion', 'ment', 'ness', 'ship', 
    'hood', 'able', 'ible', 'less', 'ward', 'wise', 'ion', 'ity', 'age',
    'ize', 'ise', 'ify', 'ate', 'ful', 'ous', 'ish', 'ive', 'ing', 'ers', 'er',
    'or', 'ty', 'en', 'ic', 'al', 'ly'
]

# Write your code to read the file, process it, and print the result.
# Use the variable filename for the name of the file.


# # This writes the stdin to the input file
# Read the file properly
with open(filename) as f:
    lines = f.read().splitlines()

# Process each line
for line in lines:
    words = line.split()
    output_words = []

    for word in words:
        stem = word

        for suf in suffixes:  
            if word.endswith(suf):
                stem = word[:-len(suf)]
                break  # stop after first matching suffix

        output_words.append(stem)

    print(" ".join(output_words))