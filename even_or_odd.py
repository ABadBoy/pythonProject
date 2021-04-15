number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number %2 == 0:
    print("\nThe number "+str(number)+" id even.")
else:
    print("\nThe number "+str(number)+" id odd.")