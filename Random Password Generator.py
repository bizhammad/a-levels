# Random Password Generator using only random module (Built-in).
# Python Code
# 9618/21/M/J/22 - Question 8 (Pseudocode to Python)

def randomchr():
    import random
    tempvar=random.randint(1, 3)
    if tempvar==1:
        tempchr=random.randint(97, 122)
        return chr(tempchr)
    elif tempvar==2:
        tempchr=random.randint(65, 90)
        return chr(tempchr)
    else:
        tempchr=random.randint(48, 57)
        return chr(tempchr)

pass1= randomchr() + randomchr() + randomchr() + randomchr()
pass2= randomchr() + randomchr() + randomchr() + randomchr()
pass3= randomchr() + randomchr() + randomchr() + randomchr()
print(pass1,"-",pass2,"-",pass3)
