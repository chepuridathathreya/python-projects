import tkinter as tk
root = tk.Tk()
root.title("My GUI")
a = tk.Label(root, text="Hello, World!")
a.pack()
button = tk.Button(root, text="click me", width=10, height=2, command=lambda: print("Button clicked!"))
button.pack()
root.mainloop()