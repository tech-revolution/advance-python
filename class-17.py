# Task 1 email slicer
# example@domain.com
# email = input("Enter Your Email: ").strip()
# username = email[:email.index("@")]
# domain_name = email[email.index("@")+1:]
# print(f"Your name is {username} and your domain name is {domain_name}")

# import mymodule as mm

# mm.print_name("Hello")
from tkinter import Label, Tk
import time
import pyqrcode

app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("450x150")
app_window.resizable(1,1)

text_font = ("Boulder",68, 'bold')
background = "#fe76a3"
foreground = "#354623"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)


digital_clock()
app_window.mainloop()



