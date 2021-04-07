"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    new_data = New_data()
    print(new_data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)

        print(parts[2])

        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
    input_file.close()

def New_data():
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        print("{} is taught by {} and has {} students".format(parts[0],parts[1],parts[2]))
    input_file.close()


main()