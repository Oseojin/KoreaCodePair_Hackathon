#import calendar as cal
#cal.prcal(2022)

#from calendar import prcal
#prcal(2022)

import datetime
t = datetime.datetime.today()
delta_time = datetime.timedelta(days=3)
result = t - delta_time
print(result.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))