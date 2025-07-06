def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y
print("Welcome to the Basic Calculator")
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
while True:
    user_choice = input("Enter choice (1/2/3/4): ")
    if user_choice in ('1', '2', '3', '4'):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter only numbers.")
            continue
        if user_choice == '1':
            print("Result:", addition(a, b))
        elif user_choice == '2':
            print("Result:", subtraction(a, b))
        elif user_choice == '3':
            print("Result:", multiplication(a, b))
        elif user_choice == '4':
            print("Result:", division(a, b))
        again = input("Do you want to perform calculation again? (yes/no): ")
        if again.lower() != 'yes':
            break
    else:
        print("Invalid Input. Please choose only 1, 2, 3 or 4.")
