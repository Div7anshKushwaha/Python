'''Append and Prepend Alternatively
Given a sequence of n strings as input, create a final word by appending and prepending the strings alternately based on their order. Strings at even indices (0-based) are appended to the end, while strings at odd indices are prepended to the beginning.

NOTE: This is an I/O type question, you need to write the whole code for taking input and printing the output.

Input Format

The fist line consists of the number of strings n.
Next n lines consists of the strings to append and prepend.
Output Format

The output string.
Examples

Input 1

6
h
t
o
y
n
p
Output 1

python
Explanation

Append 'h' -> h
Prepend 't' -> th
Append 'o' -> tho
Prepend 'y' -> ytho
Append 'n' -> ython
Prepend 'p' -> python'''

n = int(input().strip())

result = ""

for i in range(n):
    s = input().strip()
    if i%2 == 0:
        result = result + s
    else:
        result = s + result

print(result)







