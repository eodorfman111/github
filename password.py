# Leo Dorfman

def encode(password):
    encoded_password = ""
    for i in password:
        new_digit = str(int(i) + 3)
        encoded_password += new_digit
    return encoded_password
def decode(password):
    decoded_password = ""
    for i in password:
        new_digit = str(int(i) - 3)
        decoded_password += new_digit
    return decoded_password

while True:
    print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    option = input("Please enter an option: ")
    if option == "1":
        password_encode = input("Please enter your password to encode: ")
        encoded_password = encode(password_encode)
        print("Your password has been encoded and stored!")
    elif option == "2":
        print("The encoded password is "+ encoded_password + ", and the original password is "+ decode(encoded_password) + ".")
    elif option == "3":
        break
