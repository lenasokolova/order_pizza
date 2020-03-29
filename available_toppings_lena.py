availabla_toppings = ["mushrooms", "olives", "bacon", "pepperoni", "pineapple", "double cheese"]
requested_toppings = ["mushrooms", "pepperoni", "double cheese", "olives", "chicken"]

for requested_topping in requested_toppings:
	if requested_topping in availabla_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have a " +  requested_topping + ".")
print("\nYour order is ready!")
