from student import Student

class Manager:
    def __init__(self):
        self.max_id = 1
        self.list_students = []
        self.read_data()

    def read_data(self):
        try:
            with open('data.txt') as f:
                lines = f.readlines()
                for line in lines:
                    data = line.split(',')
                    s = Student(data[0], data[1], data[2], data[3])
                    self.list_students.append(s)
        except Exception as e:
            print(e)

    def save_data(self):
        with open('data.txt', 'w') as f: #w - write
            for s in self.list_students:
                f.write(str(s))
            
    def increase_id(self):
        self.max_id += 1
        return self.max_id

    def get_max_id(self):
        return self.max_id

    def show_menu(self):
        print('=====================')
        print('1. Danh sách học sinh')
        print('2. Tìm kiếm học sinh')
        print('3. Thêm học sinh')
        print('4. Xóa học sinh')
        print('5. Sửa thông tin học sinh')
        print('6. Thoát chương trình')

    def show_list_student(self):
        for s in self.list_students:
            print(f'{s.id}--{s.name}--{s.age}--{s.student_class}')
    
    def search_student(self, id):
        check = False
        for i, s in enumerate(self.list_students):
            if s.id == id:
                check = True
                print(f'{s.id}--{s.name}')
        if check is False:
            print('Khong tim thay')

    def delete_student(self, id):
        for i, s in enumerate(self.list_students):
            if s.id == id:
                # del(self.list_students[i])
                self.list_students.remove(s)
                # self.list_students.pop(i)

    def edit_student(self, id, name, age, student_class):
        for i, s in enumerate(self.list_students):
            if s.id == id:
                s.name = name
                s.age = age
                s.student_class = student_class

    def add_student(self, name, age, student_class):
        s = Student(self.get_max_id(), name, age, student_class)
        self.list_students.append(s)
        self.increase_id()