while True:
    user_input = input("Enter your age. (or tpye 'Exit' to quit): ")

    if user_input == "Exit":
        print("Thanks for checking the softwae out! Goodbye :D")
        break
 
    age = int(user_input)

    if age < 18 or age > 65:
        print("You're Eligible for the $5 Discount!")
    else: 
        print("No Discount Available :(")
