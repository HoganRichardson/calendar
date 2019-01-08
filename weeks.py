'''
Weeks iCal tool

Generate 'weeks' for university term (or similar), and saves `weeks.ics` file in current directory

Usage:
   ./weeks.py startyear startmonth startdate numweeks

Hogan Richardson
'''

from ics import Calendar, Event
from datetime import *
import sys

def usage():
    print("Usage: ")
    print("./weeks.py startyear startmonth startdate numweeks")
    sys.exit(1)

# Get user data
if len(sys.argv) != 5:
    usage()

start = date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
num_weeks = int(sys.argv[4])
c = Calendar()

# Create calendar & events
for i in range (0, num_weeks):
    e = Event()
    e.name = "Week " + str(i + 1)

    begin = start + timedelta(weeks=+(i))
    e.begin = begin.strftime("%Y%m%d %X")

    end = begin + timedelta(days=+5)
    e.end = end.strftime("%Y%m%d %X")

    e.make_all_day()

    c.events.add(e)

print("==== EVENTS GENERATED ====")
print(c.events)

# Save to file
with open('weeks.ics', 'w+') as f:
    f.writelines(c)

print("==== FILE EXPORTED ====")
