# def print_text(text): 
#     print(text) 
    
# text = input("Write anything you want: ")

# print_text(text) 

def calculator(num_x, num_y, operation, close_calculator):
    if operation == "1": 
        total_sum = num_x + num_y
    elif operation == "2": 
        total_sum = num_x - num_y 
    elif operation == "3": 
        total_sum = num_x * num_y 
    elif operation == "4": 
        total_sum = num_x / num_y 
    else: 
        print("Sorry, this operation doesn't exist. ")

    print(f"The total sum is {total_sum}")

    close_calculator = input("Do you want to close the calculator? ")
    if close_calculator == "no": 
        start_calculator()  


def start_calculator(): 
    num_x = int(input("Select a number: "))
    num_y = int(input("Select another number: "))
    operation = input("Choose an operation: 1-sum, 2-subtraction, 3-multiplication, 4-division: ")
    close_calculator = "no" 

    calculator(num_x, num_y, operation, close_calculator)


start_calculator()





