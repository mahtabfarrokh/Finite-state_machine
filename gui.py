import tkinter
import tkinter as tk
from tkinter import *
import table
class Gui :
    def __init__(self):

        self._entry = {}
        self.rows =0
        self.columns = 0
        self.root = tkinter.Tk()
        self.centerWindow()
        self.frame = Frame(self.root)
        self.frame.pack()

        self.frame1 = Frame(self.frame)
        self.frame1.pack()

        self.frame2 = Frame(self.frame)
        self.frame2.pack(side=BOTTOM)

        self.guiMake()
        self.root.mainloop()
    def getEntery (self ) :
        return int(self.E1.get())

    def makeTable(self):
        num = self.getEntery()
        self.columns = num
        self.rows = num
        self.root.destroy()

        self.table = table.SimpleTableInput ( num , num)

    def centerWindow (self) :
        self.root.withdraw()
        self.root.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("+%d+%d" % (x, y))

        # This seems to draw the window frame immediately, so only call deiconify()
        # after setting correct window position
        self.root.deiconify()

    def guiMake(self):
        self.label1 = Label(self.frame1, text="\nHow many state do you want ?\n", height=4, font=17)
        self.label1.pack()
        self.E1 = Entry(self.frame1, bd=3, width= 30, font=10)
        self.E1.pack(side=LEFT)
        self.redbutton = Button(self.frame2, text="Make Table", font=10 , command = self.makeTable )
        self.redbutton.pack()

