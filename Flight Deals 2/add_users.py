import requests

SHEET_ENDPOINT = ""

print("Welcome to Python Developer Flight Club!\nWe find the best flight deals and email you!")

first_name = input("\nWhat is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email? ")
confirm_email = input("Type your email again? ")

if confirm_email == email:

    body = {
        "sheet2": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(url=SHEET_ENDPOINT, json=body)

    print("\nYou're in the club")



