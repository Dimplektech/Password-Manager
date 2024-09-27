import random
from textwrap import indent
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for char in range(random.randint(8,10))]

    password_list += [random.choice(numbers) for char in range(random.randint(2,4))]

    password_list += [random.choice(symbols) for char in range(random.randint(2,4))]

    random.shuffle(password_list)
    password = "".join(password_list)


    password_input.insert(0,password)
    # To copy to the clipboard
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email":username,
            "password":password
        }

    }

    if len(website) < 1 or   len(password) < 1:
        messagebox.showinfo(title="Error",message="Make sure You haven't left any field empty !!" )
    else:
        try:
            with open("data_details.json","r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data_details.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open("data_details.json", "w") as data_file:
                json.dump(data,data_file,indent=4)


        password_input.delete(0,END)
        web_input.delete(0,END)

def find_password():
    try:
        with open("data_details.json","r") as data_file:
            website = web_input.get()
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No Data file not found!")
    else:
        # Convert all keys in the data dict to lowercase
        data_lower = {key.lower():value for key,value in data.items()}
        website_lower =  website.lower()
        if  website_lower in data_lower:
            email= data_lower[website_lower]["email"]
            password=data_lower[website_lower]["password"]
            messagebox.showinfo(title=website.title(),message = f"Email: {email} \n Password: {password} ")
        else:
            messagebox.showinfo(title="Error",message=f"No details exists for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
#window.minsize(width=500,height=400)
window.config(padx=50,pady=50)
canvas =Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

# Labels
web_label = Label(text="Website:",font="15")
web_label.grid(column=0,row=1)
username_label= Label(text="Email/Username:",font=15)
username_label.grid(column=0,row=2)
password_label= Label(text="Password:",font="15")
password_label.grid(column=0,row=3)

#Entries

web_input = Entry(width=40)
web_input.grid(row =1, column=1, columnspan=2)
web_input.focus()
username_input = Entry(width=40)
username_input.insert(0,"dk@dkaware.com")
username_input.grid(row=2,column=1,columnspan=2)
password_input=Entry(width=40)
password_input.grid(row=3,column=1,columnspan=2)

# Buttons
gen_pass = Button(text="Generate Password",command=generate_password)
gen_pass.grid(column=3,row=3)
add_button = Button(text="Add",width=36,bg="skyblue",command=save)
add_button.grid(column=1,row=5,columnspan=2)
search_button= Button(text="Search",width=15,command=find_password)
search_button.grid(column=3,row=1)








window.mainloop()