message = input("Tell me something, and I will repeat it back to you: ")
print(message)

height = input("How tall are you, in inches?")
height = int(height)
if height >= 36:
    print("You're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")
