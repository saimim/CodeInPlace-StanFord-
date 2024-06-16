from graphics import canvas
import time

Canvas_WIDTH = 500
CANVAS_HEIGHT = 500

def main():
    canvas = Canvas(Canvas_WIDTH,CANVAS_HEIGHT)

    canvas.create_line(0,0,500,500)