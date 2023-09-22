from tkinter import *

class TKinter_View():
    def __init__(self):
        self.window = Tk()
        self.window.title('Phonebook')
        self.window.geometry('500x400+400+200')

        btnFrame = Frame()
        btnFrame.pack()

        btnAdd = Button(btnFrame,command=self.WindowAdd,text='Add contact')
        btnAdd.pack()

        self.window.mainloop()

        

    def Head(self):
        pass
    def Data(self,person,sp):
        pass
    def Add_View(self,sp: dict) -> dict:
        return sp
    
    def WindowAdd(self):
        window_Add = Tk()
        window_Add.geometry('300x200+500+300')
        window_Add.title('Add new')
        window_Add.mainloop()
