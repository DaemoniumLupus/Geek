
from Work_With_Json import Work_With_Json as jso
from Work_With_SQL import Work_With_SQL as sql
from Console_View import Console_View as con
from TKinter_View import TKinter_View as tk

class Phonebook():
    data_class = None
    view_class = None

    def __init__(self,data = 'json',view = 'console'):
        if data == 'json':
            self.data_class = jso()
        elif data == 'sql':
            self.data_class = sql()

        if view == 'console':
            self.view_class = con() 
        else:
            self.view_class = tk()

        
    

    

    def All(self):
        sp = self.data_class.Read()
        self.view_class.Head()
        self.view_class.Write_View(sp)
                    
    def Add(self):
        sp = self.data_class.Read()
        sp = self.view_class.Add_View(sp)
        self.data_class.Load(sp)


                
    def Search(self):
        sp = self.Read()
        search_text = input("Search: ")
        for person in sp:
            if search_text in str(person):
                self.Head()
                self.Data(person,sp)

    def Remove_contact(self) -> dict:
        sp = self.Read()
        while True:
            remove_person = input("Remove(exit -> '-1'): ")
            if remove_person == '-1':
                return sp
            for person in sp:
                if remove_person in str(person):
                    ans = input("Do you want to remove this contact?(Y):")
                    if ans == 'y' or ans == 'Y':
                        del sp[person]
                        print("Contact remove.")
                        return sp
                        

    def Remove_number(self) -> dict:
        sp = self.Read()
        while True:
            remove_person = input("Remove number in contact(exit -> '-1'): ")
            if remove_person == '-1':
                return sp
            for person in sp:
                if remove_person in str(person):
                    self.Data(person,sp)
                    count = len(sp[person]['phones'])
                    if count > 1:
                        print(f"What number you want to remove contact? {[i for i in range(1,count + 1)]}:")
                        i = int(input())
                        print(sp[person]['phones'][int(i)-1])
                        ans = input(f"Do you want to remove this number of contact?(Y):")
                        if ans == 'y' or ans == 'Y':
                            sp[person]['phones'].pop(int(i)-1) 
                            print('Number remove.') 
                            return sp
                    else:
                        print(sp[person]['phones'][0])
                        print(f"Do you want to remove this number of contact?(Y/N):")
                        ans = input(f"Do you want to remove this number of contact?(Y):")
                        if ans == 'y' or ans == 'Y':
                            sp[person]['phones'].pop() 
                            print('Number remove.') 
                            return sp

        
    def Import(self):
        sp = self.Read()
        file = open('phoneimport.txt', 'w')
        file.write(self.Head_file())
        file.write('\n')
        for person in sp:
            file.write(self.Data_file(person,sp))
            file.write('\n')





            
   







