print("=============SHOPPING CART SYSTEM================\n")

Products = []
print("Added :", Products.append(input("Enter product name:")))
print("Added :", Products.append(input("Enter product name:")))
print("Added :", Products.append(input("Enter product name:")))
print("Added :", Products.append(input("Enter product name:")))

print("Products in cart:", Products)

print("Total items :", len(Products))
Search = input("Searching for:")
if Search  in Products:
    print("product found")
else:
    print("product not found")
print("Removing" , Products.remove(input("Enter product name to remove:")))

print("Updated Cart:", Products)
print("Total items : ", len(Products))