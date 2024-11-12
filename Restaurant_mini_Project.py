# Menu List
menu = {
    'Pizza':40,
    'Burger':60,
    'Pasta':50,
    'Salad':70,
    'Coffee':80,
}

print("Welcome to Python Restaurant...!!")
print("Pizza: Rs.40\nBurger: Rs.60\nPasta: Rs.50\nSalad: Rs.70\nCoffee: Rs.80")

tot_order = 0
tot_order1 = 0
item_1 = input("Enter the name of time you want to do order : ")
if item_1 in menu:
    how = int(input("How many dishes do you want ? : "))
    tot_order = tot_order + menu[item_1]
    tot_order1 = tot_order * how
    print(f"Your item {item_1} has been added")
else:
    print(f"Order item {item_1} is not availabel")


another_order = input("Do you want to add another item? (Yes/No): ")
if another_order == "Yes":
    item_2 = input("Enter the name of item : ")
    if item_2 in menu:
        how = int(input("How many dishes do you want ? : "))
        tot_order = tot_order + menu[item_2]
        tot_order1 = tot_order * how
        print(f"Your Item {item_2} has been added")
    else:
        print(f"Order item {item_2} is not availabel")

        
print("----------Your Bill----------")
print(f"Total Order is {tot_order1}")
