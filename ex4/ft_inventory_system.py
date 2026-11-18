#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in sys.argv[1:]:
        items_numbers = arg.split(":")
        if items_numbers[0] in inventory:
            print(f"Redundant item '{items_numbers[0]}' - discarding")
            continue
        if len(items_numbers) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if not items_numbers[0]:
            continue
        try:
            quantity = int(items_numbers[1])
        except ValueError as e:
            print(f"Quantity error for '{items_numbers[0]}' {e}")
            continue
        inventory[items_numbers[0]] = quantity
    print(f"Got inventory: {inventory}")
    print(f"Total quantity of the {len(inventory)} "
          f"items: {sum(inventory.values())}")
    total = sum(inventory.values())
    for item in inventory.keys():
        quantity = inventory[item]
        percentage = (quantity / total) * 100
        print(f"Item {item} represents {round(percentage, 1)}%")
    items = list(inventory.keys())
    highest = inventory[items[1]]
    lowest = inventory[items[1]]
    most_abundant = items[0]
    least_abundant = items[0]
    for item in items:
        value = inventory[item]
        if value > highest:
            highest = value
            most_abundant = item
        if value < lowest:
            lowest = value
            least_abundant = item
    print(f"Item most abundant: {most_abundant} with {highest}")
    print(f"Item least abundant: {least_abundant} with {lowest}")
    inventory.update({"magic_item": 1})
    print(f"Update inventory: {inventory}")
