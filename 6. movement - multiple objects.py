import tkinter as tk

# Set up the main application window
root = tk.Tk()
root.title("Drawing with tk")

#draw an oval centred on an 'event' location
def mouseLeftClick(event):
    oval=canvas.create_oval(event.x-10, event.y-10, event.x+10, event.y+10, fill="white")
    canvas.after(1000, lambda: move(oval, 0, 1)) #call the move procedure on this oval after 1s with values 0,1

#draw a rectangle centred on an 'event' location
def mouseRightClick(event):
    rectangle=canvas.create_rectangle(event.x-10, event.y-10, event.x+10, event.y+10, fill="black")
    canvas.after(1000, lambda: move(rectangle, 1, 0)) #call the move procedure on this rectangle after 1s with values 0,1

#place a character somewhere randomly on the screen
def keyPress(event):
    from random import randint
    text=canvas.create_text(randint(0,500), randint(0,500),text=event.keysym)
    dx=randint(-1,1)
    dy=randint(-1,1)
    canvas.after(1000, lambda: move(text, dx, dy))   #call the move procedure on this text after 1s with random values

def move(thing, dx, dy):
    #move a thing by dx, dy pixels ... and then move if afterwards as well
    canvas.move(thing, dx, dy)
    x=canvas.coords(thing)[0]
    y=canvas.coords(thing)[1]
    if x>canvas.winfo_width() or x<0:
        dx=dx*-1
    if y>canvas.winfo_height() or y<0:
        dy=dy*-1
    canvas.after(10, lambda: move(thing, dx, dy))   #call this move procedure on this thing again in 10ms

# Create a canvas widget to draw on
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

#associate pressing a mouse button or a keyboard key with a subprogram
canvas.bind("<Button-1>", mouseLeftClick)
canvas.bind("<Button-3>", mouseRightClick)
root.bind("<Key>", keyPress)

# Start the Tkinter event loop - this listens for events such as pressing a mouse button
root.mainloop()
