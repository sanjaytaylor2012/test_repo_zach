def encode(password):
    encoded = ""
    for i in range(len(password)):
        encoded += str((int(password[i]) + 3) % 10)
    return encoded


def decode(password):

    decoded = ""

    for i in range(len(password)):

        if password[i] == '0':
            decoded += '7'
        elif password[i] == '1':
            decoded += '8'
        elif password[i] == '2':
            decoded += '9'
        else:
            decoded += str((int(password[i]) - 3))

    return decoded


while True:
    print(
        """
Menu  
------------- 
1. Encode  
2. Decode  
3. Quit 
    """
    )

    option = input("Please enter an option: ")

    if option == "1":
        password = input("Please enter your password to encode: ")
        encoded_pass = encode(password)
        print("Your password has been encoded and stored!")

    elif option == "2":
        decoded_pass = decode(encoded_pass)
        print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}')
    elif option == "3":
        quit()
