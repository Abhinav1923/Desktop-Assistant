from tkinter import *
from tkinter import messagebox
from tkvideo import *
import webbrowser
from PIL import Image, ImageTk
import hide_show
import db_connect

window = Tk()
window.title("Desktop Assistant")
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth()/2 - 982/2)
positionDown = int(window.winfo_screenheight()/2 - 710/2)
window.geometry(f"982x629+{positionRight}+{positionDown}")
window.iconbitmap('images/favicon.ico')
# window.wm_attributes('-alpha', 0.7)
window.configure(bg="#fff")
canvas = Canvas(window, bg="#fff", height=629, width=982,
                bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)


'''cover page'''
img = ImageTk.PhotoImage(file="images/logo1.png")
canvas.create_image(50, 40, image=img)

hero_title = ImageTk.PhotoImage(file="images/heroTitle.png")
canvas.create_image(500, 180, image=hero_title, tag='heroTitle')

bot = Label(window, background='#fff')
player = tkvideo("videos\\bot.mp4", bot, loop=1, size=(302, 289))
player.play()
bot.place(x=335, y=355)

create_img = ImageTk.PhotoImage(file="images/create.png")
canvas.create_image(235, 380, image=create_img, tag='create')

read_img = ImageTk.PhotoImage(file="images/read.png")
canvas.create_image(750, 410, image=read_img, tag='read')

delete_img = PhotoImage(file="images/delete.png")
canvas.create_image(165, 520, image=delete_img, tag='delete')

update_img = ImageTk.PhotoImage(file="images/update.png")
canvas.create_image(790, 520, image=update_img, tag='update')

link_img = PhotoImage(file="images/linkTitle.png")
canvas.create_image(900, 45, image=link_img, tag='linkImg')

'''login'''

background_img = ImageTk.PhotoImage(file="images/background.png")

login_heading = ImageTk.PhotoImage(file="images/login_heading.png")

username = ImageTk.PhotoImage(file="images/username.png")
password = ImageTk.PhotoImage(file="images/password.png")

username_entry = Entry(
    bd=0, bg="#F6F4F4", highlightthickness=0, font=('calibre', 14, 'normal'))
username_entry.focus()

password_entry = Entry(bd=0, bg="#F6F4F4", highlightthickness=0,
                       show='*', font=('calibre', 14, 'normal'))

'''Signup'''

signup_heading = ImageTk.PhotoImage(file="images/signup_title.png")

email = ImageTk.PhotoImage(file="images/email.png")

reg_username_entry = Entry(
    bd=0, bg="#F6F4F4", highlightthickness=0, font=('calibre', 14, 'normal'))
reg_username_entry.focus()

reg_email_entry = Entry(bd=0, bg="#F6F4F4", highlightthickness=0,
                        font=('calibre', 14, 'normal'))

reg_password_entry = Entry(bd=0, bg="#F6F4F4", highlightthickness=0,
                           show='*', font=('calibre', 14, 'normal'))


def login_clicked():
    username = username_entry.get()
    password = password_entry.get()

    if not username:
        messagebox.showerror(title="Empty Fields",
                             message="Please enter Username")

    elif not password:
        messagebox.showerror(title="Empty Fields",
                             message="Please enter password")

    else:
        db_connect.check_login(username, password)


def signup_clicked():
    username = reg_username_entry.get()
    email = reg_email_entry.get()
    password = reg_password_entry.get()

    if not username:
        messagebox.showerror(title="Empty Fields",
                             message="Please enter Username")

    if not email:
        messagebox.showerror(title="Empty Fields",
                             message="Please enter Email")

    elif not password:
        messagebox.showerror(title="Empty Fields",
                             message="Please enter password")

    else:
        db_connect.check_signup(username, email, password, reg_username_entry)


def contribute_github(event):
    url = "https://github.com/Abhinav1923/Desktop-Assistant"
    webbrowser.open_new(url)


github = Label(text="Contribute on GitHub", bg="#fff",
               fg="#2B98E7", cursor="hand2")
github.place(x=820, y=44)
github.bind('<Button-1>', contribute_github)


start = PhotoImage(file="images/start_button.png")
start_btn = Button(image=start, borderwidth=0,
                   highlightthickness=0, relief="flat", activebackground='#fff', background='#fff', cursor="hand2", command=lambda: hide_show.show_login(window, canvas, bot, start_btn, back, username_entry, password_entry, login, signup_link, signup, login_link, reg_username_entry, reg_email_entry, reg_password_entry, background_img, login_heading, username, password))
start_btn.place(x=435, y=290)

back_btn = ImageTk.PhotoImage(file="images/back.png")
back = Button(image=back_btn, borderwidth=0,
              highlightthickness=0, relief="flat", activebackground='#fff', background='#fff', cursor="hand2", command=lambda: hide_show.show_cover(window, canvas, bot, start_btn, back, username_entry, password_entry, login, signup_link, signup, login_link, reg_username_entry, reg_email_entry, reg_password_entry, hero_title, update_img, delete_img, read_img, create_img))

login_btn = ImageTk.PhotoImage(file="images/login_btn.png")
login = Button(image=login_btn, borderwidth=0,
               highlightthickness=0, relief="flat", activebackground='#fff', background='#fff', cursor="hand2", command=lambda: login_clicked())

signupLink = ImageTk.PhotoImage(file="images/signup_link.png")
signup_link = Button(image=signupLink, borderwidth=0,
                     highlightthickness=0, relief="flat", activebackground='#fff', background='#fff', cursor="hand2", command=lambda: hide_show.show_signup(window, canvas, username_entry, password_entry, login, signup_link, signup, login_link, reg_username_entry, reg_email_entry, reg_password_entry, username, email, password, signup_heading))

loginLink = ImageTk.PhotoImage(file="images/login_link.png")
login_link = Button(image=loginLink, borderwidth=0,
                    highlightthickness=0, relief="flat", activebackground='#fff', background='#fff', cursor="hand2", command=lambda: hide_show.show_login(window, canvas, bot, start_btn, back, username_entry, password_entry, login, signup_link, signup, login_link, reg_username_entry, reg_email_entry, reg_password_entry, background_img, login_heading, username, password))

signup_btn = ImageTk.PhotoImage(file="images/signup_btn.png")
signup = Button(image=signup_btn, borderwidth=0,
                highlightthickness=0, relief="flat", activebackground='#fff', background='#fff', cursor="hand2", command=lambda: signup_clicked())

window.resizable(False, False)
window.mainloop()