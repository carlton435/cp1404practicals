def main():
    print("My guitars!")
    number = 0
    dic = {}
    number1 = 0
    while True:
        name = input("Name:")
        if name == " ":
            break
        else:
            number = number + 1
            year = int(input("Year:"))
            cost = int(input("Cost: $"))
            print("{}({}),{}".format(name, year, cost))
            key = "{}:{}({})".format(number, name, year)
            money = cost
            dic[key] = "{}".format(money)
            print(dic)

    while number1 < number:
        x = list(dic.keys())
        y = list(dic.values())
        print("Guitar",x[number1],", worth $ ",y[number1])
        number1 += 1



main()
