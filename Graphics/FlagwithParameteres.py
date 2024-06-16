from graphics import Canvas

canvas_width = 400
canvas_height = 300

def main():
    canvas = Canvas(canvas_width,canvas_height)
    draw_japan_flag(canvas)
    canvas.wait_for_click()
    draw_bangladeshi_flag(canvas)
    draw_pulau_flag(canvas)

def draw_japan_flag(canvas):
    draw_circle(canvas,canvas_width/2,canvas_height/2,120,'red')

def draw_bangladeshi_flag(canvas):
    canvas.create_rectangle(0,0,canvas_width,canvas_height,'darkgreen')
    draw_circle(canvas,canvas_width/2,canvas_height/2,150,'red')

def draw_pulau_flag(canvas):
    canvas.create_rectange(0,0,canvas_width,canvas_height,'dodgerblue')
    draw_circle(canvas,canvas_width/2,canvas_height/2,150,'yellow')

def draw_circle(canvas,center_x,center_y,size,color):
    left_x = center_x-size/2
    top_y = center_y - size/2
    right_x = left_x + size
    bottom_y = top_y +size
    canvas.create_oval(left_x, top_y, right_x, bottom_y,color)

if __name__ == '__main__':
    main()

