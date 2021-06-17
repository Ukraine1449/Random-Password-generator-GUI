import string
import random
import tkinter
from tkinter import END



letters = 0
numbers = 0
special = 0
tk = tkinter.Tk()
tk.title('Random password generator')
listbox = tkinter.Listbox(tk)
listbox.insert(END, "Please enter how many of each do you want?")
listbox.insert(END, "3rd box is numbers, 2nd box is special characters and first is letters")
listbox.insert(END, "Please enter only numbers")
listbox.pack()
entry = tkinter.Entry(tk)
entry.pack()
entryyy = tkinter.Entry(tk)
entryyy.pack()
entryy = tkinter.Entry(tk)
entryy.pack()
def set_letters():
    randPassword(letters=int(entryy.get()), numbers=int(entry.get()), special=int(entryyy.get()))

def randPassword(letters, special, numbers):
    capital = string.ascii_letters
    speciall = string.punctuation
    numberss = string.digits
    password = []
    for i in range(0, special):
        password.append(random.choice(capital))
    for i in range(0, letters):
        password.append(random.choice(speciall))
    for i in range(0, numbers):
        password.append(random.choice(numberss))
    random.shuffle(password)
    print(password)
    full_str =''
    full_str = full_str.join(password)
    print(full_str)
    listbox.insert(END, full_str)

button = tkinter.Button(tk, text='Add', command=set_letters)
button.pack()

tk.geometry("500x400")
tk.mainloop()
