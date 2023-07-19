# Viết fucntion in ra số lớn nhất trong các list sau
list_1 =  [1,2,3,7,0,2,17,11,19,40,21]
list_2 =  [100, 123,564,789,543,943,921]
list_3 =  [9021,6434,6465,7674,8756,9656,2434]

def find_max(arr):
    m = arr[0]
    for i in arr[1:]:
        if i > m:
            m = i
    return m

a = find_max(list_1)
print(a)

a = find_max(list_2)
print(a)

a = find_max(list_3)
print(a)