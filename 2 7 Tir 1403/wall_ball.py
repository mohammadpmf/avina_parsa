from tkinter import *
from PIL import Image, ImageTk
import random
from threading import Thread
from time import sleep

BALL_SIZE=64
WIDTH = 600
HEIGHT = 800

def move_ball():
    chance = random.randint(0, 1)
    if chance==1:
        x_speed = 5
    else:
        x_speed = -5
    y_speed = -10
    while True:
        x = int(lbl_ball.place_info().get('x'))
        y = int(lbl_ball.place_info().get('y'))
        if x<=0 or x>WIDTH-BALL_SIZE:
            x_speed *= -1
        if y<=0:
            y_speed *= -1
        x += x_speed
        y += y_speed
        if y>HEIGHT-2*BALL_SIZE-10:
            x_player = int(btn_me.place_info().get('x'))
            if x_player-BALL_SIZE < x < x_player+WIDTH//5:
                y_speed *= -1
        lbl_ball.place(x=x, y=y)
        sleep(0.02)

def move_player(event):
    x = int(btn_me.place_info().get('x'))
    if event.keysym=='Right':
        x += 10
        if x>4*WIDTH//5:
            x=4*WIDTH//5
    elif event.keysym=='Left':
        x -= 10
        if x<0:
            x=0
    btn_me.place(x=x)

root = Tk()
root.geometry(f"{WIDTH}x{HEIGHT}+{WIDTH}+100")
img_info = Image.open('black.png')
img = img_info.resize((BALL_SIZE, BALL_SIZE))
img = ImageTk.PhotoImage(img)
lbl_ball = Label(root, image=img)
lbl_ball.place(x=WIDTH//2-BALL_SIZE//2, y=HEIGHT-2*BALL_SIZE)
btn_me = Button(root, bg='orange')
root.bind('<Key>', move_player)
btn_me.place(x=2*WIDTH//5, width=WIDTH//5, y=HEIGHT-BALL_SIZE, height=BALL_SIZE)
Thread(target=move_ball, daemon=True).start()
root.mainloop()