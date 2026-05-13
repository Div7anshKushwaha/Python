'''
Write a function count_odd_three_digit_nums(nums) that takes a list of integers nums and returns the count of numbers that are:

Odd.
Three-digit numbers (ignoring the negative sign if present).
Not None.
NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Examples:
count_odd_three_digit_nums([101, -203, None, 99, 300]) → 2
Explanation: 101 and -203 are odd three-digit numbers, ignoring None.
count_odd_three_digit_nums([None, 120, 301, -401, 78]) → 2
Explanation: 301 and -401 qualify as odd three-digit numbers.
count_odd_three_digit_nums([10, 305, 507, 99]) → 2
Explanation: 305 and 507 qualify as odd three-digit numbers.
'''
def count_odd_three_digit_nums(nums):
    flag = 0
    for num in nums:
        if ((num != None) and (num%2 == 1) and (99<abs(num)<1000)):
            flag += 1
    return flag
