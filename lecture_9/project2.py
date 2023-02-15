class Student:
    def __init__(self, name, age, diemtb) -> None:
        self.name = name
        self.age = age
        self.diemtb = diemtb


class Manager:
    def __init__(self):
        self.list_students = []

    def show_menu(self):
        print('******************** Menu ********************')
        print('1. Danh sach hoc sinh')
        print('2. Tim kiem hoc sinh')
        print('3. Them hoc sinh')
        print('4. Xoa hoc sinh')
        print('5. Sua thong tin hoc sinh')
        print('0. Exit')
        print('**********************************************')

    def show_list_student(self):
        for student in self.list_students:
            print('>>Ten: ' + student.name + '--- Age: ' + str(student.age))

    def create_student(self, name, age, diemtb):
        new_student = Student(name, age, diemtb)
        self.list_students.append(new_student)

    def delete_student(self):
        # xoá phần tử khỏi list_student
        pass

manager = Manager()

while True:
    manager.show_menu()
    key = input('Moi ban lua chon: ')

    if key == '1':
        print('Danh sach hoc sinh:')
        manager.show_list_student()
    elif key == '2':
        print(' Tim kiem hoc sinh')
    elif key == '3':
        print('Them hoc sinh: ')
        name = input('Moi ban nhap ten: ')
        age = int(input('Moi ban nhap tuoi'))
        diemtb = float(input('Moi ban nhap diem trung binh'))
        manager.create_student(name, age, diemtb)

    elif key == '4':
        print('Xoa hoc sinh')
    elif key == '0':
        break
    else:
        print('Moi ban nhap lai')

