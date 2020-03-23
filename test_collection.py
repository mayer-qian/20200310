#from collections import OrderedDict
#od = OrderedDict()
od = {"applies": 5, "pears": 2, "orange": 9}
print(od)
od["pears"] = 3
od["bananas"] = 12
for fruit, quantity in od.items():
    print("You have {} {}.".format(quantity, fruit))