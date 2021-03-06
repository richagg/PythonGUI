#This script takes in two numbers and returns a calculated number back. 
#This is an extension of a simple sum of 2 numbers program
#I chose to do range rescling to see how it would handle float points ( and because it was a part of a larger project!)

#Things to remember : stuff you read from the input using get() is str. Typecast before doing calculations!

from tkinter import *
from tkinter.messagebox import *

#------------define a function for calculating the answer --------------#
def show_answer():
    scale_min = float(num1.get())
    scale_max = float(num2.get())
    scaled_score = 100 * (scale_max- scale_min+1) +scale_min
    Ans = round(scaled_score,4)
    blank.delete(0,END) #this deletes the prevoius answer if you want to rerunt he calculation
    blank.insert(0, Ans)

#------------define the main-This is the front end frame --------------#
main = Tk()
Label(main, text = "Input1").grid(row=0)
Label(main, text = "Input2").grid(row=1)
Label(main, text = "Answer").grid(row=2)



num1 = Entry(main)
num1.insert(END, '0')
num2 = Entry(main)
num2.insert(END, '1')
blank = Entry(main)


num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
blank.grid(row=2, column=1)


Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)
Button(main, text='Show', command=show_answer).grid(row=4, column=1, sticky=W, pady=4)


main.title(" Name of my Window")
# main.geometry("500x400") (use if you want to resize)
mainloop()
