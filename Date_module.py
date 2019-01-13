#Python Dates
#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

#Example
#Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
print(x)
x = datetime.datetime(2020, 5, 17)
#The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone)
#but they are optional, and has a default value of 0, (None for timezone).
print(x)
