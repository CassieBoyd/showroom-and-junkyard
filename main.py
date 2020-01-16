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
print(showroom)

"""
Print the length of your set.
"""

print(len(showroom))

"""
Pick one of the items in your show room and add it to the set again.
"""
showroom.add("Mustang")

"""
Print your showroom. Notice how there's still only one instance of that model in there.
"""

print(showroom)

"""
Using update(), add two more car models to your showroom with another set.
"""

showroom.update({"Batmobile", "Mystery Machine"})

print(showroom)

"""
You've sold one of your cars. Remove it from the set with the discard() method.
"""

showroom.discard("Leaf")

