import turtle

width = 300
height = 250

turtle.color("blue")

def drawPaintBoard():
	turtle.shape("triangle")
	turtle.penup()
	turtle.color("red")
	fillRect(0 - width,0 + height,30 -width,30 +height)
	turtle.color("blue")
	fillRect(30-width,height,60-width,30+height)
	turtle.color("#000000")
	drawRect(width,height,width-30,30+height)
	drawRect(width-30,height,width-60,height+30)
	turtle.penup()
	turtle.goto(width-15,height)
	turtle.pendown()
	turtle.circle(15)
	fillRect(width-60,height,width-90,height+30)
	drawRect(width-90,height,width-120,height+30)
	turtle.penup()
	turtle.goto(width-105,height)
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(15)
	turtle.end_fill()
	turtle.penup()
	drawRect(-15,height,15,height+30)
	turtle.goto(0,height)
	drawCursor()
	drawEraser()
	turtle.color("blue")

def drawEraser():
	turtle.penup()
	turtle.goto(-15,height)
	i = 0	
	while(i<3):
		drawRect(-15,height+10*i,-45,height+10*(i+1))
		i+=1
	

def drawCursor():
	turtle.penup()
	turtle.goto(0,height)
	turtle.pendown()
	turtle.goto(15,height+30)
	turtle.goto(-15,height+30)
	turtle.goto(0,height)
	turtle.penup()

	
	

def drawRect(x1,y1,x2,y2):
	turtle.penup()
	turtle.goto(x1,y1)
	turtle.pendown()
	turtle.goto(x1,y2)
	turtle.goto(x2,y2)
	turtle.goto(x2,y1)
	turtle.goto(x1,y1)
	turtle.penup()

def fillRect(x1,y1,x2,y2):
	turtle.penup()	
	turtle.goto(x1,y1)
	turtle.pendown()
	i = y1;
	while(i <= y2):
		turtle.goto(x2,i)
		turtle.goto(x1,i)
		i +=1
	turtle.penup()

def onClick(x,y):
	
	global cursorCircle
	global cursorFill 
	global cursorDrag
	shitHappened = False
	
	if(x >= -width and x <= (30 -width) and y >= height and y<= (30+height)):
		turtle.color("red")
		shitHappened = True
		

	if(x >= 30-width and x <= (60 -width) and y >= height and y<= (30+height)):
		turtle.color("blue")
		shitHappened = True
	
	if(not cursorDrag):
		if(x >= width - 30 and x <= width and y >= height and y<= (30+height)):
			cursorCircle = True
			cursorFill = False
			shitHappened = True
	
		if(x >= width-60 and x <= width-30 and y >= height and y<= (30+height)):
			cursorCircle = False
			cursorFill = False
			shitHappened = True

		if(x >= width-90 and x <= width-60 and y >= height and y<= (30+height)):
			cursorCircle = False
			cursorFill = True
			shitHappened = True

		if(x >= width-120 and x <= width-90 and y >= height and y<= (30+height)):
			cursorCircle = True
			cursorFill = True
			shitHappened = True
		if(x >= -45 and x <= -15 and y >= height and y<= (30+height)):
			turtle.color("white")
			turtle.begin_fill()
			drawRect(-width,-height,width,height-1)
			turtle.end_fill()
			shitHappened = True
			

	if(x >= -15 and x <= 15 and y >= height and y<= (30+height)):
		cursorDrag = not cursorDrag
		if(cursorDrag):
			turtle.showturtle()
		else:
			turtle.hideturtle()
		shitHappened = True
		
		
	if(not shitHappened and not cursorDrag):
		if(cursorCircle):
			drawCircle(x,y)
		else:
			if(cursorFill):
				turtle.begin_fill()
			drawRect(x-cursorSize,y-cursorSize,x+cursorSize,y+cursorSize)
			turtle.end_fill()
	
	if(cursorDrag and not shitHappened):
		turtle.penup()
		turtle.goto(x,y)	

def drawCircle(x,y):
	if(cursorFill):
		turtle.begin_fill()
	turtle.penup()
	turtle.goto(x,y - cursorSize/2)
	turtle.pendown()
	turtle.circle(cursorSize)
	turtle.penup()
	turtle.end_fill()

def onDrag(x,y):
	global cursorDrag
	if(cursorDrag):
		turtle.pendown()
	turtle.goto(x,y)
		

turtle.speed(0)
turtle.hideturtle()

drawPaintBoard()


color = "blue"
cursorCircle = True
cursorFill = False
cursorDrag = False
eraser = False
cursorSize = 10

turtle.onscreenclick(onClick,1,True)
turtle.ondrag(onDrag,1,False)

turtle.mainloop()
