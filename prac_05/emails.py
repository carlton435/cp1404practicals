def main():

    number = 0

    NameAndEmail = {}
    while number < 2:

        number += 1
        Email = input("Email:")
        EmailSplit = Email.split("@")

        Title = EmailSplit[0].title()


        answer = input("Is your name {}? (Y/n)".format(Title))
        answer_lower = answer.lower()
        if answer_lower == "y":

            name = EmailSplit[0].title()
            NameAndEmail[name]=Email
        elif answer_lower == "n":
            name = input("Name:")
            name = name.title()
            NameAndEmail[name]=Email
    print(NameAndEmail)
    for k,v in NameAndEmail.items():
        print("{} ({})".format(k, v))
    NameAndEmail.items()







main()