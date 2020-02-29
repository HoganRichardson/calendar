'''
Weeks iCal tool

Generate 'weeks' for university term (or similar), and saves `weeks.ics` file in current directory

Usage:
   ./weeks.py startyear startmonth startdate numweeks breakweek

Hogan Richardson
'''

from ics import Calendar, Event
from datetime import *
import sys

def usage():
    print("Usage: ")
    print("./weeks.py startyear startmonth startdate numweeks breakweek")
    sys.exit(1)

# Get user data
if len(sys.argv) != 6:
    usage()

start = date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
num_weeks = int(sys.argv[4])
break_week = int(sys.argv[5])
c = Calendar()

# Create calendar & events
for i in range (0, num_weeks + 1):
    if i == break_week:
        e = Event()
        e.name = "Mid Semester Break"

        begin = start + timedelta(weeks=+(i))
        e.begin = begin.strftime("%Y-%m-%d %X")

        end = begin + timedelta(days=+4)
        e.end = end.strftime("%Y-%m-%d %X")

        e.make_all_day()

        c.events.add(e)
    else:
        e = Event()
        if i > break_week:
            curr_week = i
        else:
            curr_week = i + 1

        e.name = "Week " + str(curr_week)

        begin = start + timedelta(weeks=+(i))
        e.begin = begin.strftime("%Y-%m-%d %X")

        end = begin + timedelta(days=+4)
        e.end = end.strftime("%Y-%m-%d %X")

        e.make_all_day()

        c.events.add(e)

print("==== EVENTS GENERATED ====")
print(c.events)

# Save to file
with open('weeks.ics', 'w+') as f:
    f.writelines(c)

print("==== FILE EXPORTED ====")
