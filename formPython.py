import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    
    message = f"Name: {name}\nEmail: {email}"
    messagebox.showinfo("Form Submission", message)

# Create the main window
root = tk.Tk()
root.title("FORM")
greeting = tk.Label(text="Sign up for free. No credit card required")
greeting.pack()

# Create and place labels and entry fields
name_label = tk.Label(root, text="First Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

last_label = tk.Label(root, text="Last Name:")
last_label.pack()
last_entry = tk.Entry(root)
last_entry.pack()

email_label = tk.Label(root, text="Business Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

password = tk.Label(root, text="Password")
password.pack()
pass_entry = tk.Entry(root)
pass_entry.pack()
# Create and place the submit button
submit_button = tk.Button(root, text="SIGN UP", command=submit_form)
submit_button.pack()

# Start the tkinter main loop
root.mainloop()