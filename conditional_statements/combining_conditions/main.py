# Define the seasonal and holiday status conditions 
seasonal_item = False
holiday_item = True

# Combine the conditions to check if the item is seasonal or discounted
# (`temporary_stock`) will become `True` if either condition `seasonal_item` OR `holiday_item` is `True`
temporary_stock = seasonal_item or holiday_item

# Print the result
print("Is this a seasonal or holiday item?", temporary_stock) 