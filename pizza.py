pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print("you ordered a "+pizza['crust']+"-crustpizza with toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)
