"""
Introduction to Lists
Growing a List: Append

We can add a single element to a list using the .append() Python method.

Suppose we have an empty list called garden:

garden = []

We can add the element "Tomatoes" by using the .append() method:

garden.append("Tomatoes")

print(garden)

Will output:

['Tomatoes']

We see that garden now contains "Tomatoes"!

When we use .append() on a list that already has elements, our new element is added to the end of the list:

# Create a list
garden = ["Tomatoes", "Grapes", "Cauliflower"]

# Append a new element
garden.append("Green Beans")
print(garden)

Will output:

['Tomatoes', 'Grapes', 'Cauliflower', 'Green Beans']

Let’s use the .append() method to manipulate a list.
Instructions
1.

Jiho works for a gardening store called Petal Power. Jiho keeps a record of orders in a list called orders.

Use print to inspect the orders he has received today.

You should see:

['daisies', 'periwinkle']

2.

Jiho just received a new order for "tulips". Use append to add this string to orders.

To use the .append() method on a list, attach it to the end of your list and pass an element you want to add in between the parenthesis ( )

example_list = [1, 2, 3]
example_list.append(4)

print(example_list)

Will output:

[1, 2, 3, 4]

3.

Another order has come in! Use append to add "roses" to orders.

Double-check your spelling and capitalization of roses.

You can add an element to orders like so:

orders.append( #YOUR ELEMENT HERE )

4.

Use print to inspect the orders Jiho has received today.

You should see:

['daisies', 'periwinkle', 'tulips', 'roses']

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Is it possible to use the append() function to add more than one item at a time to a list?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""
