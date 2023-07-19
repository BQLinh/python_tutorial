class Human:
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        self.height = 150
    
    def run(self, v):
        print(f'{self.name} is running with {v} km/h!')

hai = Human('Hai', 25)
linh = Human('linh', 25)
ta = Human('Tu Anh', 24)
tom = Human('Tom', 2)

mylist = [linh, ta, hai]

# for i in mylist:
#     if i.name == 'Hai':
#         hai.age = 26
#     print(i.name, i.age)

mylist.insert(7, linh)
# for i in mylist:
#     print(i.name)

# print(mylist[0].name)
# print(mylist[1].name)
# print(mylist[2].name)
# print(mylist[3].name)
# print(mylist[4].name)

mylist.append(hai)
# for i in mylist:
#     print(i.name)

mylist.extend([tom, linh])
for i in mylist:
    print(i.name)

list1 = [1,2,3,4]

list2 = [5,6,7]

# [1,2,3,4,5,6,7]

list3 = list1 + list2

# list1.extend(list2)
print(list3)

list3.remove(7)
list3.pop(0)
print(list3)