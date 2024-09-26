import random
from tkinter import *
from tkinter import messagebox
import pyperclip


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
    is_ok = False
    f = open("data_details.txt","a+")
    website = web_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) < 1 or   len(password) < 1:
        messagebox.showinfo(title="Error",message="Make sure You haven't left any field empty !!" )
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered :\n "
                                                         f"Email : {username} \n Password: {password}.\n Are you ok to save?" )
        if is_ok :
            f.writelines(f"{website} ¦ {username} ¦ {password} \n")
            password_input.delete(0,"end")
            web_input.delete(0,"end")
            f.close()




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








window.mainloop()