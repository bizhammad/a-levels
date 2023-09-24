array_1d = [2,4,5,6,7,9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127,171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207, 209, 211, 213, 215]


def fin_num(input_num):
    lenght=len(array_1d)
    right=lenght
    left=0
    found=True
    temp2=0

    while found==True:
        midpoint= (right + left)//2
        print("Current Midpoint is ", array_1d[midpoint])  #for tracing the program position
        temp1=midpoint
        temp3=temp2
        temp2=temp1
        if temp1==temp2 and temp2==temp3:
            print("Not found in list")
            found=False
            break
        elif input_num==array_1d[midpoint]:
            print("Number Found")
            found=False
            break
        elif input_num>array_1d[midpoint]:
            left=midpoint

        elif input_num<array_1d[midpoint]:
            right=midpoint

print("Input the Num you want to search in the array: ")
fin_num(int(input()))
input()
    


    

    
