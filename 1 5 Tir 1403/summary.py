from tkinter import *
from tkinter import messagebox
import smtplib, ssl

def send_mail():
    email_address = entry_email.get()
    if '@' not in email_address:
        messagebox.showerror("Error", "Email address should have @!")
        return
    if '.' not in email_address:
        messagebox.showerror("Error", "Email address should have at least one . !")
        return
    name = entry_name.get()
    message = f"Subject: Avina and Parsa \nHello {name}. This email is sent from python. Hope you enjoy it ;)"
    sender_email = "madval1369@gmail.com"
    password = "akxk zntp bvrf kdrg"
    smtp_server = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, email_address, message)
        messagebox.showinfo('success', "Email sent successfully!")
    except:
        messagebox.showerror('error', 'something went wrong!')
    finally:
        server.close()

root = Tk()
root.geometry('800x400')
root.config(bg='pink')
label_name = Label(root, text='Enter your name: ', bg='pink', font=('Tahoma', 24))
label_name.place(x=50, y=20, width=300, height=50)
entry_name = Entry(root, font=('Tahoma', 24))
entry_name.place(x=400, y=20, width=350, height=50)
label_email = Label(root, text='Enter your email: ', bg='pink', font=('consolas', 22))
label_email.place(x=50, y=120, width=300, height=50)
entry_email = Entry(root, font=('Tahoma', 24))
entry_email.place(x=400, y=120, width=350, height=50)
btn_send_mail = Button(root, text='Send me an email!', command=send_mail, bg='pink', font=('Tahoma', 24))
btn_send_mail.place(x=200, y=220, width=400, height=80)

mainloop()