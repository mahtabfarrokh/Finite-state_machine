import tkinter as tk
import graph
class SimpleTableInput(tk.Frame):
    def __init__(self , rows, columns):
        tk.Frame.__init__(self)

        self._entry = {}
        self.rows = rows
        self.columns = columns
        self.root = tk.Tk()

        self.centerWindow()
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.frame1 = tk.Frame(self.frame)
        self.frame1.pack()

        self.frame2 = tk.Frame(self.frame)
        self.frame2.pack(side=tk.BOTTOM)

        self.frame3 = tk.Frame(self.frame2)
        self.frame3.pack()

        self.frame4 = tk.Frame(self.frame2)
        self.frame4.pack(side=tk.BOTTOM)

        self.frame5 = tk.Frame(self.frame4)
        self.frame5.pack()

        self.frame6 = tk.Frame(self.frame4)
        self.frame6.pack(side=tk.BOTTOM)


        self.createTable()
        self.root.mainloop()

    def createTable (self) :
        # create the table of widgets
        for col in range(self.columns) :
            l = tk.Label(self.frame1 , text = col  , font =10 ,relief=tk.RIDGE )
            l.grid(row =0  , column = col+1 , stick="nsew")
        for row in range(self.rows+1) :
            if (row ==0 ) :
                l = tk.Label(self.frame1, text="state", font=8 , relief=tk.RIDGE)
                l.grid(row=0, column=0, stick="nsew")
                continue
            l = tk.Label(self.frame1, text=row -1 , font=10 , relief=tk.RIDGE)
            l.grid(row=row , column= 0, stick="nsew")
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self.frame1 , validate="key" ,bd=3, width= 10, font=10)
                e.grid(row=row +1 , column=column +1 , stick="nsew")
                self._entry[index] = e

        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column+1 , weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(self.rows +2 , weight=1)


        l = tk.Label(self.frame3, text="Enter start state  : ", font=7)
        l.pack(side = "left")
        self.e = tk.Entry(self.frame3 ,validate="key" ,bd=3, width= 12, font=10 )
        self.e.pack(side = "right")
        l1 = tk.Label(self.frame5, text="Enter finish state : ", font=7)
        l1.pack(side="left")
        self.e1 = tk.Entry(self.frame5, validate="key", bd=3, width=12, font=10)
        self.e1.pack(side="right")

        self.submit = tk.Button(self.frame6 , text="Make Graph", command=self.onMakeGraph , font=10)
        self.pack(side="bottom", fill="both", expand=True)
        self.submit.pack(side="bottom")

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result
    def onMakeGraph(self):
        print(self.get())
        print("go to graph")
        print ("")
        graph.Graph(self.get() , self.e.get() , self.e1.get().split(','), self.rows)
        self.root.destroy()

    def centerWindow (self) :
        self.root.withdraw()
        self.root.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("+%d+%d" % (x, y))

        # This seems to draw the window frame immediately, so only call deiconify()
        # after setting correct window position
        self.root.deiconify()

