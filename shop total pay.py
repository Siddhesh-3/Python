# Q. Design the retail store . 5 products and their prices should be stored in a dictionary 

#show the  product to user
#user enters product name and number of items 

#When user enters Done print the total ammount hat he need to pay

#sol -

#prepare dictonary with 5 item
#get product name an num of items
#While True
#           -break when word == Done


items = {'Pens':10,'Chocos':5,'Bottle':20}

print("Welcome........","Please Pick From The Following list :")

print(items.keys())

total = 0

while True:
    product_name = input("Enter Product Name :")
    
    if product_name == 'done':
        print('Please Pay :',total)
        break
    else:
        quantity = int(input("Enter Quantity :"))
        total = total + items[product_name] * quantity
