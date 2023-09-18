my_list = ['1,Hai,18,12 \n', '2,Tu Anh, 17, 11 \n']

with open("data2.txt", mode="wt") as f:
    f.writelines(my_list)