# The Python documentation for the datetime module provides two 
# attributes to retrieve the year from a date or datetime object: 
#     year and isocalendar.

# Copy Code
# from datetime import date

# today = date.today()

# today_year = today.year
# iso_year = today.isocalendar()[0]
# What is the difference between the year attribute and the 
# isocalendar method?

from datetime import date
today = date.today()
# print(today)

iso_day = today.isocalendar()[2] # prints 3rd day of the week 
iso_year = today.isocalendar()[0]
print(iso_day)
print(iso_year)