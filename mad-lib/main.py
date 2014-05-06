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
monsters = ['Troll', 'Ogre', 'Monstrous Donkey']

#Dictionary
new_brothers = {'new': 'John', 'old': monsters}

#Mathematical Operators
full_sail = full_sail + 2000
computer_graphics = full_sail - 1200
full_name = first_name + ' ' + last_name


if age < 20 or age > 25:
    #Assignment Operator
    age += 250

if brothers < 3:
    brothers = new_brothers['new']
else:
    brothers = new_brothers['old']

