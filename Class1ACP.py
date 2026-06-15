# Import tkinter module
from tkinter import *

# Create the main window
root = Tk()
root.title("Product Calculator")
root.geometry("300x200")

# Function to calculate product
def calculate_product():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 * num2
    result_label.config(text="Product = " + str(result))

# Labels
label1 = Label(root, text="Enter First Number:")
label1.pack()

# Entry box for first number
entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Enter Second Number:")
label2.pack()

# Entry box for second number
entry2 = Entry(root)
entry2.pack()

# Button to calculate product
btn = Button(root, text="Calculate Product", command=calculate_product)
btn.pack(pady=10)

# Label to display result
result_label = Label(root, text="Product = ")
result_label.pack()

# Run the application
root.mainloop()