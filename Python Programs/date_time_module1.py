'''26/02/2021'''
'MODULES'#packages 
#import is used to call module
#module can be caled a library but not a header

import datetime as dt
x=dt.datetime.now()

# print("Full Version", "(", x, ")")
# print("Day", "(", x.weekday(), ")", "start with monday and monday is 0")
# print("Current Date", x.date())
# print("Current Time", x.time())
# print("Full Day", x.strftime("(%A)"), "Short Day", x.stfrtime("(%a)"))
# print("Weekday", x.strftime("(%w)")
# print("Date", x.strftime("(%d)")
# print("Short Month", x.strftime("(%b)", "Long Month", x.strftime("(%B)")
# print("Month", x.strftime("(%m)")
# print("Without Century", x.strftime("(%y)", "With Century", x.strftime("(%Y)")
# print("Hours 24", x.strftime("(%H)", "Hours 12", x.strftime("(%I)")
# print("Show AM & PM", x.strftime("(%p)")
# print("Minutes", x.strftime("(%M)")
# print("Second", x.strftime("(%S)")
# print("Day out of year", x.strftime("(%j)")
# print("Week in Year", x.strftime("(%U)")
# print("Local Version both", x.strftime("(%c)")
# print("Local Version date", x.strftime("(%x)")
# print("Local Version time", x.strftime("(%X)")
# print(x.today())
# print(x.minute)
# print()


'''Check if time right now is even or not''' 
x.strftime(" %M ")
if (int(x.strftime)%2==0):
    print("even")
else:
    print("Odd")