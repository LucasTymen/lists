"""
Introduction to Lists
Shrinking a List: Remove

We can remove elements in a list using the .remove() Python method.

Suppose we have a filled list called shopping_line that represents a line at a grocery store:
"""
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]
"""
We could remove "Chris" by using the .remove() method:
"""
shopping_line.remove("Chris")

print(shopping_line)
"""
If we examine shopping_line, we can see that it now doesn’t contain "Chris":

["Cole", "Kip", "Sylvana"]

We can also use .remove() on a list that has duplicate elements.

Only the first instance of the matching element is removed:
"""
# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]

# Remove a element
shopping_line.remove("Chris")
print(shopping_line)
"""
Will output:

["Cole", "Kip", "Sylvana", "Chris"]

Let’s practice using the .remove() method to remove elements from a list.
Instructions
1.

We have decided to get into the grocery store business. Our manager Calla has decided to store all the inventory purchases in a list to help track what products need to be ordered.

Let’s create a list called order_list with the following values (in this particular order):

"Celery", "Orange Juice", "Orange", "Flatbread"

Print order_list to see the current list.

Remember the key components of a list:

    A list begins and ends with square brackets ( [ and ] ).

    Each item is separated by a comma ( , )
"""
practice_list = ['String', 6, 0.5, True]
"""
Make sure to double-check your spelling and capitalization. Check to make sure it matches the values provided from the checkpoint in the provided order.
2.

We are in luck! We actually found a spare case of "Flatbread" in our back storage. We won’t need to order it anymore. Let’s remove it from order_list using the .remove() method.

Print order_list to see the current list.

To use the .remove() method, call it on the list you are modifying and pass the value you want to remove in between the parenthesis ( ).
"""
practice_list = ["a", "b", "c"]
practice_list.remove("b")

print(practice_list)
"""
Would output:

["a", "c"]

3.

Our store has grown to be a huge success! We decided to open a second store and require a new order list. Calla has done us the favor of putting one together.

Create a new list called new_store_order_list and assign it the following values (in order):

"Orange", "Apple", "Mango", "Broccoli", "Mango"

Note: Our second store is going to need two orders of mangos so the value is duplicated.

Print new_store_order_list to see the current list.

Remember the key components of a list:

    A list begins and ends with square brackets ( [ and ] ).

    Each item is separated by a comma ( , )
"""
practice_list = ['String', 6, 0.5, True]
"""
Make sure to double-check your spelling and capitalization. Check to make sure it matches the values provided from the checkpoint.
4.

We are in luck again! We actually found a spare case of "Mango" in our back storage.

We won’t be needing to place two orders anymore.

Let’s remove it from new_store_order_list using the .remove() method.

Print new_store_order_list to see the current list.

The.remove() method will work on duplicate values in a list. .remove() will delete the first instance of a match for the provided element you want to delete.
"""
practice_list = ["a", "b", "c", "b"]
practice_list.remove("b")

print(practice_list)
"""
Would output:

["a", "c", "b"]

5.

Calla ran to tell us some important news! She asked us to remove "Onions" from our new new_store_order_list. If we double-check our list, we will notice we don’t have "Onions" on our list.

Let’s see what happens when we try to remove an item that does not exist.

Call the .remove() method with the value of "Onions" on our new_store_order_list list.

When we call .remove() on a list with a value that does not exist, we will receive a ValueError.

Traceback (most recent call last):
  File "script.py", line 18, in <module>
    new_store_order_list.remove("Onions")
ValueError: list.remove(x): x not in list

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
"""
