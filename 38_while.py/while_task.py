while True:
    try:
        num_one = float(input("Enter first number: "))
        num_two = float(input("Enter second number: "))
        print(num_one / num_two)
        ask_str = input("Do you want to proceed? Yes or No? ").capitalize()
        if ask_str == "No":
            break
        
    except ValueError:
        print("Letter is not a number. One more time :( ")
