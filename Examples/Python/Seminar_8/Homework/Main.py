

import json


def Load(sp):
    with open ('phonebook.json','w')as file:
        file.write(json.dumps(sp,indent=4))
        file.close()

def Head():
    print("{:15}    {:10}  {:10}    {}".format('Name','City','Status','Phones'))

def Data(person,sp):
    print ("{:15} -> {:10}  {:10} -> {}".format(person,sp[person]['city'],sp[person]['status'],sp[person]['phones']))

def Head_file() -> str:
    st = "{:15}    {:10}  {:10}    {}".format('Name','City','Status','Phones')
    return st

def Data_file(person,sp) -> str:
    st = "{:15} -> {:10}  {:10} -> {}".format(person,sp[person]['city'],sp[person]['status'],sp[person]['phones'])
    return st

def Read() -> dict:
    with open("phonebook.json","r") as file:
        sp = json.load(file)
        file.close()
    return sp

def All():
    sp = Read()
    Head()
    for person in sp:
        Data(person,sp)
                
def Add():
    new_name = input('Enter name new contact: ')
    sp = Read()
    exists = True
    for person in sp:
        if new_name == str(person):
            ans = input('Contact exists!\nDo you want add number this contact(Y):')
            while ans == 'y' or ans == 'Y':
                sp[person]['phones'].append(input("Enter number:"))
                ans = input("Enter one more?(Y):")
            exists = False
    if exists:
        sp[new_name] = dict()
        sp[new_name]['city'] = input(f"{new_name} -> city: ")
        sp[new_name]['status'] = input(f"{new_name} -> status: ")
        sp[new_name]['phones'] = list()
        coll = int(input('How many numbers you want input?: '))
        count = 1
        while count <= coll:
            sp[new_name]['phones'].append(input('Enter the number {count}: '))
            count += 1
    Load(sp)


            
def Search():
    sp = Read()
    search_text = input("Search: ")
    for person in sp:
        if search_text in str(person):
            Head()
            Data(person,sp)

def Remove_contact() -> dict:
    sp = Read()
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
                    

def Remove_number() -> dict:
    sp = Read()
    while True:
        remove_person = input("Remove number in contact(exit -> '-1'): ")
        if remove_person == '-1':
            return sp
        for person in sp:
            if remove_person in str(person):
                Data(person,sp)
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

    
def Import():
    sp = Read()
    file = open('phoneimport.txt', 'w')
    file.write(Head_file())
    file.write('\n')
    for person in sp:
        file.write(Data_file(person,sp))
        file.write('\n')



while True:
    command = input('Enter the command: ')
    if command == '/all':
        print('Contact list: ') 
        All()
    elif command == '/add':
        Add()
    elif command == '/search':
        Search()
    elif command == '/remove_contact':
        sp = Remove_contact()
        Load(sp)
    elif command == '/remove_number':
        sp = Remove_number()
        Load(sp)
    elif command == '/import':
        Import()





            
   







