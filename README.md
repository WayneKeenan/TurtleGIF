# TurtleGIF 

A utility which captures the output of Python Turtle programs into animated GIFs for [Zoe the Digital Zoetrope](https://github.com/Corteil/Digital-Zoetrope-) by Brian Corteil. 

The examples are currently very basic, Turtle graphics can do so much more.


# Installation

``` 
git clone https://github.com/WayneKeenan/TurtleGIF.git 

cd TurtleGIF

# Creating a virtual env is optional but highly recommended:
python3 -m venv venv
. ./venv/bin/activate

pip3 install -r requirements.txt
```


# Examples

Run from the root of the repository.

---

## Circle

Python Turtle script:

```python
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

```

Running:
```bash
python turtlegif.py --script=examples/circle.py
```

Output GIF:

![Circle Animation](images/circle.gif)

---

## Square
```
python turtlegif.py --script=examples/square.py
```

Output GIF:

![Square Animation](images/square.gif)

---

## Bitmap
```
python turtlegif.py --script=examples/pi_logo.py
```
Output GIF:

![Pi Logo Animation](images/pi.gif)

---



# Thanks

[Animation with Turtle Graphics](https://wecode24.com/stories/abraham/animation-with-turtle-graphics)

