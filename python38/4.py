# New date and datetime constructors are added for “fromisocalendar”
# source: https://bugs.python.org/issue36004?source=post_page---------------------------

from datetime import datetime

# New date and datetime constructors have been added to return the ISO calendar object:
x = datetime.fromisocalendar(2019, 12, 6)
print(x)

# This is the inverse of the function: datetime.isocalendar().
# Essentially, it takes in the year, week and day and returns
# the corresponding ISO calendar date-time object.

