# Append method for the list items
fruits = ["pineaple", "banana", "apple", "melon"]
fruits.append("Kiwi")
print(fruits)

# Insert method for a list. Note that if you add an element to the higher index than length of the list, 
# it goes to the end of the list.
fruits.insert(0, "Orange")
print(fruits)

# remove method removes the element from the list
# When the element removed was not in the list it throughs an error!
fruits.remove("melon")
print(fruits)

# pop method receives an index and retuns the element at that index after removing it
fruits.pop(3)
print(fruits)

# Assigning a new element to the list
fruits[3] = "Avocado"
print(fruits)

