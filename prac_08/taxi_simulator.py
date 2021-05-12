from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
def main():
    total = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    menu = input("q)uit, c)hoose taxi, d)rive").lower()
    while menu != "q":
        if menu == "c":
            print("Taxis available: ")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                price = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name,price))
                total += price
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total))
        menu = input("q)uit, c)hoose taxi, d)rive").lower()
    print("Total trip cost: ${:.2f}".format(total))
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))
main()