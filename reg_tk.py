import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        
        # Create a frame for the form
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(padx=10, pady=10)

        # Name
        self.name_label = tk.Label(self.frame, text="Enter name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack()

        # Gender
        self.gender_label = tk.Label(self.frame, text="Gender:")
        self.gender_label.pack()
        self.gender_var = tk.StringVar(value="")
        self.male_radio = tk.Radiobutton(self.frame, text="Male", variable=self.gender_var, value="Male")
        self.male_radio.pack()
        self.female_radio = tk.Radiobutton(self.frame, text="Female", variable=self.gender_var, value="Female")
        self.female_radio.pack()
        self.others_radio = tk.Radiobutton(self.frame, text="Others", variable=self.gender_var, value="Others")
        self.others_radio.pack()

        # Date of Birth
        self.dob_label = tk.Label(self.frame, text="Enter Date of Birth:")
        self.dob_label.pack()
        self.dob_entry = tk.Entry(self.frame)
        self.dob_entry.pack()

        # Email
        self.email_label = tk.Label(self.frame, text="Enter email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.frame)
        self.email_entry.pack()

        # Password
        self.password_label = tk.Label(self.frame, text="Enter password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show='*')
        self.password_entry.pack()

        # Submit Button
        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        name = self.name_entry.get()
        gender = self.gender_var.get()
        dob = self.dob_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Simple validation
        if not name or not gender or not dob or not email or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if len(password) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long!")
            return
        
        # Validate email format
        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid email address!")
            return

        # Success message
        messagebox.showinfo("Success", "Registration successful!")

        # Optionally: redirect to another function or window here

# Create the main window
root = tk.Tk()
app = RegistrationForm(root)
root.mainloop()
