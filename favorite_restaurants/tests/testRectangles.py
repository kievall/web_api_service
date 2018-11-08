'''
Function checking if rectangles overlap.
x1: Top Left coordinate of first rectangle.
y1: Bottom Right coordinate of first rectangle.
x2: Top Left coordinate of second rectangle.
y2: Bottom Right coordinate of second rectangle.
'''

def verifyOverlap(x1,y1,x2,y2):
   if x1>y2 or x2>y1:
       return False
   elif x1<y2 or x2<y1:
       return False
   else:
       return True

''' Test Examples '''

x1 = {0,10}
y1 = {10,0}
x2 = {10,10}
y2 = {20,10}
if verifyOverlap(x1,y1,x2,y2):
    print("Overlaped")
else:
    print("Not Overlap")

x1 = {10,0}
y1 = {0,10}
x2 = {4,8}
y2 = {12,6}
if verifyOverlap(x1,y1,x2,y2):
    print("Overlaped")
else:
    print("Not Overlap")
