from building import Building

four_oh_four_church = Building("404 Church St.", 14)
three_three_two_marshall = Building("332 Marshall St.", 2)
three_oh_one_plus_park = Building("301 Plus Park Blvd.", 5)
five_spot = Building("1006 Forrest Ave.", 1)
batman_building = Building("333 Commerce St.", 33)

buildingsList = [four_oh_four_church, three_oh_one_plus_park, three_three_two_marshall, batman_building, five_spot]

for building in buildingsList:
    building.purchase("Joe Exotic")
    building.construct()
    print(f'{building.address} was purchased by {building.owner} on {building.date_constructed.tm_mon}/{building.date_constructed.tm_mday}/{building.date_constructed.tm_year} and has {building.stories} stories')