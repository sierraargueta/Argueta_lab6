# Sierra Argueta
# Lab 6- Encoder/Decoder
def password_encoder(pass_string):
    encoded_password = ''
    for num in pass_string:
        num = int(num)
        num += 3
        encoded_password += str(num)
    return encoded_password

# decode function added by Ernesto Lopez
def decode(encoded):
    decoded_digits = []
    for digit in encoded:
        # Convert digit from string to integer
        digit_int = int(digit)
        # Shift digit down by 3, wrapping around to 0 after 9
        decoded_digit_int = 0
        if digit_int > 2:
            decoded_digit_int = digit_int - 3
        elif digit_int == 2:
            decoded_digit_int = 9
        elif digit_int == 1:
            decoded_digit_int = 8
        elif digit_int == 0:
            decoded_digit_int = 7
        # Convert encoded digit back to string and append to list
        decoded_digits.append(str(decoded_digit_int))
    # Convert list of encoded digits to string
    decoded_password = ''.join(decoded_digits)
    return decoded_password

def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('')
        user_option = int(input('Please enter an option: '))
        if user_option == 1:
            user_pass = input('Please enter your password to encode: ')
            password_encoder(user_pass)
            print('Your password has been encoded and stored!')
            print('')
        if user_option == 2:
            print(f'The encoded password is {password_encoder(user_pass)}, and the original password is {decode(password_encoder(user_pass))}.')
        if user_option == 3:
            exit()


if __name__ == '__main__':
    main()
    # print(password_encoder('12345555'))
