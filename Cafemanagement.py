# define the menu of resturent

menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
    'Tea':55,
}

#Greet
print("Welcome to Python Resturent")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80\nTea:55 ")

order_total=0
# 40+50=90

item_1 = input("Enter the name of item you want to order =")
#check which order by user is available or not
if item_1 in menu:
    order_total += menu[item_1]#0+50
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to add another item? (yes/no)")
if another_order=="yes":
    item_2 = input("Enter the name  of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Sorry {item_2} is not available!")

print(f"The Total amount of items to pay is {order_total}")







