# def print_text(text):
#     print(text)

# text = input("Write something: ")

# print_text(text)


def calculator(numberA, numberB, operation, close_calculator):
    if operation == "sum":
        total_sum = numberA + numberB
    elif operation == "subtraction":
        total_sum = numberA - numberB
    elif operation == "multiplication":
        total_sum = numberA * numberB
    elif operation == "division":
        total_sum = numberA / numberB
    else:
        print("Sorry, this operation doesn't exist.")
    
    print(f"The total sum is {total_sum}")

    close_calculator = input("Do you want to close the calculator? ")
    if close_calculator == "no":
        start_calculator()
        

def start_calculator():
    numberA = int(input("Choose a number: "))
    numberB = int(input("Choose another one: "))
    operation = input("Choose an opeation: 1-sum, 2-subtraction, 3-multiplication, 4-division: ")
    close_calculator = "no"

    calculator(numberA, numberB, operation, close_calculator)


start_calculator()
