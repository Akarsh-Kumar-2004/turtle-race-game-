import turtle
import random
screen = turtle.Screen()
screen.setup(width= 1200,height=700)
screen.bgcolor("black")
screen.title("TURTLE RACE")


color = ["violet","indigo","blue","green","yellow",'orange',"red"]
positions = [-300,-200,-100,0,100,200,300]
turtle_list = []
for i in range(7):
    tiny_turtle = turtle.Turtle(shape = "turtle")
    tiny_turtle.speed(7)
    tiny_turtle.color(color[i])
    tiny_turtle.penup()
    tiny_turtle.goto(x = -550,y=positions[i])
    tiny_turtle.pendown()
    turtle_list.append(tiny_turtle)



user_input = screen.textinput(title = "MAKE YOUR BET",prompt="choose the colour of the turtle !!")
print(f"you chose {user_input} color ")
input_check_flag = False
if user_input in color:
    input_check_flag = True
while input_check_flag:
    for t in turtle_list:
        
        if t.xcor()<560:
            
            distance = random.randint(0,10)
            t.forward(distance)
        else:
            
            winning_turtle = t.pencolor()
            input_check_flag = False
            if user_input==winning_turtle:
                print("you won !!!")
            else:
                print("YOU LOST ")
    
    




screen.exitonclick()