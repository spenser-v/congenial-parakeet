price_dictionary = {'white': 1, 'wheat': 1.5, 'sourdough': 1.5,
'chicken': 3, 'turkey': 3.5, 'ham': 3, 'tofu': 3.5,
'cheddar': 1, 'swiss': 1, 'mozzarella': 1,
'mayo': .1, 'mustard': .1, 'lettuce': .3, 'tomato': .3}

sandwich = ['white', 'chicken', 'cheddar', 'mayo']
price = [price_dictionary[x] for x in sandwich]

print('$ '+ str(sum(price)) + '0')
