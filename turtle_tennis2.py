import turtle
import random


turtle.setup(1500, 500)
wn = turtle.Screen()
tess = turtle.Turtle()
tess.shape("triangle")


def get_point(t):
    
    a= 0
    b= 0
    
    while check_win(t, a, b) == True:
        rand = random.randint(0, 1)
        t.penup()
        t.forward(25)
        t.pendown()
        score_board(t, a, b, rand)
        t.penup()
        t.forward(25)
        t.pendown()
        
        #check_win(a,b)
       
        if rand == 0:
            a += 1
            t.left(30)
            t.forward(50)
            t.stamp()
            t.penup()
            t.right(30)
            t.pendown()
            
        else:
            b += 1
            t.right(30)
            t.forward(50)
            t.stamp()
            t.penup()
            t.left(30)
            t.pendown()
     
        
            
def score_board(t, a, b, rand):
    points = ['0', '15', '30', '40']
    A = ""
    B = ""
      
    if a <= 2 or (a == 3 and b < 3):
        A = points[a]   
    else:
        A = "D"
   
    if b <= 2 or (b == 3 and a < 3):
        B = points[b] 
    else:
        B = "D"
        
    if a >= 4 and a-b >= 2:
        A = "A"
     
    if b>= 4 and b-a>= 2:
        B= "A"

    if A == "D" and B == "D":
        if a > b:
            A = "A"
        elif a < b :
            B = "A"
            
    if a >= 3 and b >= 3 and a == b:
        A = "D"
        B = "D"
       


    scoreboard = (A, B)
    t.write(scoreboard)
                      
 
        
        
def check_win(t, a, b):
   
    if a != 7 or b != 7:     
        if a == 6 and b <= 4:
            t.penup()
            t.forward(50)
            t.write("A win")
            return False
        elif a <= 4 and b == 6:
            t.penup()
            t.forward(50)
            t.write("B win")
            return False
        elif a== 3 and b== 3:
           
            return True
        else:           
            return True
    else:
       if a == 7:
           t.penup()
           t.forward(50)
           t.write("A win")
       else:
           t.penup()
           t.forward(50)
           t.write("B win")
       return False



get_point(tess)
wn.mainloop()



