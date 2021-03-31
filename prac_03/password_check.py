def main():
    password = get_password()
    the_password(password)


def the_password(password):
    print("*" * int(password))


def get_password():
    password = input("Enter your password:")
    return password


main()


