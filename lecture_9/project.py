class Manage:
    def __init__(self) -> None:
        self.students = []

    def show_menu(self):
        print('********************* Menu *********************')
        print('1. Danh sách học sinh')
        print('2. Tìm kiếm học sinh')
        print('3. Thêm học sinh')
        print('4. Xóa học sinh')
        print('0. Exit')
        print('************************************************')

class Student:
    def __init__(self, name, diemtb) -> None:
        self.name = name
        self.diemtb = diemtb

manager = Manage()

while True:
    manager.show_menu()
    key = int(input('Mời bạn nhập 1 lựa chọn: '))
    if key == 1:
        print('Danh sách học sinh')
    elif key == 2:
        print('Tìm kiếm học sinh')
    elif key == 3:
        print('Thêm học sinh')
    elif key == 0:
        print('Thoát chương trình!')
        break   
    else:
        print('Lựa chọn không tồn tại. Mời bạn nhập lại!!')
