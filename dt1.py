import time;
from datetime import datetime  
from datetime import timedelta  

# to get current local time
localtime = time.localtime(time.time())
print("Date and time:=")

print("Local current time :", localtime)
print("Day = " + str(localtime.tm_mday))
print("Month = " + str(localtime.tm_mon))
print("Year = " + str(localtime.tm_year))
print("Hour = " + str(localtime.tm_hour))
print("Minute = " + str(localtime.tm_min))
print("Seconds = " + str(localtime.tm_sec))

# to increment Todays date by 5 days
print('Today Date: ',datetime.now().strftime('%d/%m/%Y'))
newdate = datetime.now() + timedelta(days=5)
print('After 5 Days:', newdate.strftime('%d/%m/%Y'))

newdateyear = datetime.now() + timedelta(days=365)
print('After 1 year:', newdateyear.strftime('%d/%m/%Y'))
