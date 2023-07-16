def encode(password):
    encoded = ""
    for i in range(len(password)):
        encoded += str((int(password[i]) + 3) % 10)
    return encoded


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
        print(encoded_pass)

    # elif option == "2":
    # decoded_pass = decode(encoded_pass)
    # print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}')
    elif option == "3":
        quit()
