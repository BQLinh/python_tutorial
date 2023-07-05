# Tạo 1 menu gồm các mục
# 1- Danh sách học sinh
# 2- Tìm kiếm học sinh
# 3- Thêm học sinh
# 4- Xóa học sinh
# 0- Thoát

# khi người dùng ấn 1 => In ra "Danh sách học sinh"
# khi người dùng ấn 2 => In ra "Tìm kiếm học sinh"
# khi người dùng ấn 3 => In ra "Thêm học sinh"
# khi người dùng ấn 4 => In ra "Xóa học sinh"
# khi người dùng ấn 0 => In ra "Thoát" 
# trường hợp khác => "In ra mời bạn nhập lại"
# *khi người dùng ấn 0 thì ngừng chương trình, nếu không thì chương trình sẽ tiếp tục nhập


while True:
    print('===========================')
    print('1. Danh sách học sinh')
    print('2. Tìm kiếm học sinh')
    print('3. Thêm học sinh')
    print('4. Xóa học sinh')
    print('0. Thoát')
    print('===========================')

    lua_chon = input('Moi ban chon: ')
    
    if lua_chon == '1':
        print('>>Danh sách học sinh')
    elif lua_chon == '2':
        print('>>Tìm kiếm học sinh')
    elif lua_chon == '3':
        print('>>Thêm học sinh')
    elif lua_chon == '4':
        print('>>Xóa học sinh')
    elif lua_chon == '0':
        print('>>Thoát')
        break
    else:
        print('>>In ra mời bạn nhập lại')