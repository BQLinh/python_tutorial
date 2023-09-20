
from manager import Manager

manager = Manager()

while True:
    manager.show_menu()
    inp = input('Enter your choice: ')

    if inp == '1':
        print('>>Show all laptops: ')
        manager.show_list_laptop()

    elif inp == '2':
        print('>>Search laptop')
        id_input = input('Moi ban nhap code: ')
        manager.search_laptop_by_code(id_input)

    elif inp == '3':
        print('>>Add laptop:')
        name = input('Enter a name: ')
        code = input('Enter a code: ')
        cost = input('Enter a cost: ')
        link = input('Enter a link: ')
        img = input('Enter an image: ')

        manager.add_laptop(name, code, cost, link, img)
        
    elif inp == '4':
        print('>>')
        id_input = int(input('Enter your ID: '))
        manager.remove_laptop(id_input)
        
    elif inp == '5':
        try:
            print('>>Change informations')
            id = int(input('Enter id: '))
            name = input('Enter a name: ')
            code = input('Enter a code: ')
            cost = input('Enter a cost: ')
            link = input('Enter a link: ')
            img = input('Enter a image: ')
            manager.update_laptop(id, name, code, cost, link, img)
        except:
            print('Ban da nhap sai')

    elif inp == '0':
        manager.save_data()
        print('>>Thoát')
        break
    else:
        print('Mời bạn nhập lại')
