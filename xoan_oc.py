import turtle


d=200
buoc_di=0
while (turtle.distance(0,0)<d):
    buoc_di+=0.3
    turtle.forward(buoc_di)
    turtle.left(30)
turtle.done()