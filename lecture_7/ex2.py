class Human:
    def __init__(self, my_name, my_age):
        self.name = my_name
        self.age = my_age
        self.eyes = None

    def speak(self):
        print('hello my name is', self.name)

    def run(self, speed):
        print(self.name, 'is running with speed', speed)


linh = Human('linh', 25)
linh2 = Human('linh2', 24)
minh = Human('minh', 20)
tom = Human('tom', 2)
pi = Human('pi', 5)


mylist = [linh, linh2, minh, tom, pi]

# mylist2 = [tom, pi]

# for i in mylist:
#     print(i.name)

# mylist.append(pi)
# mylist.insert(1, pi)

# mylist[2].name = 'Minh 2'

# mylist.extend(mylist2)

for i in mylist:
    if i.name == 'minh':
        i.name = 'Minh2'

for i in mylist:
    print(i.name)

