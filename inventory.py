# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        item_total += 1
        print(str(v)+' '+k)
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item]=inventory.get(item,0)+1
    return inventory
        
displayInventory(stuff)

displayInventory(inv)
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

