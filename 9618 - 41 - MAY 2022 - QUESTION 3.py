# Question 3 
# 9618/41 May 2022

# 3 A
global tailpointer
global headpointer
QueueArray = ["","","","","","","","","",""]  # Queue Array Declared as array (string) + 10 empty strings in queue
headpointer = 0 # Headpointer Declared as integer and zero assigned
tailpointer = 0 # Tailpointer Declared as integer and zero assigned


# 3 B
global numberitems
numberitems = 0

def enqueue(DataToAdd):
    global numberitems
    global tailpointer
    global headpointer
    if numberitems == 10 :
        return False
    QueueArray[tailpointer] = DataToAdd
    if tailpointer>= 9:
        tailpointer = 0
    else:
        tailpointer = tailpointer + 1
    numberitems = numberitems + 1
    return True


# 3 C
def dequeue():
    global numberitems
    global headpointer
    if numberitems == 0 :
        return False
    Currentpointer = headpointer
    if headpointer>= 9:
        headpointer = 0
    else:
        headpointer = headpointer + 1
    numberitems = numberitems - 1
    QueueArray[Currentpointer] = ''

# 3 D
for x in range(0,11):
    y = input("Enter the Value you want to store: ")
    if enqueue(y) == True:
        print(" Value was Added")
    else:
        print("Stack Full")
print("Stack: ", QueueArray)
dequeue()
dequeue()
print("Stack after DeQueue: ", QueueArray)