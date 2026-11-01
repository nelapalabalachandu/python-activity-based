opening_stock = int(input("Enter opening stock: "))
received = int(input("Enter received stock: "))
sold = int(input("Enter sold stock: "))

available_stock = opening_stock + received - sold

print("Available Stock:", available_stock)

if available_stock < 10:
    print("Low Stock")
else:
    print("Stock Available")