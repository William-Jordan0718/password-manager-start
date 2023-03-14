from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


# Website Row
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)


# Email Row
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)


# Password Row
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

button = Button(text="Generate Password", width=10)
button.grid(column=2, row=3)


# Add Button
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()