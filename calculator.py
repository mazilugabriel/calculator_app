from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
should_continue = True

while should_continue:
    num1 = int(input("Please enter your first number:"))
    for symbol in operations:
        print(symbol)
    operations_symbol = input("Please choose a operation")
    num2 = int(input("Please enter your seccond number:"))
    calculation_function = operations[operations_symbol]
    answare = calculation_function(num1, num2)
    
    print(f"{num1} {operations_symbol} {num2} = {answare}")
    if input("Type 'y' to continue: ") == "y":
        num1 = answare
    else:
        should_continue = False