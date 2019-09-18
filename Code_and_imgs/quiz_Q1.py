#Ryan Rusli - 2201832446
#Quiz Question 1

#----------------------
import matplotlib.pyplot as plt
import csv
import sys

from datetime import datetime
from datetime import date


filename = 'quiz_activity.csv'


def addsteps(row,total_steps):      #function to check for unavailable days and add the steps
    try:
        total_steps += int(row[0])
    except ValueError:
        print("Data for this day unavailable.")
        sys.exit()
    return total_steps



user_date = input("Input Date (YYYY-MM-DD): ")
user_date = datetime.strptime(user_date,"%Y-%m-%d")

with open(filename) as f:
    reader = csv.reader(f)
    nextcol = next(reader)

    intervals,steps = [],[]
    total_hour_steps = 0
    hour = ''

    for row in reader:
        current_date = datetime.strptime(row[1],"%Y-%m-%d")
        if current_date  == user_date:
            if len(str(row[2])) <= 2:   #if the time is 12 am and 12.55 am
                total_hour_steps = addsteps(row,total_hour_steps)
                if 0 not in intervals:
                    intervals.append(0)
                total_hour_steps = int(row[0])

            elif len(str(row[2])) == 3: #if the time is between 1 am and 9.55 am
                x = str(row[2])
                if x[0] != hour:
                    hour = x[0]
                    steps.append(total_hour_steps)
                    if int(hour) not in intervals:
                        intervals.append(int(hour))
                    total_hour_steps = int(row[0])
                elif x[0] == hour:
                    total_hour_steps = addsteps(row,total_hour_steps)

            elif len(str(row[2])) == 4: # if the time is between 10 am and 11.55 pm
                x = str(row[2])
                if x[0:2] != hour:
                    hour = x[0:2]
                    steps.append(total_hour_steps)
                    if int(hour) not in intervals:
                        intervals.append(int(hour))
                    total_hour_steps = int(row[0])
                elif x[0:2] == hour:
                    total_hour_steps = addsteps(row,total_hour_steps)

            if len(steps) == 23 and len(intervals) == 24:
                steps.append(total_hour_steps)

plt.bar(intervals,steps,width = 1)

plt.title("Hourly Steps Taken",fontsize = 16)
plt.xlabel("Intervals",fontsize = 12)
plt.ylabel("Total Steps Taken",fontsize = 8)
plt.tick_params(labelsize = 6)



plt.show()


                
                    
                
                

            
        

    
    
    
