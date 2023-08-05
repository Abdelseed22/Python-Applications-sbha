#************* Muslim Sbaha app *************** 


import tkinter as tk

def add_one(number_label):
    number = int(number_label["text"])
    number += 1
    number_label.config(text=str(number))

def exit_program():
        root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Add One")

# Create a label to display the number
number_label = tk.Label(root, text="0", font=("Helvetica", 24))
number_label.pack(pady=20)

# Create a button to add one to the number
add_button = tk.Button(root, text="Add One", command=lambda: add_one(number_label))
add_button.pack()

# Create an "Exit" button to close the program
exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack()
 



# Start the main event loop
root.mainloop()
