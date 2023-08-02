# print('hello')

# x = int(input('moi ban nhap x: '))

# if x == 1:
#     print('x =1')
# elif x > 1:
#     print('x > 1')
# else:
#     print('x < 1')

# i = 1
# while i < 10:
#     print(i)
#     i += 1

# for i in range(1, 10):
#     print(i)

# mylist = []

# def hello(name):
#     print('Xin chao ban', name)

# hello('linh')
# hello('tom')

class SinhVien:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def greeting(self):
        print(f'Xin chao {self.name}')

sv1 = SinhVien(1, 'linh')
print(sv1.id, sv1.name)
# print(sv1.name)

sv2 = SinhVien(2, 'tom')
print(sv2.id, sv2.name)
# print(

sv2.greeting()
