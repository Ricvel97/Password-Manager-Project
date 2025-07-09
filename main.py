from tkinter import *
from tkinter import messagebox
import random
import pyperclip

BLUE = "#1B3C53"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def random_password():
    password_entry.delete(0, END)
    password = []

    password += [random.choice(letters) for _ in range(random.randint(7, 10))]
    password += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(password)

    new_password = ''.join(password)

    password_entry.insert(END, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website_info = website_entry.get()
    username_info = username_entry.get()
    password_info = password_entry.get()

    if len(website_info) == 0 or len(password_info) == 0:
        messagebox.showwarning(title="Alert!", message="Don't leave any of the fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website_info, message=f"These are the details provided:\n"
                                                                   f"Email: {username_info}\n"
                                                                   f"Password: {password_info}\n"
                                                                   f"Is the data correct?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_info} | {username_info} | {password_info}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Password Manager")
root.config(padx=40, pady=40, bg=BLUE)


canvas = Canvas(width=200, height=200, bg=BLUE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# -------------------------------------- Labels -------------------------------------
website = Label(text="Website:")
website.config(padx=5, pady=5, bg=BLUE, fg="white", font=("Courier", 15, "bold"))
website.grid(column=0, row=1)

username = Label(text="Email/Username:")
username.grid(column=0, row=2)
username.config(padx=5, pady=5, bg=BLUE, fg="white", font=("Courier", 15, "bold"))

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_label.config(padx=5, pady=5, bg=BLUE, fg="white", font=("Courier", 15, "bold"))

# -------------------------------------- Entries -------------------------------------
website_entry = Entry(width=54)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.config()

username_entry = Entry(width=54)
username_entry.insert(END, "Ricardoavc97@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=29)
password_entry.grid(column=1, row=3)

# -------------------------------------- Buttons -------------------------------------
add_button = Button(text="Add", width=40, bg="#D2C1B6", fg="black", font=("Courier", 10, "bold"), command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

gen_pass_button = Button(text="Generate Password", bg="#D2C1B6", fg="black", font=("Courier", 10, "bold"), command=random_password)
gen_pass_button.grid(column=2, row=3)

root.mainloop()