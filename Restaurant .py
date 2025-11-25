menu={'Pizza':50,
      'Burger':60,
      'Tea':20,
      'COffee':30,
      'Fries':30,
      'Sandwich':50,
      'Orange juice':40
}

print("Welcome to CS Restaurant")
print("Pizza: Rs50\nBurger: Rs60\nTea: Rs20\nCoffee: Rs30\nFries: Rs30\nSndwich: Rs50\nOrange juice: Rs40")

order_total=0
item_1=input("Entre the name of item you want to order =")
if item_1 in menu:
  order_total+=menu[item_1]
  print(f"Your item {item_1} has been added to your order ")

else:
  print(f"Ordered item {item_1} is not available yet!")

another_order=input("Do you want to add another item? (Yes/No)")
if another_order=='Yes':
  item_2=input("Entre the name of second item=")
  if item_2 in menu:
    order_total+=menu[item_2]
    print(f"Item {item_2} has been added to your order")

  else:
    print(f"Ordered item {item_2} is not available yet!")

  print(f"The total amount of items to pay is{order_total}")

  review=input('Do you want to review your order? (Yes/No)')
  if review=='Yes':
    print(f"Thank you for your cooperation")

  else:
    print(f"Thank you for visiting our Restaurant please give us another chance")
