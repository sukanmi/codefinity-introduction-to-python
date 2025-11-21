# Task 1: Create the list
vegetables = ["tomatoes", "potatoes", "onions"]

# Task 2: Remove "onions"
vegetables.remove("onions")

# Task 3: Add "carrots" if not already present
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

# Task 4: Add "cucumbers" if not already present
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

# Task 5: Sort alphabetically
vegetables.sort()

# Output
print("Updated Vegetable Inventory:", vegetables)