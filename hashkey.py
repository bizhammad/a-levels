
array1d=[0,0,0,0]
maxval=len(array1d)


def hashkey(x):
    divi= x % maxval 
    turn = 0
    if divi > maxval:
        divi=maxval
    done = False
    while done == False:
            if array1d[divi]==0:
                 array1d[divi]=x
                 print("value stored")
                 done=True
            elif turn > maxval:
                 print("Stack Full")
                 done=True
            else:
                 divi = divi + 1
                 turn = turn + 1
        

for i in range(0,6):
     inputtostore = int(input("Input the value you want to store : "))
     hashkey(inputtostore)
     

