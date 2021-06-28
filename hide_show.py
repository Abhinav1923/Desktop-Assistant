
def show_login(window, canvas, bot, start_btn, backBtn, username_entry, password_entry, loginBtn, signup_link, signupBtn, login_link, reg_username_entry, reg_email_entry, reg_password_entry, background_img, login_heading, username_img, password_img):

    window.title("Desktop Assistant | Login")
    canvas.delete('heroTitle')
    bot.place_forget()
    canvas.delete('create')
    canvas.delete('update')
    canvas.delete('read')
    canvas.delete('delete')
    canvas.delete('email')
    start_btn.place_forget()
    canvas.create_image(232, 315, image=background_img, tag='background')
    canvas.create_image(730, 180, image=login_heading, tag='login_title')
    backBtn.place(x=485, y=30)
    canvas.delete('username')
    canvas.delete('password')
    canvas.create_image(730, 300, image=username_img, tag='username')
    canvas.create_image(730, 400, image=password_img, tag='password')
    username_entry.place(x=572.0, y=290, width=321.0, height=50)
    password_entry.place(x=572.0, y=370+20, width=321.0, height=50)
    loginBtn.place(x=670, y=460)
    signup_link.place(x=622, y=515)
    canvas.delete('signup_title')
    signupBtn.place_forget()
    login_link.place_forget()
    reg_username_entry.place_forget()
    reg_email_entry.place_forget()
    reg_password_entry.place_forget()


def show_cover(window, canvas, bot, start_btn, backBtn, username_entry, password_entry, loginBtn, signup_link, signupBtn, login_link, reg_username_entry, reg_email_entry, reg_password_entry, hero_title, update_img, delete_img, read_img, create_img, logoutBtn):

    window.title("Desktop Assistant")
    bot.place(x=335, y=355)
    canvas.delete('background')
    canvas.delete('login_title')
    backBtn.place_forget()
    loginBtn.place_forget()
    signup_link.place_forget()
    username_entry.place_forget()
    password_entry.place_forget()
    reg_username_entry.place_forget()
    reg_email_entry.place_forget()
    reg_password_entry.place_forget()
    canvas.delete('username')
    canvas.delete('password')
    canvas.create_image(500, 180, image=hero_title, tag='heroTitle')
    canvas.create_image(790, 520, image=update_img, tag='update')
    canvas.create_image(165, 520, image=delete_img, tag='delete')
    canvas.create_image(750, 410, image=read_img, tag='read')
    canvas.create_image(235, 380, image=create_img, tag='create')
    start_btn.place(x=435, y=290)
    canvas.delete('signup_title')
    canvas.delete('email')
    login_link.place_forget()
    signupBtn.place_forget()
    canvas.delete('wizard')
    canvas.delete('Rectangle_box')
    canvas.delete('ball_1')
    canvas.delete('ball_2')
    canvas.delete('ball_3')
    canvas.delete('ball_4')
    canvas.delete('ball_5')
    canvas.delete('ball_6')
    logoutBtn.place_forget()


def show_signup(window, canvas, username_entry, password_entry, loginBtn, signup_link, signupBtn, login_link, reg_username_entry, reg_email_entry, reg_password_entry, username_img, email, password_img, signup_heading):

    window.title("Desktop Assistant | Signup")
    canvas.delete('login_title')
    loginBtn.place_forget()
    signup_link.place_forget()
    username_entry.place_forget()
    password_entry.place_forget()
    canvas.delete('username')
    canvas.delete('password')
    canvas.create_image(730, 250, image=username_img, tag='username')
    canvas.create_image(730, 350, image=email, tag='email')
    canvas.create_image(730, 450, image=password_img, tag='password')
    canvas.create_image(700, 145, image=signup_heading, tag='signup_title')
    signupBtn.place(x=665, y=510)
    login_link.place(x=622, y=562)
    reg_username_entry.place(x=572.0, y=240, width=321.0, height=50)
    reg_email_entry.place(x=572.0, y=340, width=321.0, height=50)
    reg_password_entry.place(x=572.0, y=440, width=321.0, height=50)


def show_assistant(window, canvas, wizard, Rectangle_box, ball_1, ball_2, ball_3, ball_4, ball_5, ball_6, signupBtn, login_link, reg_username_entry, reg_email_entry, reg_password_entry, backBtn, loginBtn, signup_link, username_entry, password_entry, github, logoutBtn, micBtn):

    window.title("Desktop Assistant | FiloBot")
    canvas.create_image(500, 220, image=wizard, tag='wizard')
    canvas.create_image(500, 490, image=Rectangle_box, tag='Rectangle_box')
    canvas.create_image(720, 200, image=ball_1, tag='ball_1')
    canvas.create_image(60, 350, image=ball_2, tag='ball_2')
    canvas.create_image(260, 170, image=ball_3, tag='ball_3')
    canvas.create_image(790, 330, image=ball_4, tag='ball_4')
    canvas.create_image(950, 150, image=ball_5, tag='ball_5')
    canvas.create_image(200, 350, image=ball_6, tag='ball_6')
    logoutBtn.place(x=850, y=35)
    micBtn.place(x=780, y=520)
    signupBtn.place_forget()
    login_link.place_forget()
    reg_username_entry.place_forget()
    reg_email_entry.place_forget()
    reg_password_entry.place_forget()
    backBtn.place_forget()
    canvas.delete('background')
    canvas.delete('login_title')
    backBtn.place_forget()
    loginBtn.place_forget()
    signup_link.place_forget()
    username_entry.place_forget()
    password_entry.place_forget()
    reg_username_entry.place_forget()
    reg_email_entry.place_forget()
    reg_password_entry.place_forget()
    canvas.delete('username')
    canvas.delete('password')
    canvas.delete('signup_title')
    canvas.delete('email')
    canvas.delete('linkImg')
    github.place_forget()
