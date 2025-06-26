import tkinter as tk

# Set up the main application window
root = tk.Tk()
root.title("Drawing with tk")

# Create a canvas widget to draw on
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

canvas.create_oval(100,100,200,200)  #100,100 to 200,200 is the bounding box of the oval (ie a circle)
canvas.create_rectangle(100,300,200,400)  #100,300 to 200,400 is the bounding box of the rectangle (ie a square)
canvas.create_line(300,100,400,200) #draw a line from 300,100 to 400,200
canvas.create_text(300,300,text="Text!")    #put some text on the screen at 300,300 

# Start the Tkinter event loop
root.mainloop()
