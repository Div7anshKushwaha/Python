# different ways to import a library

# first way

import calendar
print(calendar.month(2020,7))      # Call functions with module name prefix
print(calendar.calendar(2007))

# second way
from calendar import*
print(calendar(2007))       # Direct call (no prefix needed)
print(calendar(2020))       # Direct call to the function calendar()
print(month(2007,1))


# third way

from calendar import month , calendar
# print(month(2012,2))
print(calendar(2012))

# fourth way
#1
from calendar import month as m
print(m(2012,2))

#2
import calendar as c
print(c.month(2012,12))