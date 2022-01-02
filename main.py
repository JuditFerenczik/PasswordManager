from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    password_list = [choice(letters) for num in range(randint(8, 10))]
    password_list += [choice(symbols) for num in range(randint(2, 4))]
    password_list += [choice(numbers) for num in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(char for char in password_list)
    print(f"Your password is: {password}")
    entry_pass.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():

    with open("passwords.txt", mode='a') as f:
        website = entry_web.get()
        email= entry_email.get()
        password = entry_pass.get()

        if len(website) < 1 or len(password) < 1:
            messagebox.showinfo(title="Error", message="Website and password fields cannot be empty!")
            return
        is_ok = messagebox.askokcancel(title=website,message=f"These details are entered:\nE-mail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            savings =f"{website} |  {email}  |  {password}\n"
            f.write(savings)
            print(savings)
            entry_web.delete(0, 'end')
            entry_pass.delete(0, 'end')

    # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

l_webs = Label(text="Website:")
l_webs.grid(row=1, column=0)

entry_web = Entry(width=52)
entry_web.grid(row=1, column=1, columnspan=2)
entry_web.focus()

l_email = Label(text="Email/Username:")
l_email.grid(row=2, column=0)

entry_email = Entry(width=52)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0,"sample@gmail.com")

l_pass = Label(text="Password:")
l_pass.grid(row=3, column=0)

entry_pass = Entry(width=32)
entry_pass.grid(row=3, column=1)

pass_button = Button(text="Generate Password", command=generate_pass )
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()