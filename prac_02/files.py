
out_file = open("name.txt", 'w')
name = input("enter your name:")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read()
print("Your name is", name)
in_file.close()

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

in_file = open("numbers.txt", "r")
line = in_file.readlines()
print(line)
in_file.close()