# các giá trị trong list có thể :
# - thay đổi được
# - sắp xếp
# - trùng lặp 
# - có chỉ mục
my_list = ['linh', 'pi', 'tui', 1, 2]
for i in my_list:
    print(i)

# access 1 item
my_list[2]

my_list[-1]

my_list[1:3]

# change list item
my_list[1] = 'tom'

my_list[1: 4]= ['1', '2', '3']

my_list[1:2] = ['linh']

# insert a value
my_list.insert(1 , 'bobo')

# thêm giá trị vào cuối list
my_list.append('tom')

# thêm 1 list khác vào cuối list
my_list.extend([6, 'hehe'])

# xóa 1 phần tử theo giá trị
my_list.remove('hehe')

# xóa 1 phần tử theo index
my_list.pop(2)

# xóa bằng del
del(my_list[4])

# xóa bằng clear
# my_list.clear()

# list comprehension : newlist = [expression for item in iterable if condition == True]
[print(i) for i in my_list ]

my_list = ['das', 'asd', 'sda']
# sort
my_list.sort()


# copy a list
b = my_list
print(b)
print(my_list)

my_list[2] = 'ttttt'
print(b)
print(my_list)

# use copy()
my_list2 = my_list.copy()
# or
my_list2 = list(my_list)

my_list[2] = '1231'
print(my_list2)

# cộng 2 list 
new_list = my_list + my_list2