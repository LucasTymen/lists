"""
Introduction to Lists
Growing a List: Plus (+)

When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).

Below, we have a list of items sold at a bakery called items_sold:

items_sold = ["cake", "cookie", "bread"]

Suppose the bakery wants to start selling "biscuit" and "tart":
"""
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)
"""
Would output:

['cake', 'cookie', 'bread', 'biscuit', 'tart']

In this example, we created a new variable, items_sold_new, which contained both the original items sold, and the new items. We can inspect the original items_sold and see that it did not change:
"""
print(items_sold)
"""
Would output:

['cake', 'cookie', 'bread']

We can only use + with other lists. If we type in this code:
"""
my_list = [1, 2, 3]
my_list + 4
"""
we will get the following error:

TypeError: can only concatenate list (not "int") to list

If we want to add a single element using +, we have to put it into a list with brackets ([]):
"""
my_list + [4]
"""
Let’s use + to practice combining two lists!
Instructions
1.

Jiho is updating a list of orders. He just received orders for "lilac" and "iris".

Create a list called new_orders that contains our new orders.

Remember the key components of a list:

    A list begins and ends with square brackets ( [ and ] ).

    Each item is separated by a comma ( , )
"""
practice_list = ["String", 6, 0.5, True]
"""
Make sure to double-check your spelling, capitalization, and element order. Check to make sure it matches the values provided from the checkpoint.
2.

Use + to create a new list called orders_combined that combines orders with new_orders.

To combine two lists using +, define a new variable and set it to the two lists we want to combine with + in between.
"""
list_one = [1, 2, 3]
list_two = [4, 5, 6]

combo_using_plus = list_one + list_two
print(combo_using_plus)
"""
Will output:

[1, 2, 3, 4, 5, 6]

3.

Remove the # and whitespace in front of the list broken_prices. If you run this code, you’ll get an error:

TypeError: can only concatenate list (not "int") to list

Fix the command by inserting brackets ([ and ]) so that it will run without errors.

Getting an IndentationError? Remember to remove the whitespace in front of broken_prices
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.

"""
