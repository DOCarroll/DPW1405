#singe line comments!
'''
name: Daniel O'Carroll
date: 5/4/14
class: DPW1405
'''

first_name = 'Daniel '
last_name = 'OCarroll'

year_born = 1994
print 2014 - year_born

'''
if(year_born < 1990){
print 'you are part of generation y'
}
'''


'''
if year_born < 1995:
    print 'you are part of the millennial generation'
elif year_born > 1978:
    print 'you are part of generation y'
elif year_born > 1965:
    print 'you are part of generation x'
else:
    print 'these generations do not apply'
'''

#arrays
students = ['Nicole', 'Eli', 'Gabriel', 'Jordan', 'Danny']
students.append('Arturo')
students[0] = students[0].lower()
print students
punks = ['Bob', 'Dylan', 'Hemmet']

#dictionaries - associative arrays
class_info = {'students': students, 'roster count': 9, 'room': 'FS4A-107'}
print class_info

#loops
'''
for s in students:
    print s + ', you will do great in this class!'
'''
'''
for i in range(0, 5):
    print students[i]

import random

for i in range(0,10):
    print random.randrange(20)
'''

#function
'''
def calc_area(h, w):
    area = h * w
    return area

a = calc_area(20, 30)
print a
'''

#format string method
'''
user_name = "Kermit"
join_date = 2001
message = """
Welcome to our site, {user_name}!
It's great you're here! You've been with us since {join_date}
"""
message = message.format(**locals())
print message
'''

age = input('Type your age:')
print int(age) + 2