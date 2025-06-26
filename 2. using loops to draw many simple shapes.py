import tkinter as tk

# Set up the main application window
root = tk.Tk()
root.title("Drawing with tk")

# Create a canvas widget to draw on
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

#draw some concentric circles using a loop to change the radius 
for radius in range(0,100,5):  
    canvas.create_oval(150-radius,150-radius,150+radius,150+radius)  

#draw some rectangles of increasing size, all starting @ 100,300
for size in range(0,200,10):
        canvas.create_rectangle(100,300,100+size,300+size)

#draw one of those cool line patterns that make a curve
for offset in range(0,150,10):
            canvas.create_line(300+offset,100,450,100+offset)

#put some words into random positions on the screen
from random import randint
for word in 'a mix of random words all jumbled in a list'.split():  
    canvas.create_text(300+randint(0,200),300+randint(0,200),text=word)

# Start the Tkinter event loop
root.mainloop()
