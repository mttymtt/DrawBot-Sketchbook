# Dynamically fetch date and time
# Source: https://learnandlearn.com/python-programming/python-reference/python-get-current-date
    
    
import datetime
 
# getting current date and time
d = datetime.datetime.today()
print('Current date and time: ', d)
 
# getting current year
print('Current year: ', d.year)
 
#getting current month
print('Current month: ', d.month)
 
#getting current day
print('Current day: ', d.day)
 
# getting current hour
print('Current hour: ', d.hour)
 
# getting current minutes
print('Current minutes: ', d.minute)
 
# getting current Seconds
print('Current seconds: ', d.second)
 
# getting current microsecond
print('Current micro seconds: ', d.microsecond)

# /end example

# rolling my own: current date (YYYY-MM-DD)
print(d.strftime('%Y-%m-%d'))

# current military time (HH:MM) 
print(d.strftime('%H:%M'))