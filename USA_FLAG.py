import turtle
import math

# Flag dimensions
FLAG_HEIGHT = 260
FLAG_WIDTH = 494
STRIPE_HEIGHT = FLAG_HEIGHT / 13
UNION_HEIGHT = STRIPE_HEIGHT * 7
UNION_WIDTH = FLAG_WIDTH * 2 / 5

# Adjust union size for star placement
UNION_HEIGHT += STRIPE_HEIGHT * 1.25
UNION_WIDTH += FLAG_WIDTH * 0.06

# Colors
RED = "#B3192E"
WHITE = "#FFFFFF"
BLUE = "#0A3161"

# Star dimensions
STAR_DIAMETER = UNION_HEIGHT / 12
STAR_RADIUS = STAR_DIAMETER / 2

# Setup screen
screen = turtle.Screen()
screen.setup(width=FLAG_WIDTH + 100, height=FLAG_HEIGHT + 100)
screen.bgcolor("white")
screen.title("Flag of the United States")

# Create drawing pen
pen = turtle.Turtle()
pen.speed(0)
pen.up()

# Function to draw a rectangle
def draw_rectangle(turtle, x, y, width, height, color):
    turtle.goto(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()

# Function to draw a star
def draw_star(turtle, x, y, radius, color):
    turtle.goto(x, y - radius)
    turtle.setheading(162)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(2 * radius * math.sin(math.radians(36)))
        turtle.left(144)
    turtle.end_fill()
    turtle.up()

# Draw the stripes
y = FLAG_HEIGHT / 2
for i in range(13):
    color = RED if i % 2 == 0 else WHITE
    draw_rectangle(pen, -FLAG_WIDTH / 2, y, FLAG_WIDTH, STRIPE_HEIGHT, color)
    y -= STRIPE_HEIGHT

# Draw the union
draw_rectangle(pen, -FLAG_WIDTH / 2, FLAG_HEIGHT / 2, UNION_WIDTH, UNION_HEIGHT, BLUE)

# Draw the stars
star_rows = [6, 5] * 5
star_y = FLAG_HEIGHT / 2 - STRIPE_HEIGHT
star_x_start = -FLAG_WIDTH / 2 + UNION_WIDTH / 10

for row_count in star_rows:
    star_x = star_x_start if row_count == 6 else star_x_start + UNION_WIDTH / 12
    for _ in range(row_count):
        draw_star(pen, star_x, star_y, STAR_RADIUS, WHITE)
        star_x += UNION_WIDTH / 6
    star_y -= UNION_HEIGHT / 11

# Hide pen and finish
pen.hideturtle()
turtle.done()
