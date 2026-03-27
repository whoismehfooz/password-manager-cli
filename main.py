from utils import add_password, view_passwords

def main():
    while True:
        print('\n---PASSWORD MANAGER---')
        print('1. Add password')
        print('2. View passwords')
        print('3. Exit')

        choice = input('Enter here:  ')

        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            break
        else:
            print('INVALID CHOICE!')

if __name__ == '__main__':
    main()