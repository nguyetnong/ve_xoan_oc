import turtle

mau_sac =['red','green']
mau_sac[0]
d=200
buoc_di=0
turtle.pensize(5)
cnt =0
while (turtle.distance(0,0)<d):
    if cnt % 2 == 0:
        turtle.color(mau_sac[0])
    else:
        turtle.color(mau_sac[1])
    buoc_di+=0.3
    turtle.forward(buoc_di)
    turtle.left(30)
    cnt = cnt +1
turtle.done()