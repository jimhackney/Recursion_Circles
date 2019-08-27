import turtle

def main():
    RADIUS = 500 #Radius of the outer circle      
    LENGTH = RADIUS #the length of the line from the center
    LINE_NUM = 4 #the number of lines to make
    DEGREES = 0 #Direction of line from center in degrees
                #(0 = positive horizontal)
    
    turtle.bgcolor('black') #set background color
    turtle.color('yellow') #set line color
    
    #Call concentric_circles function
    concentric_circles(RADIUS)
    
    #Call the make_lines function
    make_lines(LENGTH, LINE_NUM, DEGREES)
    
    turtle.hideturtle() #Hide the cursor
    
    
#Draw concentric circles
def concentric_circles(RADIUS):
    DISTANCE_BETWEEN = 50 #distance between two circles in pixels
    LEVEL = int(RADIUS / DISTANCE_BETWEEN) #number of times to make a circle  
    if  LEVEL  >= 1:
        turtle.penup()          #Pickup pen from "paper"
        turtle.right(90)        #Turn pointer 90 degrees to point down
        turtle.forward(RADIUS)  #Move forward one radius
        turtle.right(270)       #Back to start heading
        turtle.pendown()        #Put the pen down on the "paper"
        turtle.circle(RADIUS)   #Draw a circle
        turtle.penup()          #Pen up while we go home
        turtle.home()           #Head back to the start pos
        LEVEL -= 1
        #Call concentric_circles function
        concentric_circles(RADIUS - DISTANCE_BETWEEN)

#Draw lines
def make_lines(LENGTH, LINE_NUM, DEGREES):
    if LINE_NUM >= 1:
        turtle.penup()          #Pickup pen from "paper"
        turtle.right(DEGREES)   #Turn pointer 0 degrees to point left
        turtle.pendown()        #Put the pen down on the "paper"
        turtle.forward(LENGTH)  #Move forward to outer circle
        turtle.penup()          #Pen up while we go home
        turtle.home()           #Head back to the start pos
        #Call the make_lines function
        make_lines(LENGTH, LINE_NUM - 1, DEGREES + 90)
        
#Call main function
main()

    
        
    
