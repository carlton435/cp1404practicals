def main():
    list = []
    for i in range(5):
        list.append(int(input("Number:")))
    print("The first number is {}".format(list[0]))
    print("The last number is {}".format(list[4]))
    print("The smallest number is {}".format(min(list)))
    print("The largest number is {}".format(max(list)))
    average = (list[0] + list[1] + list[2] + list[3] + list[4]) / 5
    print("The average of the numbers is {}".format(average))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    entername = input("What is your usename:")
    if entername in usernames:
        print("Access granted")
    else:
        print("Access denied")
main()