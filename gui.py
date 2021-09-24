import tkinter as tk
from mailer import mail_loop

#TODO: Refactor!
def main():
    master = tk.Tk("Fool")
    canvas = tk.Canvas(master, height=300, width=500, bg="#278ee8")
    canvas.pack()
    #creating elements
    #labels
    email_label = tk.Label(master, text="Whats Your Gmail?")
    email_pwd_label = tk.Label(master, text="Whats your Gmail password?")
    recipient_label = tk.Label(master, text="Who is the recipient?")
    amount_of_email = tk.Label(master, text="How many emails do we send?")
    email_msg = tk.Label(master, text="Short email message")
    #entries
    email_entry = tk.Entry(master)
    email_pwd_entry = tk.Entry(master)
    recipient_entry = tk.Entry(master)
    amount_of_email_entry = tk.Entry(master)
    email_msg_entry = tk.Entry(master)
    #button
    btn = tk.Button(master, text="Submit", command=lambda: mail_loop(recipient_entry.get(), email_pwd_entry.get(), email_entry.get(), email_msg_entry.get(), int(amount_of_email_entry.get())))
    #adding elements to window
    btn.pack()
    #labels
    email_label.place(relx=0.1, rely=0.1)
    email_pwd_label.place(relx=0.1, rely=0.2)
    recipient_label.place(relx=0.1, rely=0.3)
    amount_of_email.place(relx=0.1, rely=0.4)
    email_msg.place(relx=0.1, rely=0.5)
    #entries
    email_entry.place(relx=0.5, rely=0.1)
    email_pwd_entry.place(relx=0.5, rely=0.2)
    recipient_entry.place(relx=0.5, rely=0.3)
    amount_of_email_entry.place(relx=0.5, rely=0.4)
    email_msg_entry.place(relx=0.5, rely=0.5)

    
    master.mainloop()

main()