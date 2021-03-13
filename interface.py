from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, StringVar
from tkinter.ttk import Frame, Label, Entry, Button, Radiobutton, Combobox
import handler
import db

class MainWindow(Frame):

    def __init__(self):
        super().__init__()
        self.db = db.DB()
        self.handler = handler.Handler()
        self.initUI()


    def initUI(self):

        self.master.title("Text Encryption")
        self.pack(fill=BOTH, expand=True)

        self.frame1 = Frame(self)
        self.frame1.pack()

        self.lbl3 = Label(self.frame1, text="original text", width=25)
        self.lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.txt = Text(self.frame1, width=100, height=10)
        self.txt.pack(fill=BOTH, pady=25, padx=25, expand=True)

        self.frame2 = Frame(self)
        self.frame2.pack()
        self.btn1 = Button(self.frame2, text="process", command=self.pushButton)
        self.btn1.pack()
        self.type = StringVar(self.frame2, "encrypt")
        self.radio1 = Radiobutton(self.frame2, text='encrypt', value='encrypt', variable=self.type)
        self.radio2 = Radiobutton(self.frame2, text='decrypt', value='decrypt', variable=self.type)
        self.radio1.pack()
        self.radio2.pack()


        self.frame5 = Frame(self)
        self.frame5.pack()
        self.lbl4 = Label(self.frame5, text="processed text", width=25)
        self.lbl4.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.txt1 = Text(self.frame5, width=100, height=10)
        self.txt1.pack( pady=25, padx=25 )

        self.frame6 = Frame(self)
        self.frame6.pack()
        self.lbl5 = Label(self.frame6, text="settings", width=10)
        self.lbl5.pack(side=LEFT, anchor=N, padx=5, pady=5)

        #setting up the combo
        allProperties = self.db.getAllProperies()
        comboContent = []
        for x in allProperties:
            comboContent.append(x[1])
        self.combo = Combobox(self.frame6,text= 'preporty', values=comboContent)
        self.combo.pack()

        self.combo.bind('<<ComboboxSelected>>', self.comboModified)

        self.frame7 = Frame(self)
        self.frame7.pack()

        self.lbl6 = Label(self.frame7, text="value", width=10)
        self.lbl6.pack(side=LEFT, anchor=N, padx=5, pady=5)


        self.entry = Entry(self.frame7)
        self.entry.pack()

        self.btn2 = Button(self.frame7, text='Save')
        self.btn2.pack()

    def comboModified(self, event):
        self.entry.delete('0','end')
        self.entry.insert('0',self.db.getPropery(self.combo.get())[0][2])

    def pushButton(self):


        input = (self.txt.get("1.0",'end-1c'))
        #print(self.type.get())
        self.txt1.delete("1.0","end-1c")
        self.txt1.insert("1.0",self.handler.execute(input,self.type.get()))



def main():

    root = Tk()
    root.geometry("600x600+300+300")
    app = MainWindow()
    root.mainloop()


if __name__ == '__main__':
    main()