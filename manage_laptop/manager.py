from laptop import Laptop

class Manager:
    def __init__(self):
        self.max_id = 0
        self.list_laptop = []
        self.load_data()

    def crawl(self):
        pass

    def load_data(self):
        try:
            with open('data.txt') as f:
                lines = f.readlines()
                for line in lines:
                    data = line.split(',')
                    s = Laptop(self.new_id(),data[0], data[1], data[2], data[3], data[4])
                    self.list_laptop.append(s)
        except Exception as e:
            print(e)

    def save_data(self):
        with open('data.txt', 'w') as f:
            for s in self.list_laptop:
                f.write(str(s))

    def new_id(self):
        self.max_id += 1
        return self.max_id 

    def show_menu(self):
        print('''
==================================
1. Show list laptop
2. Search laptop
3. Add new laptop
4. Delete laptop
5. Update laptop
6. Crawl laptops
0. Quit
==================================''')

    def add_laptop(self, name, code, cost, link, img):
        laptop = Laptop(self.new_id(), name, code, cost, link, img)
        self.list_laptop.append(laptop)

    def show_list_laptop(self):
        for laptop in self.list_laptop:
            print(laptop)

    def remove_laptop(self, id):
        laptop = self.search_laptop_by_id(id)
        self.list_laptop.remove(laptop)

    def update_laptop(self, id, name, code, cost, link, img):
        laptop = self.search_laptop_by_id(id)
        if laptop is not None:
            laptop.name = name
            laptop.code = code
            laptop.cost = cost
            laptop.link = link
            laptop.img = img
            laptop.save()
        else:
            print('No laptop founded')

    def search_laptop_by_code(self, key):
        is_founded = False
        for laptop in self.list_laptop:
            if key == laptop.code:
                print(laptop)
                is_founded = True

        if not is_founded:
            print('No laptop founded')

    def search_laptop_by_id(self, key):
        for laptop in self.list_laptop:
            if key == laptop.id:
                return laptop
        return None