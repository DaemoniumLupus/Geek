# from tkinter import *
# import sqlite3  
# from tkinter import ttk

import json

# sp = {'дядя коля': {'phones': ['8-800-555-35-35', '8-900-536-35-35'], 'city': 'Сыктыфкар', 'status': 'дядя'},
#        'нюрка': {'phones': ['8-555-549-34-35'], 'city': 'Сыктыфкар', 'status': 'тетя'}}

# conn = sqlite3.connect("phonebook.db")
# cursor = conn.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS names ( 
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 city TEXT,
#                 bithD TEXT);
# """)
   
# cursor.execute("""CREATE TABLE IF NOT EXISTS number (
#                 id_num INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name_id INTEGER NOT NULL,
#                 phone text NOT NULL
#                 )
# """)

# with open ('phonebook.json','w+')as file:
#     file.write(json.dumps(sp,indent=4))
#     file.close()
def Load() -> dict:
    with open("phonebook.json","r") as file:
        sp = json.load(file)
        file.close()
    return sp

def All():
    sp = Load()
    print("{:10}    {:10}  {:10}    {}".format('Name','City','Status','Phones'))
    for person in sp:
        print(f"{person:10} -> {sp[person]['city']:10}  {sp[person]['status']:10} -> {sp[person]['phones']}")
                
def Add():
    f = input('Введите имя нового контакта: ')
    sp = Load()
    exists = True
    for person in sp:
        if f == str(person):
            print('Контакт существует!')
            exists = False
    if exists:
        sp[f] = dict()
        sp[f]['city'] = input(f"{f} -> city: ")
        sp[f]['status'] = input(f"{f} -> status: ")
        sp[f]['phones'] = list()
        coll = int(input('Сколько номеров вы хотите ввести: '))
        while coll > 0:
            sp[f]['phones'].append(input('Введите первый номер: '))
            coll -= 1
        print(f"{'Name':10} -> {'City':10},{'Status':10} -> {'Phones'}")
        for person in sp:
            print(f"{person:10} -> {sp[person]['city']:10},{sp[person]['status']:10} -> {sp[person]['phones']}")
            
def Search():


while True:
    command = input('Введите команду: ')
    if command == '/all':
        print('Вот текущий список номеров') 
        All()
    elif command == '/add':
        Add()
    elif command == "/search":
        search_text = input("Поиск: ")
        # Search(sp,search_text)




            
    #     sp.append(f)
    #     print('Фильм был успешно добавлен в коллекцию!')
    # elif command == '/help':
    #     print('Здесь какойто мануал')


# class Main():
#     def __init__(self):
#         self.window = Tk()
#         self.window.title("Phonebook")
#         self.window.geometry("1000x400+300+200")   

#         btnframe = Frame(self.window,height=100,width=100,borderwidth=1,relief=SOLID)
#         btn_add = Button(btnframe,text="Add Contact")
#         btn_add.pack(side=LEFT,anchor=NW)
#         btn_search = Button(btnframe,text="Search")
#         btn_search.pack(side=LEFT,anchor=N)
#         btnframe.pack(fill=X)

#         columns = ("name", "phone", "email","BD")
#         self.tree = ttk.Treeview(columns=columns,show="headings")
#         self.tree.pack(fill='both',expand=1)

#         self.tree.heading("name",text='Name')
#         self.tree.heading("phone",text="Phone")
#         self.tree.heading("email",text= "Email")
#         self.tree.heading("BD",text="Bith Day")

#         for person in sp:
#             self.tree.insert("",END,values=person)



#         self.window.mainloop()     
#     def Table_print(self):
#         for person in sp:
#             self.tree.insert("",END,values=person)
# def Add(sp: dict):
#     pass



# m = Main()





