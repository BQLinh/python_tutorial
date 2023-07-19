# Viết fucntion với giá trị đầu vào là ‘hello', Kiểm tra name có nằm trong các list sau
list1 = ['hellolinh', 'hehe', 'xin chao', 'hello']
list2 = ['tom', 'james', 'linda', 'pi']


def find(arr):
    if 'hello' in arr:
        print('hello nam trong arr')
    else:
        print('hello ko nam trong arr')

def find(arr):
    for i in arr:
        if i == 'hello':
            print('hello nam trong arr')
            break
    else:
        print('hello ko nam trong arr')

find(list2)
