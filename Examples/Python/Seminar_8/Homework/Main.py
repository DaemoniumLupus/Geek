from Phonebook import Phonebook

pb = Phonebook(data='json',view='tk')


if Phonebook.view_class == 'console':
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

