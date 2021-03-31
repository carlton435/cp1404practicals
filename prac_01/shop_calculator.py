number = int(input("Number of items:"))
total = 0
while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items:"))
for i in range(0,number):
    item = float(input("Price of item:"))
    total =item + total
if total > 100:
    discount = total - total *0.1
    print("Total price for {} items is ${:.2f} ".format(number,discount))
else:
    print("Total price for {} items is ${} ".format(number,total))
