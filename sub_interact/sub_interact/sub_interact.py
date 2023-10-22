## import all subcodes
## Each button has a function that can call 

#pedir que quiere el usuario
## new subject // showcase latest report
## available subjects // showcase latest report
## others

#
import tkinter as tk
from tkinter import PhotoImage

def close_window():
    window.destroy()

def open_window():
    # Create a new top-level window
    window2 = tk.Toplevel(window)
    
    # Set the window title
    window2.title("Child Window")

    # Create a label with padding
    label = tk.Label(window2, text="This is a child window.")
    label.pack(padx=10, pady=10, anchor="w")  # Align to the left (west)


    # Create a button to close the window
    close_button = tk.Button(window2, text="Close", command=close_window)
    close_button.pack(padx=10, pady=10, anchor="w")  # Align to the left (west)

def get_input():
    user_input = entry.get()  # Get the text from the Entry widget
    label.config(text=f"You entered: {user_input}")


# Create the main window
window = tk.Tk()

# Set the window title
window.title("Subject_Screener App UI")

# Create a label widget
label = tk.Label(window, text="Welcome to Subject Screener! This is a tool to help you build corpus content & words for a subject based on news on the internet.")
label.pack(padx=10, pady=10)


# Create a button widget
button = tk.Button(window, text="Search New Subject", command=open_window)
button.pack(padx=10, pady=10, anchor="w")

image = PhotoImage(file="your_image.gif")  # Replace "your_image.gif" with the path to your image file

# Create a label to display the image
image_label = tk.Label(root, image=image)
image_label.pack()



button = tk.Button(window, text="Explore Available Subjects")
button.pack(padx=10, pady=10, anchor="w")

button = tk.Button(window, text="See latest reports updated")
button.pack(padx=10, pady=10, anchor="w")



# Create a label
label = tk.Label(window, text="Enter something:")
label.pack()

# Create an Entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button to get the input
button = tk.Button(window, text="Submit", command=get_input)
button.pack()

# Start the main event loop
window.mainloop()