import tkinter as tk
from tkinter import messagebox

def validate_form():
    name = entry_name.get()
    gender = var_gender.get()
    dob = entry_dob.get()
    email = entry_email.get()
    password = entry_password.get()
    
    # Simple validation
    if not email or not password:
        messagebox.showerror("Input Error", "Email and Password are required!")
        return
    
    if len(password) < 8:
        messagebox.showerror("Input Error", "Password must be at least 8 characters long!")
        return
    
    if '@' not in email or '.' not in email:
        messagebox.showerror("Input Error", "Invalid email address!")
        return
    
    # If validation passes, show a success message
    messagebox.showinfo("Success", "Registration successful!")
    # Here you could redirect to another window or page if needed

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place widgets
tk.Label(root, text="Enter name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:").grid(row=1, column=0, padx=10, pady=5)
var_gender = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=var_gender, value="Male").grid(row=1, column=1, padx=10, pady=5)
tk.Radiobutton(root, text="Female", variable=var_gender, value="Female").grid(row=1, column=2, padx=10, pady=5)
tk.Radiobutton(root, text="Others", variable=var_gender, value="Others").grid(row=1, column=3, padx=10, pady=5)

tk.Label(root, text="Enter Date of Birth:").grid(row=2, column=0, padx=10, pady=5)
entry_dob = tk.Entry(root)
entry_dob.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Enter email:").grid(row=3, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Enter password:").grid(row=4, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=4, column=1, padx=10, pady=5)

tk.Button(root, text="Submit", command=validate_form).grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
