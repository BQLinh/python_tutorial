# Tạo 1 chương trình quản lý danh sách học viên gồm các chức năng:
# + hiển thị menu:
#     1. Hiển thị danh sách học sinh
#     2. Tìm kiếm học sinh => hiện thị thông tin học sinh đó
#     3. Thêm học sinh
#     4. Xóa học sinh
#     5. Sửa thông tin học sinh
#     6. Thoát chương trình
# + chức năng: người sẽ thực hiện các chức năng tương ứng khi nhập từ 1-6
# + nếu người dùng nhập sai => nhập lại
# + học sinh gồm các thuộc tính:ID, name, age, class

from manager import Manager

manager = Manager()
while True:
    manager.show_menu()
    inp = input('Moi ban nhap 1 so: ')

    if inp == '1':
        print('>>Danh sách học sinh: ')
        manager.show_list_student()

    elif inp == '2':
        print('>>Tìm kiếm học sinh')
        id_input = int(input('Moi ban nhap id: '))
        manager.search_student(id_input)

    elif inp == '3':
        print('>>Thêm học sinh')
        # id = int(input('Moi ban nhap id: '))
        name = input('Moi ban nhap ten: ')
        age = int(input('Moi ban nhap tuoi: '))
        student_class = input('Moi ban nhap class: ')
        manager.add_student( name, age, student_class)
        
    elif inp == '4':
        print('>>Xóa học sinh')
        id_input = int(input('Moi ban nhap id: '))
        manager.delete_student(id_input)
        
    elif inp == '5':
        try:
            print('>>Sửa thông tin học sinh')
            id = int(input('Moi ban nhap id: '))
            name = input('Moi ban nhap ten: ')
            age = int(input('Moi ban nhap tuoi: '))
            student_class = input('Moi ban nhap class: ')
            manager.edit_student(id, name, age, student_class)
        except:
            print('Ban da nhap sai')

    elif inp == '0':
        manager.save_data()
        print('>>Thoát')
        break
    else:
        print('Mời bạn nhập lại')


# add average_score field => min, max
# search by id and name
# find student have average_score > 8
# find student rank: good(>=8), normal(5-8), not pass(5 > ) 
