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

#Dictionary
new_brothers = {'new': 'John', 'old': monsters}

#Mathematical Operators
full_sail = full_sail + 2000
computer_graphics = full_sail - 1200
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
else:
    part1 = """
    Hello, {suffix} {full_name},
    You picked a good time to come to Full Sail!
    """
if brothers < 3:
    brothers = new_brothers['new']
    part2 = """
    All the brothers you grew up with died, now you are left with your new brother {brothers}.
    """
    part2 = part2.format(**locals())
    print_monsters(brothers)
else:
    brothers = new_brothers['old']
    part2 = """
    Some of your brothers died, or were turned into monsters. Now your brothers are a
    """

def story(age_part, brothers_part):
    print age_part
    print brothers_part



story(part1, part2)


