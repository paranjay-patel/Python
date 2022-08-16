from ctypes.wintypes import RGB
import colorgram
import turtle as t
import random

pal = t.Turtle()
t.colormode(255)
pal.hideturtle()
pal.penup()
color_list = [(193, 164, 137), (219, 202, 180), (130, 99, 71), (35, 49, 145), (212, 192, 165), (59, 76, 156), (41, 28, 17), (17, 25, 77), (193, 220, 240), (131, 158, 192), (155, 127, 94), (88, 103, 188), (131, 181, 
158), (175, 113, 86), (19, 13, 17), (193, 230, 202), (85, 63, 36), (164, 186, 230), (119, 88, 103), (178, 144, 156)]

def drawdot():
    pal.dot(20,random.choice(color_list))
    if counter < 10 :
        pal.forward(30)
    
def move_upleft():
    pal.left(90)
    pal.forward(30)
    pal.left(90)    

def move_upright():
    pal.right(90)
    pal.penup()
    pal.forward(30)
    pal.right(90)  

for _ in range(10):
    counter = 0
    for _ in range(10):
        counter += 1
        drawdot()
    if pal.heading()==0:
        move_upleft()
    else:
        move_upright()

t.Screen().exitonclick()

 



#extract color from image
# rgb_colors = []
# colors = colorgram.extract('hirst-painting\image.png', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)