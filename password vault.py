import tkinter as tk
from tkinter import END, messagebox, PhotoImage
import mysql.connector as sql

op = 0
def open_db():    
    global db
    global c
    try:       
        db = sql.connect(username = "root" ,password = "", host = "127.0.0.1", database = "aravind")
        c = db.cursor()
        
    except:
        lab = tk.Label(window, text="before continue start sql in xampp")
        lab.grid(row=0,column=1,columnspan=2)
        exit_button = tk.Button(window, text="Exit", command=window.quit,width=10,bg="black",fg="white",state="normal")
        exit_button.grid(row=5,column=2,padx=10,pady=10)

    else:
        messagebox.showinfo("Password Vault", "DB is open now!")
        close_button = tk.Button(window, text="close DB", command=lambda:[close_db()],bg="red",fg="white",state="normal")
        close_button.grid(row=5,column=1,padx=10,pady=10)

def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    gmail = Gmail_entry.get()

    q = "insert into details values (%s,%s,%s,%s)"
    t = [(website,gmail,username,password)]
    
    
    try:
        c.executemany(q,t)
        db.commit()
        # Show a messagebox to confirm password saved
        messagebox.showinfo("Password Vault", "Password Saved!")
    except:
        messagebox.showinfo("Password vault","Oops! something went wrong")

    website_entry.delete(0,END)
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    Gmail_entry.delete(0,END)
    del q
    del t
    del password
    del username
    del website
    del gmail


def close_db():
    messagebox.showinfo("Password Vault", "DB was closed!")
    db.close()
    exit_button = tk.Button(window, text="Exit", command=window.quit,width=10,bg="black",fg="white",state="normal")
    exit_button.grid(row=5,column=2,padx=10,pady=10)
    

# Create the main window
window = tk.Tk()
window.title("Password Vault")
window.configure(bg="lightblue")

pic = tk.PhotoImage(file="icon2.ico")
window.iconphoto(False,pic)

# Create labels and entry fields for website, username, and password
website_label = tk.Label(window, text="Website:",bg="lightblue")
website_label.grid(row=1,column=0,padx=10,pady=10)
website_entry = tk.Entry(window)
website_entry.grid(row=1,column=2,padx=10,pady=10)

Gmail_label = tk.Label(window, text="Gmail Id:",bg="lightblue")
Gmail_label.grid(row=2,column=0,padx=10,pady=10)
Gmail_entry = tk.Entry(window)
Gmail_entry.grid(row=2,column=2,padx=10,pady=10)

username_label = tk.Label(window, text="Username:",bg="lightblue")
username_label.grid(row=3,column=0,padx=10,pady=10)
username_entry = tk.Entry(window)
username_entry.grid(row=3,column=2,padx=10,pady=10)

password_label = tk.Label(window, text="Password:",bg="lightblue")
password_label.grid(row=4,column=0,padx=10,pady=10)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=4,column=2,padx=10,pady=10)


# Create a button to save the password
open_button = tk.Button(window, text="open DB", command=open_db,bg="green",fg="white")
open_button.grid(row=0,column=0,padx=10,pady=10)

save_button = tk.Button(window, text="Save", command=save_password,bg="orange")
save_button.grid(row=5,column=0,padx=10,pady=10)

close_button = tk.Button(window, text="close DB", command=lambda:[close_db()],bg="red",fg="white",state="disabled")
close_button.grid(row=5,column=1,padx=10,pady=10)

exit_button = tk.Button(window, text="Exit", command=window.quit,width=10,bg="black",fg="white",state="disabled")
exit_button.grid(row=5,column=2,padx=10,pady=10)

# Run the Tkinter event loop
window.mainloop()