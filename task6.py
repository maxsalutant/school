from turtle import*
size = 30
left(90)
tracer(0)
down()
speed(0)
for k in range(7):
    forward(10*size)
    right(120)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*size, y*size)
        dot(4, red)
done()