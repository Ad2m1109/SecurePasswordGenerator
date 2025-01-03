import random
import string
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.filedialog import askdirectory

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True, min_uppercase=0, min_lowercase=0, min_numbers=0, min_special=0, exclude_similar=False):
    character_pool = ''
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if exclude_similar:
        character_pool = character_pool.replace('l', '').replace('I', '').replace('1', '').replace('O', '').replace('0', '')

    if not character_pool:
        raise ValueError('At least one character type must be selected.')

    password = ''
    if use_uppercase and min_uppercase > 0:
        password += ''.join(random.choice(string.ascii_uppercase) for _ in range(min_uppercase))
    if use_lowercase and min_lowercase > 0:
        password += ''.join(random.choice(string.ascii_lowercase) for _ in range(min_lowercase))
    if use_numbers and min_numbers > 0:
        password += ''.join(random.choice(string.digits) for _ in range(min_numbers))
    if use_special and min_special > 0:
        password += ''.join(random.choice(string.punctuation) for _ in range(min_special))

    for _ in range(length - len(password)):
        password += random.choice(character_pool)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def generate_password_ui():
    try:
        length = int(length_entry.get())
        min_uppercase = int(min_uppercase_entry.get()) if min_uppercase_entry.get() else 0
        min_lowercase = int(min_lowercase_entry.get()) if min_lowercase_entry.get() else 0
        min_numbers = int(min_numbers_entry.get()) if min_numbers_entry.get() else 0
        min_special = int(min_special_entry.get()) if min_special_entry.get() else 0
        exclude_similar = exclude_similar_var.get()

        use_uppercase = uppercase_var.get()
        use_lowercase = lowercase_var.get()
        use_numbers = numbers_var.get()
        use_special = special_var.get()

        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special, min_uppercase, min_lowercase, min_numbers, min_special, exclude_similar)

        messagebox.showinfo('Generated Password', f'Password: {password}')
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter valid values.')

root = tk.Tk()
root.title('Password Generator')
root.geometry('400x600')
root.configure(bg='#0f1c4f')

style = ttk.Style()
style.configure("TFrame", background='#0f1c4f')
style.configure("TLabel", background='#0f1c4f', foreground='#FFFFFF', font=('Arial', 10))
style.configure("TEntry", fieldbackground='#2D2D2D', foreground='#0f1c4f', font=('Arial', 10))
style.configure("TCheckbutton", background='#0f1c4f', foreground='#FFFFFF', font=('Arial', 10))
style.configure("TButton", background='#0f1c4f', foreground='#0f1c4f', font=('Arial', 10), padding=5)

input_frame = ttk.Frame(root, style="TFrame")
input_frame.pack(pady=10)

length_label = ttk.Label(input_frame, text='Enter password length:')
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = ttk.Entry(input_frame, width=20)
length_entry.grid(row=0, column=1, padx=5, pady=5)

min_uppercase_label = ttk.Label(input_frame, text='Minimum uppercase letters:')
min_uppercase_label.grid(row=1, column=0, padx=5, pady=5)
min_uppercase_entry = ttk.Entry(input_frame, width=20)
min_uppercase_entry.grid(row=1, column=1, padx=5, pady=5)

min_lowercase_label = ttk.Label(input_frame, text='Minimum lowercase letters:')
min_lowercase_label.grid(row=2, column=0, padx=5, pady=5)
min_lowercase_entry = ttk.Entry(input_frame, width=20)
min_lowercase_entry.grid(row=2, column=1, padx=5, pady=5)

min_numbers_label = ttk.Label(input_frame, text='Minimum numbers:')
min_numbers_label.grid(row=3, column=0, padx=5, pady=5)
min_numbers_entry = ttk.Entry(input_frame, width=20)
min_numbers_entry.grid(row=3, column=1, padx=5, pady=5)

min_special_label = ttk.Label(input_frame, text='Minimum special characters:')
min_special_label.grid(row=4, column=0, padx=5, pady=5)
min_special_entry = ttk.Entry(input_frame, width=20)
min_special_entry.grid(row=4, column=1, padx=5, pady=5)

options_frame = ttk.Frame(root, style="TFrame")
options_frame.pack(pady=10)

exclude_similar_var = tk.BooleanVar(value=False)
exclude_similar_check = ttk.Checkbutton(options_frame, text='Exclude similar characters (l, 1, I, O, 0)', variable=exclude_similar_var)
exclude_similar_check.pack(anchor='w', padx=5, pady=5)

uppercase_var = tk.BooleanVar(value=True)
uppercase_check = ttk.Checkbutton(options_frame, text='Include uppercase letters', variable=uppercase_var)
uppercase_check.pack(anchor='w', padx=5, pady=5)

lowercase_var = tk.BooleanVar(value=True)
lowercase_check = ttk.Checkbutton(options_frame, text='Include lowercase letters', variable=lowercase_var)
lowercase_check.pack(anchor='w', padx=5, pady=5)

numbers_var = tk.BooleanVar(value=True)
numbers_check = ttk.Checkbutton(options_frame, text='Include numbers', variable=numbers_var)
numbers_check.pack(anchor='w', padx=5, pady=5)

special_var = tk.BooleanVar(value=True)
special_check = ttk.Checkbutton(options_frame, text='Include special characters', variable=special_var)
special_check.pack(anchor='w', padx=5, pady=5)

button_frame = ttk.Frame(root, style="TFrame")
button_frame.pack(pady=10)

generate_button = ttk.Button(button_frame, text='Generate Password', command=generate_password_ui)
generate_button.pack(pady=10)

root.mainloop()
