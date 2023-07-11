# Sierra Argueta
# Lab 6- Encoder/Decoder
def password_encoder(pass_string):
    encoded_password = ''
    for num in pass_string:
        num = int(num)
        num += 3
        encoded_password += str(num)
    return encoded_password


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
            pass
        if user_option == 3:
            exit()


if __name__ == '__main__':
    main()
    # print(password_encoder('12345555'))
