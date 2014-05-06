'''
name: Daniel O'Carroll
date: 5/4/14
class: DPW1405
'''

#String User Inputs
first_name = raw_input('Enter your first name: ')
last_name = raw_input('Enter your last name: ')
gender = raw_input('Enter your gender (M or F): ')

#Number User Inputs
age = input('Enter your age: ')
brothers = input('How many brothers do you have?(Enter a number): ')
full_sail = input('How many years have you been at Full Sail?(Enter a number): ')

#Array
monsters = ['Troll', 'an Ogre', 'and a Monstrous Donkey']
john_dave = ['John', 'and Dave']

#Dictionary
new_brothers = {'new': john_dave, 'old': monsters}

#Mathematical Operators
full_sail = full_sail + 2000
full_name = first_name + ' ' + last_name

def print_monsters(b):
    for i in b:
        print i

if gender == "M":
    suffix = "Sir"
else:
    suffix = "Lady"
if age < 20 or age > 25:
    #Assignment Operator
    age += 250
    part1 = """
    Hello, {suffix} {full_name},
    You spent most of your life at Full Sail, you are now {age}!
    """
    part1 = part1.format(**locals())
elif age > 20 or age < 25:
    part1 = """
    Hello, {suffix} {full_name},
    You picked a good time to come to Full Sail, you're so young!
    """
    part1 = part1.format(**locals())
if brothers < 3:
    brothers = new_brothers['new']
    part2 = """
    All the brothers you grew up with died, now you are left with your new brothers
    """
    part2 = part2.format(**locals())

else:
    brothers = new_brothers['old']
    part2 = """
    Some of your brothers died, or were turned into monsters. Now your brothers are a
    """

#Creating a function that will return a value

def computer(full):
    full = full - 1200
    full /= 3
    return full
computer_graphics = computer(full_sail)

part3 = """
You're doomed to stay at Full Sail for {full_sail} years!
{computer_graphics} years will be spent in Advanced Computer Graphics!
"""
part3 = part3.format(**locals())

def story(age_part, brothers_part, full_sail_part):
    print age_part
    print full_sail_part
    print brothers_part




story(part1, part2, part3)
print_monsters(brothers)

