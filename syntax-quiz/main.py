'''
Name:Danny O'Carroll
Class:DPW1405
Date:Wednesday, May 7th, 2014
'''

height = input("Enter a height: ")
width = input("Enter a width: ")

def calc_area(h, w):
    area = h * w
    if h == w:
        print "The area of your square is " + str(int(area))
    else:
        print "The area of your rectangle is " + str(int(area))

calc_area(height, width)


bottles = input("Enter a number of bottles: ")
def count_down(b):
   for i in range(b, 0, -1):
       print str(int(b)) + " Bottles of Beer on the Wall, " + str(int(b)) + " Bottles of Beer.. take one down and pass it around. Now you have " + str(int(b)) + " bottles of beer on the wall!"
       b -= 1

count_down(bottles)