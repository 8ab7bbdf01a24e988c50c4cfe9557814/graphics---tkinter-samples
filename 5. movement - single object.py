import tkinter as tk

# Set up the main application window
root = tk.Tk()
root.title("Drawing with tk")

def move():
    #move the oval object by dx, dy pixels ... and then move if afterwards as well
    global dx,dy
    canvas.move(oval, dx, dy)
    x=canvas.coords(oval)[0]
    y=canvas.coords(oval)[1]
    if x>canvas.winfo_width() or x<0:   #check if the oval has gone too far horizontally
        dx=dx*-1
    if y>canvas.winfo_height() or y<0:  #check if the oval has gone too far vertically
        dy=dy*-1
    canvas.after(10, move)   #call this move procedure again in 10ms

# Create a canvas widget to draw on
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

#save an oval object to a variable name, and choose some movement values
oval=canvas.create_oval(100,200,200,300,fill="white")
dx=1
dy=1

canvas.after(1000,move) #call the move procedure in 1000ms

# Start the Tkinter event loop - this listens for events such as pressing a mouse button
root.mainloop()
