# The item's discount and stock status have been defined
#discounted = False
#lowStock = True
# Define the perishable and stock status conditions
is_perishable = True
item_quantity = 110
perishable_highStockRisk = 100

# Using the (and) operator to combine two conditions
# The first condition (`is_perishable`) checks if the item is perishable
# The second condition (`item_quantity >= perishable_highStockRisk`) checks if the item is high in stock 
# The `consider_discount` variable will become `True` only if both conditions are `True`
consider_discount = is_perishable and (item_quantity >= perishable_highStockRisk)

# Print the result
print("Is the item perishable and high in stock?", consider_discount)