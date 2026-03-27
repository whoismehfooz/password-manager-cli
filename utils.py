from storage import load_passwords, save_passwords


def add_password():
    site = input('Enter site: ')
    username = input('Enter username: ')
    password = input('Enter password: ')

    data = load_passwords()

    data[site] = {
        'username': username,
        'password': password
    }

    save_passwords(data)
    print('✅ Password saved')


def view_passwords():
    data = load_passwords()

    if not data:
        print('No passwords saved yet!')
        return

    print('\n--- SAVED PASSWORDS ---')
    for site, creds in data.items():
        print(f"🌐 {site}")
        print(f"Username: {creds['username']}")
        print(f"Password: {creds['password']}")
        print('-' * 30)