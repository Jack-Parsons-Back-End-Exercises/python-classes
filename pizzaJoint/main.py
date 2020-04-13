from pizza import Pizza

meat_lovers = Pizza()
meat_lovers.size = "16"
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()

meatball_parm = Pizza()
meatball_parm.size = "20"
meatball_parm.style = "Hand-tossed"
meatball_parm.add_topping("Meatballs")
meatball_parm.add_topping("Parmesan")
meatball_parm.print_order()