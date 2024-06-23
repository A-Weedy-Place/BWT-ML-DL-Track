def update_inventory(inventory_dict, item, quantity):
  if item not in inventory_dict:
    inventory_dict[item] = 0

  new_quantity = inventory_dict[item] + quantity
  if new_quantity >= 0:
    inventory_dict[item] = new_quantity
  else:
    print(f"Cannot remove more than {quantity} {item} from inventory.")
  return inventory_dict

inventory = {"mangoes": 10, "apples": 10, "oranges": 0}
while True:

    #print("Items in inventory: 'mangoes = 10', 'apples = 10' and 'oranges = 0'")
    item = input("Enter item: ")
    quantity = int (input("Enter quantitiy: "))

    inventory = update_inventory(inventory.copy(), item, quantity)
    print(inventory) 