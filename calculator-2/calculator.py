"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("Please enter your equation > ")
    user_input = user_input.split(' ')
    # for item in user_input:
    #     if item.hasdigit:
    #         item = float(item)
    total = 0
    x=1
    while x < len(user_input): 
        user_input[x] = float(user_input[x])
        x += 1
    if user_input[0] == "q":
        break

    elif user_input[0] == "+":
        total = add(user_input[1], user_input[2])
        
    elif user_input[0] == "-":
        total = subtract(user_input[1], user_input[2])

    elif user_input[0] == "*":
        total = multiply(user_input[1], user_input[2])

    elif user_input[0] == "/":
        total = divide(user_input[1], user_input[2])
    
    elif user_input[0] == "square":
        total = square(user_input[1])
    
    elif user_input[0] == "cube": 
        total = cube(user_input[1])
    
    elif user_input[0] == "pow":
        total = power(user_input[1], user_input[2])
    
    elif user_input[0] == "mod":
        total = mod(user_input[1], user_input[2])
    
    else: 
        total = "Please enter a valid equation"

    print(total)




    
    


    





    