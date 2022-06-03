from tkinter import *

def entrada(valor):
    label1['text'] += valor

def saida():
    resultado = eval(label1['text'])
    label1['text'] = str(resultado)

def  limpar():
    label1['text'] = ''


Calculadora = Tk()

# Tamanhos dos botões(Button)
Calculadora.grid_rowconfigure(0, weight=1)
Calculadora.grid_columnconfigure(0, weight=1)
Calculadora.grid_rowconfigure(1, weight=1)
Calculadora.grid_columnconfigure(1, weight=1)
Calculadora.grid_columnconfigure(2, weight=1)

# widgets
label1 = Label(Calculadora, text='', font='Arial 28')
bt1 = Button(Calculadora, text='7', font='Arial 30', command=lambda: entrada('7'))
bt2 = Button(Calculadora, text='8', font='Arial 30', command=lambda: entrada('8'))
bt3 = Button(Calculadora, text='9', font='Arial 30', command=lambda: entrada('9'))
bt4 = Button(Calculadora, text='*', font='Arial 30', command=lambda: entrada('*'))
bt5 = Button(Calculadora, text='4', font='Arial 30', command=lambda: entrada('4'))
bt6 = Button(Calculadora, text='5', font='Arial 30', command=lambda: entrada('5'))
bt7 = Button(Calculadora, text='6', font='Arial 30', command=lambda: entrada('6'))
bt8 = Button(Calculadora, text='/', font='Arial 30', command=lambda: entrada('/'))
bt9 = Button(Calculadora, text='1', font='Arial 30', command=lambda: entrada('1'))
bt10 = Button(Calculadora, text='2', font='Arial 30', command=lambda: entrada('2'))
bt11 = Button(Calculadora, text='3', font='Arial 30', command=lambda: entrada('3'))
bt12 = Button(Calculadora, text='+', font='Arial 30', command=lambda: entrada('+'))
bt13 = Button(Calculadora, text='0', font='Arial 30', command=lambda: entrada('0'))
bt14 = Button(Calculadora, text='=', font='Arial 30', command=lambda: saida())
bt15 = Button(Calculadora, text='.', font='Arial 30', command=lambda: entrada('.'))
bt16 = Button(Calculadora, text='-', font='Arial 30', command=lambda: entrada('-'))
bt17 = Button(Calculadora, text='Del', font='Arial 30', command=lambda: limpar())
bt18 = Button(Calculadora, text='C', font='Arial 30', command=lambda: limpar())
bt19 = Button(Calculadora, text='(', font='Arial 30', command=lambda: entrada('('))
bt20 = Button(Calculadora, text=')', font='Arial 30', command=lambda: entrada(')'))

# layout
label1.grid(row=0, column=0, sticky=NSEW)
bt1.grid(row=1, column=0, sticky=NSEW)
bt2.grid(row=1, column=1, sticky=NSEW)
bt3.grid(row=1, column=2, sticky=NSEW)
bt4.grid(row=1, column=3, sticky=NSEW)
bt5.grid(row=2, column=0, sticky=NSEW)
bt6.grid(row=2, column=1, sticky=NSEW)
bt7.grid(row=2, column=2, sticky=NSEW)
bt8.grid(row=2, column=3, sticky=NSEW)
bt9.grid(row=3, column=0, sticky=NSEW)
bt10.grid(row=3, column=1, sticky=NSEW)
bt11.grid(row=3, column=2, sticky=NSEW)
bt12.grid(row=3, column=3, sticky=NSEW)
bt13.grid(row=4, column=0, sticky=NSEW)
bt14.grid(row=4, column=1, sticky=NSEW)
bt15.grid(row=4, column=2, sticky=NSEW)
bt16.grid(row=4, column=3, sticky=NSEW)
bt17.grid(row=5, column=0, sticky=NSEW)
bt18.grid(row=5, column=1, sticky=NSEW)
bt19.grid(row=5, column=2, sticky=NSEW)
bt20.grid(row=5, column=3, sticky=NSEW)

# run
Calculadora.mainloop()
