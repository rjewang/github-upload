# import graphics
from graphics import *

# ask for user input
length = int(input("Enter window length: "))
spacing = int(input("Enter shape spacing: "))

# Create graphics window titled 'Love' of size by user input
win = GraphWin('Love', length, length)

#Define a as the same width of circle, triangle and square
#Define b as horizontal spacing and c as vertical spacing
a = (length - 7 * spacing ) / 7
b = spacing
c = (length - 2 * a) / 2

#Define 'L', yellow rectangle based on corner points
A = Point(2 * b, c )
B = Point(2 * b + a, c + 2 * a )
R = Rectangle(A,B)

#Set 'L' color
R.setOutline('Yellow')
R.setFill('Yellow')
R.draw(win)

#Define 'O', red circle based on central point and radius
C = Point(3 * b + 2 * a, c + a)
Y = Circle(C, a)

#Set 'O' color
Y.setOutline('red')
Y.setFill('red')
Y.draw(win)

#Define 'V', green triangle based on corner points
P1 = Point(4 * a + 4 * b, c + 2 * a)
P2 = Point(3 * a + 4 * b, c)
P3 = Point(5 * a + 4 * b, c)
T = Triangle(P1, P2, P3)

#Set 'V' color
T.setOutline('Green')
T.setFill('Green')
T.draw(win)

#Define 'E', blue rectangle based on corner points
G = Point(length - 2 * a - 2 * b, c)
H = Point(length - 2 * b, c + 2 * a)
R1 = Rectangle(G,H)

#Set 'E' color
R1.setOutline('Blue')
R1.setFill('Blue')
R1.draw(win)

# Close after mouse click
try:
    win.getMouse()    
    win.close()
except:
    pass