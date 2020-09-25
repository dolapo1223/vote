print(
    "Hello, Let's check your voter eligibility status.. \n\nWhen ready let's proceed!!!\n\n"
)
name = input("Enter your name here: ")
while name != "quit":
    age = int(input("\nHow old are you: "))
    citizen = input("\nAre you a US citizen? Enter yes or No: ")
    register = input("\nAre you Registered to vote? Enter yes or No:  ")

    if (age >= 18) and (citizen == "yes") and (register == "yes"):
        print(
            f"\n\n{name.upper()}, you are eligible to vote in upcoming\nNov 3rd,2020 Presidential election 😎"
        )

    elif (age < 18) or (citizen == "yes") and (register == "No"):
        print(f"\n\n{name.upper()}, sorry kiddo, you are too young to vote 😉")
    elif (age >= 18) and (citizen == "yes") or (register == "No"):
        print(
            f"\n\n{name.title()},you need to register before you can be elibigible to vote.visit \n\n\033[1mhttps://www.usa.gov/register-to-vote\033[0m to register"
        )
    else:
        print(
            f"\n\n{name.title()},Sorry you are not eligible to vote in this upcoming \nNov 3rd,2020 Presidential election😮"
        )

    print(
        "==========================================================================="
    )

    name = input("\n\nEnter your name here: ")
