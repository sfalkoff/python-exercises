#functions exercise 2
import turtle

def drawSquare(t):
    sz = 20
    for i in range(5):
        for i in range(4):
            t.forward(sz)
            t.left(90)
        sz = sz + 20
        t.penup()
        t.left(45)
        t.backward(14)
        t.right(45)
        t.pendown()
       
wn = turtle.Screen()
wn.bgcolor("lightgreen")

sara = turtle.Turtle()
sara.color("hotpink")
sara.pensize(3)

drawSquare(sara)

wn.exitonclick()


#functions exercise 16
import math

def myPi(times):
    pi = 0
    sign = 1
    n = 0
    denominator = 1 
    denominator2 = 1
    for i in range(times):
        pi = pi + (sign/(denominator * denominator2))
        sign = sign * -1
        n = n + 1
        denominator = denominator + 2 
        denominator2 = 3 ** n
        
    pi = pi * math.sqrt(12)
    return pi


print(myPi(1000))


#conditionals exercise 12
def isLeap(year):
    remainder = year % 100
    century = year - remainder
    if year % 4 == 0 and century % 400 == 0: 
        return True
    else:
        return False


#strings exercise 6 
def reverse(astring):
    '''reverse astring'''
    revString = ''
    for i in range(len(astring)-1, -1, -1):
        revString = revString + astring[i]
    return revString


#strings exercise 10
def count(substr,theStr):
    '''Count the number of instances of substr in a theStr'''
    count = 0
    if substr in theStr:
        for i in range(len(theStr)):
            if substr in theStr[i:i+len(substr)]:
                count = count + 1
        return count          
    else:
        return 0


#strings exercise 12
def remove_all(substr,theStr):
    '''Removes all instances of substr from theStr'''
    index = theStr.find(substr)
    return_str = ''
    if index < 0:
        return theStr
    while index >= 0:
        return_str = theStr[:index] + theStr[index+len(substr):]
        theStr = return_str
        index = return_str.find(substr)
    return return_str       


#lists exercise 12
def word_count(lst):
    word_count = 0
    index = 0
    while lst[index] != "sam" and index < len(lst):
        word_count = word_count + 1
        index = index + 1
    return word_count

lst = ['apple', 'sam', 'cherry', 'berry', 'sam']

print(word_count(lst))  


#lists exercise 13
def count_func(x, your_list):
    '''return the number of times x appears in the list'''
    count = 0
    for item in your_list:
        if item == x:
            count = count + 1
    return count


def in_func(x, your_list):
    '''return True if x appears in the list'''
    for item in your_list:
        if item == x:
            return True 
    return False

def reverse_func(your_list): 
    reverse_list = []
    for item in range(len(your_list)-1 , -1, -1):
        reverse_list.append(your_list[item])
    return reverse_list

def index_func(x, your_list):
    '''return the first index of item x and an error if x is not in the list'''
    for item in range(len(your_list)):
        if x == your_list[item]:
            return item
    return -1
        
def insert_func(x, y, your_list):
    '''insert x into your_list at index y'''
    your_list[y:y] = [x]
    return your_list   


#lists exercise 14
def replace(s, old, new):
    '''replaces all instances of old with new in string s'''
    index = s.find(old)
    return_str = ''
    if index < 0:
        return s
    while index >= 0:
        return_str = s[:index] + new + s[index+len(old):]
        s = return_str
        index = return_str.find(old)
    return return_str  


print(replace("hello world it is good to love", "l", "p"))


#files exercise 2:
def find_average(file):
    f = open(file, 'r')
    for aline in f:
        values = aline.split()
        sum = 0
        for value in range(1, len(values), 1):
            value_int = int(values[value])
            sum = sum + value_int
        average = sum/len(values)
        print(values[0], average)
    f.close()
              
find_average('studentdata.txt')     


#files exercise 3:
import math

def find_average(file):
    f = open(file, 'r')
    for aline in f:
        values = aline.split()
        minimum = min(values[1:])
        maximum = max(values[1:])
        print(values[0], 'min is', minimum, 'max is', maximum)
    f.close()
              
find_average('studentdata.txt')     


#files exercise 4 (unfinished):
import turtle
t = turtle.Turtle()            
wn = turtle.Screen()
wn.setworldcoordinates(-50, -50, 150, 150)
    
def plotRegression(file, turtle):
    f = open(file, 'r')
    sumX = 0
    sumY = 0
    count = 0

    for aline in f:
        values = aline.split()
        turtle.penup()
        turtle.goto(int(values[0]), int(values[1]))
        turtle.pendown()
        turtle.stamp() 
        sumX = sumX + int(values[0])
        sumY = sumY + int(values[1])
     
    count = count + 1
    meanX = sumX/count
    meanY = sumY/count
    n = count * 2 
    numerator = 0
    denominator = 0
    
    for aline in f:
        values = aline.split()
        numerator = numerator + ((int(values[0]) * int(values[1])) - (n * meanX * meanY))
        denominator = denominator + ((int(values[0])**2) - (n * (meanX**2)))
    
    m = numerator/denominator
 
    f.close() 
    wn.exitonclick()

   
plotRegression('labdata.txt', t) 
 
  
#files exercise 5:
import turtle
t = turtle.Turtle()            
wn = turtle.Screen()
wn.setworldcoordinates(-300, -300, 300, 300)
    
def mystery(file, turtle):
    f = open(file, 'r')
    for aline in f:
        values = aline.split()
        if "UP" in values:
            turtle.penup()
        elif "DOWN" in values:
            turtle.pendown()   
        else:
            turtle.goto(int(values[0]), int(values[1]))

    f.close() 
    wn.exitonclick()

   
mystery('mystery.txt', t)


#recursion self-check(1):
def reverse(s):
    if len(s) <= 1:
        return s
    else: 
        s = s[len(s) - 1:len(s)] + reverse(s[0:len(s) - 1])
    return s


#recursion self-check(2):
def reverse(s):
    if len(s) <= 1:
        return s
    else: 
        s = s[len(s) - 1:len(s)] + reverse(s[0:len(s) - 1])
    return s

def removeWhite(s):
    new_s = ''
    for ch in s:
        if ch in string.ascii_letters:
            new_s = new_s + ch  
    return new_s

def isPal(s):
    s = removeWhite(s)
    if reverse(s) == s:
        return True
    else:
        return False


#recursion self-check(3):
import turtle
import random

def tree(branchLen, pensize, t):
    if branchLen > 5:
        t.pensize(pensize)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-random.randrange(1, 20), pensize - 2, t)
        t.left(40)
        tree(branchLen-random.randrange(1, 35), pensize - 2, t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.setworldcoordinates(-400, -400, 400, 400)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75, 10, t)
    myWin.exitonclick()

main()


#lab - counting letters
def countLetters(string):
    counts = {}
    for letter in string:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] = counts[letter] + 1
    return counts

print(countLetters("banana"))


#lab - letter count histogram (still need to set up window)
import turtle

wn = turtle.Screen()
tess = turtle.Turtle()           
tess.color("lightgreen")
tess.fillcolor("blue")
tess.pensize(3)

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()    
                
def countLettersHist(string):
    counts = {}
    for letter in string:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] = counts[letter] + 1
    
    countsList = list(counts.keys())
    countsList.sort()

    for key in countsList:
        value = counts[key]
        drawBar(tess, value)             
             
countLettersHist("bananas bananas")
        

