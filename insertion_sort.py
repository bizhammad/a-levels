#Task: Using insertion sorting, arrange the following in order.
sort_num = [10, 50, 8, 6, 7, 70, 21, 1]
length_array = len(sort_num)

for x in range(length_array):
    temp = x
    while temp > 0 and sort_num[temp] < sort_num[temp - 1]:
        swap = sort_num[temp]
        sort_num[temp] = sort_num[temp - 1]
        sort_num[temp - 1] = swap
        temp -= 1

print(sort_num)
