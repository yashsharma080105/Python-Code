from tkinter import *
from  tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generated_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(2, 5))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbols
    shuffle(password_list)


    password = "".join(password_list)

# password = ""
# for char in password_list:
#     password += char

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }







    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any field empty")
    else:
        try:
    # messagebox.showinfo(title="Title", message="Message") # showinfo is use to generate a popup by using tkinter
            with open("dat.json", "r") as data_file:
              #Reading old data
              data = json.load(data_file)
        except FileNotFoundError:
            with open("dat.json", "w") as data_file :
                json.dump(new_data, data_file, indent=4)

        else:
          #Updating old data with new data
             data.update(new_data)

             with open("dat.json", "w") as data_file:
                    # saving update data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("dat.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found.")

    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title =website, message=f"Email: {email}\n Password:{password}" )
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website :")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username :")
email_label.grid(row=2,column=0)
password_label= Label(text="Password :")
password_label.grid(row=3,column=0)

# Entries

website_entry= Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus() #. The focus() method sets focus to a window.
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert( 0, "yash@gmail")  # insert is use to  inserts a  string in a specified index 0 for staring and END for End
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1 ,column=2)
generated_password_button = Button(text="Generate Password", command=generated_password)
generated_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command= save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
