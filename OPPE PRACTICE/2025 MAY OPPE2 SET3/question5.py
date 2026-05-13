'''Remainder Grouping Dictionary
Write a Python program that reads two inputs from the user:

A single line containing a list of integers separated by commas. The line may contain arbitrary spaces around the commas.
An integer k - the divisor.
Your task is to build a dictionary that groups the numbers by their remainder when divided by k.

Each key is a remainder r (0<=r<k) that actually appears among the given numbers.
The value for a key r is a list of all numbers whose remainder equals r, sorted in ascending order.
Print the dictionary in ascending order of the keys using the following format (one key per line) with values in ascending order.:

key1 - val1,val2,...
key2 - val1,val2,...
...
There must be no extra spaces around the dash or the commas.'''




nums = [int(x) for x in input().replace(" ", "").split(",")]
k = int(input())

groups = {}

for n in nums:
    r = n % k
    groups.setdefault(r, []).append(n)

for r in sorted(groups):
    print(f"{r} - {','.join(map(str, groups[r]))}")


