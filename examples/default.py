
PI_SHAPE = addshape("examples/images/pi.gif")
print(PI_SHAPE)
def start(t):
    t.penup()
    t.goto(-SCREEN_WIDTH/2, 0)
    t.pendown()
    t.showturtle()


def update(t, frame):
    t.clear()
    t.shape(PI_SHAPE)
    t.penup()
    t.forward(SCREEN_WIDTH/NUM_FRAMES)

