#Task: Sort the following in accesing order using bubble sorting
sort_num = [10, 50, 8, 6, 7, 70, 21, 1]
swap=True
range_num=7

while swap:
    swap=False
    for i in range (range_num):
        if sort_num[i] > sort_num[i+1]:
            temp=sort_num[i+1]
            sort_num[i+1]=sort_num[i]
            sort_num[i]=temp
            swap=True
print(sort_num)