
def draw_square(t):
    for side in range(4):
        t.forward(SCREEN_HEIGHT/4)
        t.left(90)


def start(t):
    t.penup()
    t.goto(-SCREEN_WIDTH/2, 0)
    t.pendown()


def update(t, frame):
    t.clear()
    draw_square(t)
    t.penup()
    t.forward(SCREEN_WIDTH/NUM_FRAMES)
    t.pendown()

