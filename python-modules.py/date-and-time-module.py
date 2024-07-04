# 1) import module
# to import whole module simply 
import file2 as renamedFile
print("Data From File2: ",renamedFile.user())
# specific part 
from file2 import user;


# 2)time module(builtin module)
import time
print(time.time())
# sleep is used to stop program execution for some time
time.sleep(1)
print("sleep ended")


# 3) dateTime module
import datetime
current_time=str(datetime.datetime.now())
print(current_time)

formationDate=current_time.split(" ")
print(formationDate)
currentDate=formationDate[0]
formatedDate=datetime.datetime.strptime(currentDate,"%Y-%m-%d")
print("formated Date:",formatedDate)
# only date
onlyDate=datetime.date.today()
print(onlyDate)
# only time
onlyTime=datetime.time(hour=12,minute=30,second=21)
print(onlyTime)

#CALCULATING SECONDS TILL 3 DAYS
duration=datetime.timedelta(hours=23,days=7) 
total=duration.total_seconds()
print(total)