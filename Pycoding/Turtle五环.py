#绘制奥运环
import turtle

turtle.width(10) #画笔宽度

turtle.color("blue")  #画之前调整颜色
turtle.circle(50)

turtle.penup()
turtle.goto(120,0)

turtle.pendown()
turtle.color("black")
turtle.circle(50)
turtle.penup()
turtle.goto(240,0)

turtle.pendown()
turtle.color("red")
turtle.circle(50)
turtle.penup()
turtle.goto(60,-60)

turtle.pendown()
turtle.color("yellow")
turtle.circle(50)
turtle.penup()
turtle.goto(180,-60)

turtle.pendown()
turtle.color("green")
turtle.circle(50)

