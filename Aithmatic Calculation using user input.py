
a = int (input("Enter value of a: "))
b = int (input("Now enter value of b: "))
choice = input("Enter your choice +,-,*,/ \n")
if choice == "+":
    print(a + b)
elif choice == "-":
    print(a - b)
elif choice == "*":
    print(a * b)
elif choice == "/":
    print(a / b)
else:
    print("Invalid choice! please choose +,-,*,/")
