
# from src.calculator import add,sub
from calculator import add,sub

ask = int(input(f"Press 1 : Add  or press 2 : Sub \n" ))

if ask==1:

    inp_1 = int(input(f"Enter 1st number:  "))
    inp_2 = int(input(f"Enter 2nd number:  "))
    result = add(inp_1,inp_2)
    print(f" Result is : {result}")
    
elif ask==2:

    inp_1 = int(input(f"Enter 1st number:  "))
    inp_2 = int(input(f"Enter 2nd number:  "))
    result = sub(inp_1,inp_2)
    print(f" Result is : {result}")


