inventory_items = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for item, amount in inventory_items.items():
        print(amount, item)
        item_total = item_total + int(amount)
    print("Total number of items: " + str(item_total))

display_inventory(inventory_items)
