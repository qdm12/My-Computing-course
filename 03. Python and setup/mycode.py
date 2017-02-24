from datetime import datetime

name = raw_input("Hello ! Please enter your name: ")
birth_date = raw_input("Enter your birth date in the format dd/mm/yyyy: ")

print
print "Hello "+name+"! I'm calculating your age, 1 second..."
today_object = datetime.today()
today_year = today_object.year
today_month = today_object.month
today_day = today_object.day

birth_year = int(birth_date[6:10])
birth_month = int(birth_date[3:5])
birth_day = int(birth_date[0:2])
#int() converts the 'text' (string) to an integer

age_year = today_year - birth_year
age_month = today_month - birth_month
age_day = today_day - birth_day

age_float = age_year + float(age_month)/12 + float(age_day)/365
#float() converts to a floating point number. It is necessary to floating point divisions !
print "You are "+str(age_float)+" years old"
#str() converts to 'text' (string)
