import pyinputplus as pyip
sandwich_ingredients = []
for i in ['mayo', 'mustard', 'lettuce', 'tomato']:
    response = pyip.inputYesNo(prompt = 'Would you like ' + i + '?')
    if response == 'yes':
        response = i
        sandwich_ingredients.append(response)
print(sandwich_ingredients)
