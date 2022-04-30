import argparse
import turtle
from time import sleep
import tempfile
from PIL import Image
import imageio.v2 as imageio
from os.path import join



parser = argparse.ArgumentParser()


# Hardocded graphbical settings for Zoe https://github.com/Corteil/Digital-Zoetrope-
#parser.add_argument("--width",  type=int, default=1024, help="")
#parser.add_argument("--height", type=int, default=768, help="")
#parser.add_argument("--depth", type=int, default=768, help="")     # currently just mono
#parser.add_argument("--frames", type=int, default=32, help="")
#parser.add_argument("--fps", type=int, default=25, help="")
parser.add_argument("--script", type=str, default="examples/default.py", help="")
parser.add_argument("--output", type=str, default="output.gif", help="")
parser.add_argument("--zoe", action='store_true', default=True, help="")
parser.add_argument("--zoe_width_border", type=int, default=19, help="Adjustment fudge factor for Turtle UI")
parser.add_argument("--zoe_height_border", type=int, default=19, help="Adjustment fudge factor for Turtle UI")

args = parser.parse_args()

if args.zoe:
    args.width = 296   + args.zoe_width_border
    args.height = 128  + args.zoe_height_border
    args.frames = 15
    args.fps = 12.5

screen = turtle.Screen()
screen.setup(args.width, args.height)

screen.tracer(False)            # disable auto canvas update
#turtle.screensize(canvwidth=args.width, canvheight=args.height, bg=None)
canvas = screen.getcanvas()
canvas.update()
# print(turtle.screensize())
# print(canvas.winfo_width())


t = turtle.Turtle()
t.reset()
t.hideturtle()
t.speed(0)  # fast

# Setup some vars for the script
NUM_FRAMES = args.frames
SCREEN_WIDTH = args.width
SCREEN_HEIGHT = args.height
DEFAULT_COLOUR="black"


with tempfile.TemporaryDirectory() as tmpdirname:
    frame = 0
    png_filepaths = []

    # Utility to work around Turtle only supporting GIFS
    # WIP...
    def addshape(filepath: str):
        if not filepath.lower().endswith("gif"):
            images = []
            images.append(imageio.imread(filepath))
            gif_filepath = join(tmpdirname, 'tmp.gif')
            imageio.mimsave(gif_filepath, images)
            screen.addshape(gif_filepath)
            return gif_filepath
        else:
            screen.addshape(filepath)
            return filepath



    # Zoe is currently mono so default it
    t.fillcolor(DEFAULT_COLOUR)

    # Read and exec th script
    exec(open(args.script).read())

    start(t)
    for frame in range(0, args.frames):
        print("frame={}".format(frame))
        update(t, frame)
        sleep(1/args.fps)
        screen.update()         # display frame
        frame += 1
        eps_filepath = join(tmpdirname, "frame_{}.eps".format(frame))
        png_filepath = join(tmpdirname, "frame_{}.png".format(frame))
        png_filepaths.append(png_filepath)
        canvas.postscript(file=eps_filepath, colormode='mono')
        ps_img = Image.open(eps_filepath)
        ps_img.save(png_filepath, "png")

    # https://imageio.readthedocs.io/en/v2.4.1/formats.html
    # https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
    with imageio.get_writer(args.output, mode='I', palettesize=2, fps=args.fps) as writer:
        for filename in png_filepaths:
            image = imageio.imread(filename)
            writer.append_data(image)
    print("Generated " + args.output)