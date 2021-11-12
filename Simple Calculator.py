from tkinter import *
from tkinter import messagebox


screen = Tk()
screen.title('Simple Calculator')
screen.iconbitmap('icon.ico')
screen.config(bg='black')


display = Entry(screen, bd=2, width=37, font=('times', 16, 'bold'), bg='black', fg='white')
display.grid(row=0, column=0, columnspan=4)


final = 0


def numbers(num):
    f_num = display.get()
    display.delete(0, END)
    display.insert(0, f"{f_num + str(num)}")


def add():
    if len(display.get()) == 0:
        messagebox.showwarning('Warning', 'You Did Not Enter Any Number')
    else:
        global operation
        global final
        final= int(display.get())
        display.delete(0, END)
        operation = 'ADD'


def sub():
    if len(display.get()) == 0:
        messagebox.showwarning('Warning', 'You Did Not Enter Any Number')
    else:
        global operation
        global final
        final = int(display.get())
        display.delete(0, END)
        operation = 'SUB'


def mul():
    if len(display.get()) == 0:
        messagebox.showwarning('Warning', 'You Did Not Enter Any Number')
    else:
        global operation
        global final
        final = int(display.get())
        display.delete(0, END)
        operation = 'MUL'


def div():
    if len(display.get()) == 0:
        messagebox.showwarning('Warning', 'You Did Not Enter Any Number')
    else:
        global operation
        global final
        final = float(display.get())
        display.delete(0, END)
        operation = 'DIV'


def equal():
    if len(display.get()) == 0:
        messagebox.showwarning('Warning', 'You Did Not Enter Any Number To Calculate')
    else:
        global operation
        global final
        f_num = display.get()
        if operation == 'ADD':
            final += int(f_num)
        elif operation == 'SUB':
            final -= int(f_num)
        elif operation == 'MUL':
            final *= int(f_num)
        elif operation == 'DIV':
            final /= int(f_num)
    display.delete(0, END)
    display.insert(0, f'{final}')



def clear():
    display.delete(0, END)




b7=Button(screen, text='7', pady=20, padx=40, font=('arial', 12, 'bold'), bg='black', fg='white', command=lambda: numbers(7), activebackground='black', activeforeground='white')
b7.grid(row=1, column=0, sticky='w')
b8=Button(screen, text='8', pady=20, padx=40, font=('arial', 12, 'bold'), bg='black', fg='white', command=lambda: numbers(8), activebackground='black', activeforeground='white')
b8.grid(row=1, column=1, sticky='w')
b9=Button(screen, text='9', pady=20, padx=40, font=('arial', 12, 'bold'), bg='black', fg='white', command=lambda: numbers(9), activebackground='black', activeforeground='white')
b9.grid(row=1, column=2, sticky='w')


b4=Button(screen, text='4', pady=20, padx=40, font=('arial', 12, 'bold'), bg='black', fg='white', command=lambda: numbers(4), activebackground='black', activeforeground='white')
b4.grid(row=2, column=0, sticky='w')
b5=Button(screen, text='5', pady=20, padx=40, font=('arial', 12, 'bold'), bg='black', fg='white', command=lambda: numbers(5), activebackground='black', activeforeground='white')
b5.grid(row=2, column=1, sticky='w')
b6=Button(screen, text='6', pady=20, padx=40, font=('arial', 12, 'bold'), bg='black', fg='white', command=lambda: numbers(6), activebackground='black', activeforeground='white')
b6.grid(row=2, column=2, sticky='w')


b1=Button(screen, text='1', pady=20, padx=40, font=('arial', 12, 'bold'), bg='black', fg='white', command=lambda: numbers(1), activebackground='black', activeforeground='white')
b1.grid(row=3, column=0, sticky='w')
b2=Button(screen, text='2', pady=20, padx=40, font=('arial', 12, 'bold'), bg='black', fg='white', command=lambda: numbers(2), activebackground='black', activeforeground='white')
b2.grid(row=3, column=1, sticky='w')
b3=Button(screen, text='3', pady=20, padx=40, font=('arial', 12, 'bold'), bg='black', fg='white', command=lambda: numbers(3), activebackground='black', activeforeground='white')
b3.grid(row=3, column=2, sticky='w')


ba=Button(screen, text='+', pady=20, padx=42, font=('arial', 12, 'bold'), bg='black', fg='cyan', command=add, activebackground='black', activeforeground='cyan')
ba.grid(row=1, column=3, sticky='w')
bs=Button(screen, text='-', pady=18, padx=42, font=('arial', 14, 'bold'), bg='black', fg='cyan', command=sub, activebackground='black', activeforeground='cyan')
bs.grid(row=2, column=3, sticky='w')
bm=Button(screen, text='x', pady=20, padx=42, font=('arial', 12, 'bold'), bg='black', fg='cyan', command=mul, activebackground='black', activeforeground='cyan')
bm.grid(row=3, column=3, sticky='w')
bd=Button(screen, text='/', pady=20, padx=44, font=('arial', 13, 'bold'), bg='black', fg='cyan', command=div, activebackground='black', activeforeground='cyan')
bd.grid(row=4, column=3, sticky='w')



b0=Button(screen, text='0', pady=20, padx=40, font=('arial', 12, 'bold'), command=lambda: numbers(0), bg='black', fg='white', activebackground='black', activeforeground='white')
b0.grid(row=4, column=1, sticky='w')
bc=Button(screen, text='Clear', pady=20, padx=24, font=('arial', 13, 'bold'), bg='black', fg='white', command=clear, activebackground='red', activeforeground='white')
bc.grid(row=4, column=0, sticky='w')
be=Button(screen, text='=', pady=20, padx=40, font=('arial', 12, 'bold'), command=equal, activebackground='green', bg='black', fg='cyan', activeforeground='cyan')
be.grid(row=4, column=2, sticky='w')

screen.mainloop()