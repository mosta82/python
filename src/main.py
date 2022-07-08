user_numb = int(input("Enter your number: "))

while user_numb > 0:
    if user_numb % 5 == 0 or user_numb % 3 == 0:
        print(user_numb)

    user_numb -= 1