# Author: Cesaire Tchoudjuen
# Program that outputs whether or not today is a weekday

import datetime

week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',  'Friday'] # We define the list of week days
weekend_days = ['Saturday', 'Sunday'] # List of weekend days
x = datetime.datetime.now() # variable assigned to an object returning the current date and time
today = x.strftime("%A") # The current date and time format is changed to only return the current day of the week


if today in week_days: # we check if the current day of the week is included in the week days
    print("Yes, unfortunately today is a weekday.")
else: # we check if the current day of the week is included in the weekend days
    print('It is the weekend, yay!')

