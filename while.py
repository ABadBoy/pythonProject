current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

message = input("Tell me something, and I will repeat it back to you: ")
print(message)
prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
