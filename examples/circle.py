
def start(t):
    t.penup()
    t.goto(-SCREEN_WIDTH/2, 0)
    t.pendown()


def update(t, frame):
    t.clear()
    t.begin_fill()
    t.circle(SCREEN_HEIGHT/6)
    t.end_fill()
    t.penup()
    t.forward(SCREEN_WIDTH/NUM_FRAMES)

