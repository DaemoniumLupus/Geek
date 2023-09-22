class Console_View():
    def __init__(self) -> None:
        pass
    
    def Head(self):
        print("{:15}    {:10}  {:10}    {}".format('Name','City','Status','Phones'))

    def Data(self,person,sp):
        print ("{:15} -> {:10}  {:10} -> {}".format(person,sp[person]['city'],sp[person]['status'],sp[person]['phones']))

    def Write_View(self,sp: dict):
        for person in sp:
            self.Data(person,sp)

    def Add_View(self,sp: dict) -> dict:
        new_name = input('Enter name new contact: ')
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
                sp[new_name]['phones'].append(input(f'Enter the number {count}: '))
                count += 1
        return sp
    
    def MainLoop(self):
        while True:
            command = input('Enter the command: ')
            if command == '/all':
                print('Contact list: ') 
                pb.All()
            elif command == '/add':
                pb.Add()
            elif command == '/search':
                pb.Search()
            elif command == '/remove_contact':
                sp = pb.Remove_contact()
                pb.data_class.Load(sp)
            elif command == '/remove_number':
                sp = pb.Remove_number()
                pb.Load(sp)
            elif command == '/import':
                pb.Import()

