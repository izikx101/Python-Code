import turtle

def drawSqaure (t, x, y, length):
    t.up()
    t.goto(x, y)
    t.down()
    for count in range(4):
        t.foward(length)
        t.left(90)

