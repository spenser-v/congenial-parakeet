import pyinputplus as pyip

price_dictionary = {'white': 1, 'wheat': 1.50, 'sourdough': 1.50,
'chicken': 3, 'turkey': 3.50, 'ham': 3, 'tofu': 3.50,
'cheddar': 1, 'swiss': 1, 'mozzarella': 1, 'None': 0,
'mayo': .10, 'mustard': .10, 'lettuce': .30, 'tomato': .30}

bread = pyip.inputMenu(['white', 'wheat', 'sourdough'])
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
cheese = pyip.inputYesNo(prompt = 'Would you like to add cheese for $1?')
if cheese == 'yes':
    cheese_choice = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'])
else:
    cheese_choice = 'None'
sandwich_ingredients = [bread, protein, cheese_choice]
for i in ['mayo', 'mustard', 'lettuce', 'tomato']: #can add other ingredients here
    response = pyip.inputYesNo(prompt = 'Would you like to add ' + i + '?')
    if response == 'yes':
        response = i
        sandwich_ingredients.append(response)
sandwich_number = pyip.inputInt(prompt ='How many sandwiches would you like?', min = 1)

print(sandwich_ingredients)
price = [price_dictionary[x] for x in sandwich_ingredients]
print('Your sandwich(es) cost ' + str('${:,.2f}'.format(sum(price) * sandwich_number)) + '.')
