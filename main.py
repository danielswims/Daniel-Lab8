from DEL_decode import decode
from DEL_Encode import encode


def main():
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        op = input('Please enter an option: ')

        if op == '1':
            password = input('Please enter a password to encode: ')
            encode(password)
            print('Your password has been encoded and stored!')
            print('')
        elif op == '2':
            print(f"The encoded password is {decode(password)}, and the original password is {password}")
            print('')
        elif op == '3':
            break


if __name__ == '__main__':
    main()
