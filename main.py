"""
Create an empty set named showroom.
"""
# Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary

showroom = set()

"""
Add four of your favorite car model names to the set.
"""

showroom.add("Mustang")
showroom.add("Model 3")
showroom.add("Impala")
showroom.add("Leaf")
# print(showroom)

"""
Print the length of your set.
"""

# print(len(showroom))

"""
Pick one of the items in your show room and add it to the set again.
"""
showroom.add("Mustang")

"""
Print your showroom. Notice how there's still only one instance of that model in there.
"""

# print(showroom)

"""
Using update(), add two more car models to your showroom with another set.
"""

showroom.update({"Batmobile", "Mystery Machine"})

# print(showroom)

"""
You've sold one of your cars. Remove it from the set with the discard() method.
"""

showroom.discard("Leaf")

# print(showroom)

"""
Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
"""

junkyard = set()

junkyard.add("Mustang")
junkyard.add("Model 3")
junkyard.add("Lumina")
junkyard.add("PT Cruiser")
junkyard.add("Cobra")
junkyard.add("Party Wagon")
junkyard.add("DeLorean")

# print(junkyard)

"""
Use the intersection method to see which cars exist in both the showroom and that junkyard.
"""

match = showroom.intersection(junkyard)

# print("Matches:", match )

"""
Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
"""

master_list = showroom.union(junkyard)

# print("Master List:", master_list)

"""
Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.
"""

junkyard.discard("PT Cruiser")

print("Less Junky:", junkyard)