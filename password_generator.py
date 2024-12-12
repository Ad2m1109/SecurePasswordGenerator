import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError('At least one character type must be selected.')

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def generate_password_with_requirements(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError('At least one character type must be selected.')

    password = ''
    if use_uppercase:
        password += random.choice(string.ascii_uppercase)
    if use_lowercase:
        password += random.choice(string.ascii_lowercase)
    if use_numbers:
        password += random.choice(string.digits)
    if use_special:
        password += random.choice(string.punctuation)

    for _ in range(length - len(password)):
        password += random.choice(character_pool)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Function to generate password based on user input
def generate_password_ui():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_numbers = numbers_var.get()
        use_special = special_var.get()

        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        password_with_requirements = generate_password_with_requirements(length, use_uppercase, use_lowercase, use_numbers, use_special)

        messagebox.showinfo('Generated Passwords', f'Password: {password}\nPassword with requirements: {password_with_requirements}')
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter a valid length.')

# Creating the main window
root = tk.Tk()
root.title('Password Generator')

# Creating UI elements
length_label = tk.Label(root, text='Enter password length:')
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

uppercase_var = tk.BooleanVar(value=True)
uppercase_check = tk.Checkbutton(root, text='Include uppercase letters', variable=uppercase_var)
uppercase_check.pack()

lowercase_var = tk.BooleanVar(value=True)
lowercase_check = tk.Checkbutton(root, text='Include lowercase letters', variable=lowercase_var)
lowercase_check.pack()

numbers_var = tk.BooleanVar(value=True)
numbers_check = tk.Checkbutton(root, text='Include numbers', variable=numbers_var)
numbers_check.pack()

special_var = tk.BooleanVar(value=True)
special_check = tk.Checkbutton(root, text='Include special characters', variable=special_var)
special_check.pack()

generate_button = tk.Button(root, text='Generate Password', command=generate_password_ui)
generate_button.pack()

# Running the main loop
root.mainloop()
