
print("Unit Conversion Tool")

while True:
    print("Select Conversion Type: \n1. Length Conversion \n2. Area Conversion \n3. Weight Conversion \n0. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("Length Conversion\n")
    elif choice == "2":
        print("Area Conversion\n")
    elif choice == "3":
        print("Weight Conversion\n")
    elif choice == "0":
        print("Exiting the program.\nGoodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")

