# Author: Cesaire Tchoudjuen
# Program that outputs whether or not today is a weekday

import datetime

#from datetime import date
my_date = date.today()
#week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',  'Friday', 'Saturday', 'Sunday']

#import pandas as pd
#df = pd.Timestamp(my_date)
#print(df.dayofweek, df.weekday_name)


x = datetime.datetime(my_date)
print(x.strftime("%B"))
