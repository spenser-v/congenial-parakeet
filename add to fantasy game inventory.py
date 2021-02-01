def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory[i] = 1

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for item, amount in inventory.items():
        print(amount, item)
        item_total = item_total + int(amount)
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(inv, dragon_loot)

display_inventory(inv)