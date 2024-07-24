# Using the datetime module in Python, how would you obtain 
# the current date and time?

import datetime

print(datetime.datetime.now())

# OR

from datetime import datetime

current_datetime = datetime.now()
print(current_datetime)