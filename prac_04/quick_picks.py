import random
def main():
    number = int(input("How many quick picks?"))
    for i in range(number):
        list = []
        for i in range(6):
            list.append(random.randint(1, 45))
        print(list)






main()