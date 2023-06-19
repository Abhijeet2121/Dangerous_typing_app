from tkinter import *

count = 0

window = Tk()
window.title("Dangerous Typing App")
window.geometry('800x800')
window.config(padx=50, pady=50)

def check_text():
    global count, current_text
    if len(text_entry.get()) > 0 and text_entry.get() == current_text:
        message_label.config(text=f"Deleting in... {count}Secs", fg='red')
        if count == 0:
            message_label.config(text="Start Typing again...", fg="white")
            text_entry.delete(0, END)
            window.after(1000, check_text)
        else:
            count -= 1
            window.after(1000, check_text)
    else:
        current_text = text_entry.get()
        count = 5
        window.after(1000, check_text)

current_text = ''
text_entry = Entry(font=("Arial", 20, 'normal'), width=40)
text_entry.grid(row=2, column=0, padx=30, pady=20, sticky='w')
text_entry.focus()

title_label = Label(text="Dangerous Typing App", font=("TImes New Roman", 24, 'normal'))
title_label.grid(row=0, column=0, padx=30, pady=20, sticky='w')

message_label = Label(text='Start Typing', font=('Arial', 20, 'normal'))
message_label.grid(row=1, column=0, padx=30, pady=20, sticky='w')

if __name__ == "__main__":
    check_text()
    window.mainloop()