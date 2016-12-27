import time

message = "Hello "
name = "Denisa"
print message + name

#Your birthday date
birthday_day = 2
birthday_month = 12
birthday_year = 1993

#Gets the current date
present_day = int(time.strftime("%d"))
present_month = int(time.strftime("%m"))
present_year = int(time.strftime("%Y"))
#int() converts the 'text' (string) to an integer

age = present_year - birthday_year
age = age + float(present_month - birthday_month)/12
#we use float otherwise 5/2 = 2 and not 2.5
age += float(present_day - birthday_day)/365
# += is a shortcut for age = age + ..
print "You are " + str(age) + " years old :P" 