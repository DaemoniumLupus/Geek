# elif choice == "Загрузить БД":  #если выбрали этот пункт
#             # загрузить из json
#             fname=fileopenbox('Выберите файл формата JSON')  #открываем файл
#             with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
#                 BD = json.load(fh)  # загружаем из файла данные в словарь data
#             print('БД успещно загружена')
#             loaded=True #меняем флаг загрузки БД
#         elif choice=='Сохранить БД': #если выбрали этот пункт
#             # сохранить в json
#             with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
#                 fh.write(json.dumps(BD,
#                                     ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
#             print('БД успещно сохранена')

def All(sp: dict):
    for item in sp:
        print(f"{item} {sp[item]['phones']}")

def Search(sp: dict,text):
    for item in sp:
        print(type(item))
        if text in item:
          print(f"{item} {sp[item]['phones']}")
        else:
            print("Не найдено!")
            break
        
            

def Add(sp: dict):
    pass


sp = {'дядя коля': {'phones': ['8-800-555-35-35', '8-900-536-35-35'], 'город': 'Сыктыфкар', 'Статус': 'дядя'},
       'нюрка': {'phones': ['8-555-549-34-35'], 'город': 'Сыктыфкар', 'Статус': 'тетя'}}



while True:
    command = input('Введите команду: ')
    if command == '/all':
        print('Вот текущий список номеров') 
        All(sp)
    elif command == '/add.contact':
        f = input('Введите имя нового контакта: ')
        if f in sp:
            print('Контакт существует!')
        else:
            coll = int(input('Сколько номеров вы хотите ввести: '))
            while coll != 0:
                nambers = input('Введите первый номер: ')
    elif command == "/search":
        search_text = input("Поиск: ")
        Search(sp,search_text)




            
    #     sp.append(f)
    #     print('Фильм был успешно добавлен в коллекцию!')
    # elif command == '/help':
    #     print('Здесь какойто мануал')





