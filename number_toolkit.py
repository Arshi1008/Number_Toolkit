def get_number(message):
    while True:                          
        num = input(message).strip()    
        if num.isdecimal():             
            return int(num)             
        print("Invalid input! Please enter a whole number (0 or greater).")

def factorial(n):
    result = 1                           
    for i in range(2, n + 1):            
        result = result * i
    return result

def fibonacci_series(n):
    series = []                          
    a, b = 0, 1                          
    for i in range(n):                   
        series.append(a)                 
        a, b = b, a + b                  
    return series

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10                   
        rev = rev * 10 + digit  
        n = n // 10                      
    return rev

def is_prime(n):
    if n < 2:                            
        return False
    i = 2
    while i * i <= n:                    
        if n % i == 0:                   
            return False
        i = i + 1
    return True                          

def gcd(a, b):
    while b != 0:
        a, b = b, a % b                  
    return a

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        rem = n % 2                
        binary = str(rem) + binary 
        n = n // 2
    return binary

def sum_of_digits(n):
    total = 0
    while n > 0:
        total = total + n % 10           
        n = n // 10                     
    return total

def swap_numbers(a, b):
    a, b = b, a                          
    return a, b

def show_menu():
    print("\nNUMBER TOOLKIT")
    print("1. Factorial")
    print("2. Fibonacci series")
    print("3. Reverse a number")
    print("4. Prime number check")
    print("5. GCD of two numbers")
    print("6. Decimal to binary")
    print("7. Sum of digits")
    print("8. Swap two numbers")
    print("0. Exit")

def main():
    print("Welcome to the Number Toolkit!")
    while True:                          
        show_menu()
        choice = get_number("Enter your choice (0-8): ")

        if choice == 1:
            n = get_number("Enter a number: ")
            print("Factorial of", n, "is", factorial(n))

        elif choice == 2:
            n = get_number("How many Fibonacci terms do you want? ")
            print("Fibonacci series:", fibonacci_series(n))

        elif choice == 3:
            n = get_number("Enter a number: ")
            print("Reverse of", n, "is", reverse_number(n))

        elif choice == 4:
            n = get_number("Enter a number: ")
            if is_prime(n):
                print(n, "is a prime number.")
            else:
                print(n, "is NOT a prime number.")

        elif choice == 5:
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            if a == 0 and b == 0:
                print("GCD is not defined when both numbers are 0.")
            else:
                print("GCD of", a, "and", b, "is", gcd(a, b))

        elif choice == 6:
            n = get_number("Enter a decimal number: ")
            print("Binary of", n, "is", decimal_to_binary(n))

        elif choice == 7:
            n = get_number("Enter a number: ")
            print("Sum of digits of", n, "is", sum_of_digits(n))

        elif choice == 8:
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            print("Before swapping: a =", a, ", b =", b)
            a, b = swap_numbers(a, b)
            print("After swapping:  a =", a, ", b =", b)

        elif choice == 0:
            print("Thank you for using the Number Toolkit. Goodbye!")
            break                        

        else:
            print("Invalid choice! Please pick a number from 0 to 8.")


main()                                   
