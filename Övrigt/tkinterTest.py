import time
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk

root = Tk()
screenHeight = 1000
screenWidth = 1000

root.title("Adam Jonsson")
canvas = Canvas(root, height=screenHeight, width=screenWidth)
canvas.pack()

ball = canvas.create_oval(0, 0, 100, 100, fill="red")
images = Image.open("City.jpg")
tempimage = ImageTk.PhotoImage(images)
imageObject = canvas.create_image((255, 255), tempimage)
xSpeed = 5
ySpeed = 3

while True:
    canvas.move(ball, xSpeed, ySpeed)
    ballPos = canvas.coords(ball)
    if(ballPos[2] >= screenWidth or ballPos[0] <= 0):
        xSpeed *= -1
    if(ballPos[3] >= screenHeight or ballPos[1] <= 0):
        ySpeed *= -1
    root.update()
    time.sleep(0.01)
root.mainloop()