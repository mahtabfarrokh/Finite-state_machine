from graphviz import Digraph
from subprocess import check_call
import tkinter as tk
class Vertex () :
    def __init__(self , a , state ):
        self.a = a
        self.state = state
class Graph () :
    def __init__(self, list,start , finish ,  stateNumer):
        self.list = list
        self.stateNumber = stateNumer
        self.startState = start
        self.finishState = finish
        self.zoomNum = 3
        self.start = False
        self.imageWidth =0
        self.imageHeight =0
        self.mark = []
        for i in range(self.stateNumber) :
            self.mark.append(0)

        self.root = tk.Toplevel()

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(side="bottom")

        self.frame2 = tk.Frame(self.frame1)
        self.frame2.pack()

        self.frame3 = tk.Frame(self.frame1)
        self.frame3.pack(side="bottom")

        self.centerWindow()
        self.dot = Digraph(comment='The Round Table')

        self.visited= []
        self.adjacent =[]
        self.makeGraph()
        self.root.mainloop()
    def makeDotFile (self ) :

        self.dot = Digraph(comment='The Round Table')

        self.dot.attr('node', shape="point")
        self.dot.node("s")
        for i in range(self.stateNumber):
            if (str(i) in self.finishState):

                self.dot.attr('node', shape='doublecircle')
                self.dot.node(str(i))
               # self.dot.attr(str(i), shape="doublecircle")
            elif (str(i) == self.startState):
                pass
            else:
                self.dot.attr('node', shape="circle")
                self.dot.node(str(i))
        self.dot.edge("s", str(self.startState),"start" , constraint='false')
        for i in range(self.stateNumber):
            v = self.list[i]
            for j in range(self.stateNumber):
                e = v[j]
                if (e is not ''):
                    for ch in e.split(','):
                        self.dot.edge(str(i), str(j), ch, constraint='false')
       # print(self.dot.source)
        self.dot.render('test-output/round-table.gv', view=False)

        # draw graph file :

        check_call(['dot', '-Tgif', 'test-output/round-table.gv', '-o', 'test-output/OutputFile.gif'])
        if (self.imageHeight== 0) :
            photo = tk.PhotoImage(file='test-output/OutputFile.gif' )
            self.imageHeight = photo.height()
            self.imageWidth = photo.width()
        else:
            photo = tk.PhotoImage(file='test-output/OutputFile.gif' , width = self.imageWidth , height = self.imageHeight)
        photo = photo.zoom(3,3)

        lbl = tk.Label(self.frame, image=photo )
        lbl.image = photo  # keeping a reference in this line
        lbl.configure(image=photo)
        lbl.grid(row=0, column=0 )

       # lbl.pack(side="bottom", fill="both", expand="yes")




    def adjacentListDraw (self) :
        self.adjacent = []
        l = tk.Label(self.frame2, text="state", font=8, relief=tk.RIDGE)
        l.grid(row=0, column=0, sticky="nsew")
        l = tk.Label(self.frame2, text="adjacent", font=8, relief=tk.RIDGE)
        l.grid(row=0, column=1, sticky="nsew")
        for i in range(self.stateNumber):
            v = self.list[i]
            l = tk.Label(self.frame2, text=str(i), font=8, relief=tk.RIDGE)
            l.grid(row=i + 1, column=0, sticky="nsew")
            strL = ""
            listE = []
            for j in range(self.stateNumber):
                e = v[j]

                if (e is not ''):
                    a = []
                    for ch in e.split(','):
                        strL = strL + "(" + str(j) + " , " + ch + ")"
                        a.append(ch)
                    listE.append(Vertex(a, j))
            self.adjacent.append(listE)
            l = tk.Label(self.frame2, text=strL, font=8, relief=tk.RIDGE)
            l.grid(row=i + 1, column=1, sticky="nsew")

    def makeGraph (self) :

        self.makeDotFile()


        # draw adjacent list :
        self.adjacentListDraw()
        #find string :
        l = tk.Label(self.frame3, text="Find String :", font=8 )
        l.grid(row=0, column=0, sticky="nsew")
        self.e = tk.Entry(self.frame3 ,validate="key" ,bd=3, width= 12, font=10)
        self.e.grid(row=0, column=1, sticky="nsew")
        self.e.bind('<Return>', self.findString)

        #find loop :
        self.visited.clear()
        loop =  self.findLoop()
        loop = True
        if loop :
           l2 = tk.Label(self.frame3, text="There is loop", font=8)
           l2.grid(row=1, column=0, sticky="nsew")
           self.b = tk.Button(self.frame3 , text="Delete Loop" , font =8 , command = self.deleteLoop)
           self.b.grid(row=1, column=1 , sticky="nsew")
        else :
            l = tk.Label(self.frame3, text="There is not loop", font=8)
            l.grid(row=1 , column=0, sticky="nsew")

    def dfs(self, i):
        self.visited.append(i)
        self.mark[i] = 1
        j = 0
        for ver in self.list[i]:
            if (ver is not ''):
                if (self.mark[j]==1):
                    v = self.list[i]
                    v[j] = ''
                    return False
                else:
                    self.dfs(j)
            j += 1
        self.mark[i] = 2
        return True

    def deleteLoopNode(self, i):
        self.mark = [0]* self.stateNumber
        self.dfs(i)
        self.visited.clear()

    def deleteLoop (self) :

        for i in range(self.stateNumber) :
            k = self.list[i]
            k[i] = '0'
            print("list : " , k)
        self.deleteLoopNode(int(self.startState))
        for i in range(self.stateNumber):
            self.deleteLoopNode(int(i))
        self.makeDotFile()
        self.adjacentListDraw()
        l = tk.Label(self.frame3, text="loop deleted", font=8)
        l.grid(row=1, column=0, sticky="nsew")
        self.b.destroy()


    def loopDFS (self , i ) :
        self.visited.append(i)
        self.mark[i] = 1
        j = 0
        for ver in self.list[i]:
            if (ver is not ''):
                if(self.mark[j] == 1):
                    return False
                else:
                    self.dfs(j)
            j += 1
        self.mark[i] = 2
        return True

    def findLoop (self ) :

        for i in range(int(self.stateNumber)) :
            self.mark = [0] * self.stateNumber
            if not self.loopDFS(int(i))  :
                return True
        return False

    def findPartOfString(self , currentState , eString) :
        if eString =="" and (str(currentState) in self.finishState)  :
            return True
        elif eString =="" :
            return False
        f = False
        ch = eString[0]
        for adj in self.adjacent[currentState]:
            if ch in adj.a:
                f = f or self.findPartOfString(int(adj.state) ,eString[1:])
        if f :
            return True
        else:
            return False

    def findString (self , event ) :
        currentState = int(self.startState)
        b = self.findPartOfString(currentState , self.e.get())
        if b :
            l = tk.Label(self.frame3, text=" True", fg="green", font=8)
            l.grid(row=0, column=2, sticky="nsew")
        else :
            l = tk.Label(self.frame3, text=" False", fg="red", font=8)
            l.grid(row=0, column=2, sticky="nsew")
        return
    def centerWindow(self):
        self.root.withdraw()
        self.root.update_idletasks()  # Update "requested size" from geometry manager

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("+%d+%d" % (x, y))

        # This seems to draw the window frame immediately, so only call deiconify()
        # after setting correct window position
        self.root.deiconify()