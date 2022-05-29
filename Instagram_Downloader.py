# import packages
from tkinter import *
from instaloader import *
from tkinter import filedialog
import os
import urllib.parse
import instaloader
import threading

# call instaloder package
mod = instaloader.Instaloader()


# download direction function
def browse_button():

    filename = filedialog.askdirectory()

    lbl1.config(text ="Download Direction : "+str(filename))

    os.chdir(filename)


# download posts function
def download():
    profile = instaloader.Profile.from_username(mod.context, str(url_entry.get()))
    print('media count:', profile.mediacount)
    try:
        post_number = profile.mediacount
        posts_label.config(text=str(post_number) + " posts", bg="yellow")
        for i in range(post_number):
            tasks_label.config(text="Download Is Completing, Please Wait! ")
            mod.download_profile(str(url_entry.get()), profile_pic_only=False)
            break
        return tasks_label.config(text="download is completed")

    except Exception as Error:

        print(Error)

    return download_label.config(text="complete")


# login function
def login():
    try:
        log = mod.login(str(user_entry.get()), str(password_entry.get()))
        label.config(text="You Logged Successfully")

    except Exception as Error:
        label.config(text="The Password Was Wrong")


# download highlights function
def dnhighlights():
    userID = mod.check_profile_id(url_entry.get())

    mod.download_highlights(userID, fast_update=False)


# download story function
def stories():
    userID = mod.check_profile_id(url_entry.get())
    mod.download_stories(userids=[userID])


# download profile pic function
def profile():
    mod.download_profile(str(url_entry.get()), profile_pic_only=True)


# download saved post function
def save_post():
    mod.download_saved_posts(max_count=10, fast_update=False, post_filter=None)


# download single post function
def single():
    address = str(url_entry)
    s = urllib.parse.urlsplit(address)
    add = ("{}".format(s.path.split("p/")[-1], s.query))
    new_url = add.replace("/", "")
    post = Post.from_shortcode(mod.context, new_url)
    mod.download_post(post, target='os.chdir(sourcePath)')
    print("Done")

# main window tkinter
window = Tk()
window.title("Insta Bot")
window.geometry('500x500')
window.resizable(False, False)
# icon = PhotoImage(file="instagram-logo-png-2428.png")
#window.iconphoto(True, icon)

# Buttons Frame
frame = Frame(window, bg="green", width=250, height=70)
frame.grid(row=15, column=0, columnspan=2)

# Direction label
lbl1 = Label(window, text="")
lbl1.grid(row=6, column=0)

# Completed Download Label
download_label = Label(window, text="")
download_label.grid(row=8, column=0)

# posts number
posts_label = Label(window, text="")
posts_label.grid(row=6, column=1)

# direction button
buttonBrowse = Button(frame, text="Browse folder", command=browse_button, width=15)
buttonBrowse.grid(row=0, column=0)

# target url label
url_label = Label(window, text="Instagram Username >>> ", font=25)
url_label.grid(row=5, column=0)

# downloading label
tasks_label = Label(window, text="")
tasks_label.grid(row=5, column=1)

# target url entry
url_entry = Entry(window, width=40)
url_entry.grid(row=5, column=1)

# download button
download_Button = Button(frame, text='Download pics', width=15, command=threading.Thread(target=download).start)
download_Button.grid(row=1, column=0)

# username label
username_label = Label(window, text="Enter Your Username >>> ")
username_label.grid(row=0, column=0)

# username entry
user_entry = Entry(window, width=30)
user_entry.grid(row=0, column=1)

# password label
password_label = Label(window, text="Enter Your Password >>>")
password_label.grid(row=1, column=0)

# password entry
password_entry = Entry(window, width=30)
password_entry.grid(row=1, column=1)
password_entry.config(show="*")

# login button
login_button = Button(window, text="Login", command=login, width=15, bg="yellow", fg="red")
login_button.grid(row=2, column=0)
login_button.config(padx=2, pady=2)

# login status label
label = Label(window, text="Logging Status: ")
label.grid(row=2, column=1)

# highlights_button
highlights_button = Button(frame, text="Download Highlights", command=dnhighlights, width=15)
highlights_button.grid(row=1, column=1)

# download story_buttons
story_buttons = Button(frame, text="Download Stories ", command=stories, width=15)
story_buttons.grid(row=2, column=1)

# download profile button
down_profile = Button(frame, text="Download Profile Pic", command=profile, width=15)
down_profile.grid(row=2, column=0)

# download username saved button
post_button = Button(frame, text="Saved Posts", command=save_post, width=15)
post_button.grid(row=3, column=0)

# download single post
single_post = Button(frame, text="Download One Post", command=single, width=15)
single_post.grid(row=3, column=1)

window.mainloop()
