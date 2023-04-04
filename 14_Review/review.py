"""
Introduction to Lists
Review

So far, we have learned:

    How to create a list
    How to access, add, remove, and modify list elements
    How to create a two-dimensional list
    How to access and modify two-dimensional list elements

Let’s practice these skills.
Instructions
1.

Maria is entering customer data for her web store business. We’re going to help her organize her data.

Start by turning this list of customer first names into a list called first_names. Make sure to enter the names in this order:

    Ainsley
    Ben
    Chani
    Depak

Remember the key components of a list:

    A list begins and ends with square brackets ( [ and ]).

    Each item is separated by a comma ( , )

practice_list = ["String", 6, 0.5, True]

Make sure to double-check your spelling, capitalization, and element order. Check to make sure it matches the values provided from the checkpoint.
2.

Maria wants to track all customer’s preferred sizes for her clothing. Create a list called preferred_size.

Fill our new list preferred_size with the following data, containing the preferred sizes for Ainsley, Ben, and Chani:

["Small", "Large", "Medium"]

Remember the key components of a list:

    A list begins and ends with square brackets ( [ and ] ).

    Each item is separated by a comma ( , )

practice_list = ['String', 6, 0.5, True]

Make sure to double-check your spelling and capitalization. Check to make sure it matches the values provided from the checkpoint in the provided order.
3.

Oh no! We forgot to add Depak’s size.

Depak’s size is "Medium". Use .append() to add "Medium" to the preferred_size list.

Print preferred_size to see our change.

To use the .append() method on a list, attach it to the end of your list and pass an element you want to add in between the parenthesis ( )
"""
example_list = [1, 2, 3]
example_list.append(4)

print(example_list)
"""
Will output:

[1, 2, 3, 4]

4.

Maria is having a hard time visualizing which customer is associated with each size. Let’s restructure our two lists into a two-dimensional list to help Maria.

In addition to our already available data, Maria is adding a third value for each customer that reflects if they want expedited shipping on their orders.

This will be reflected using a boolean value (True for expedited, False for regular)

Create a two-dimensional list called customer_data using the following table as a reference for the data. Each sublist should contain a name, size, and expedited shipping option for a single person.
Name 	Size 	Expedited Shipping
"Ainsley" 	"Small" 	True
"Ben" 	"Large" 	False
"Chani" 	"Medium" 	True
"Depak" 	"Medium" 	False

Print customer_data to see the data.

Here is what our list would look like if it only included "Ainsley"

[["Ainsley","Small", True]]

Make sure to double-check your spelling, capitalization, and element order. Check to make sure it matches the values provided from the checkpoint.
5.

"Chani" reached out to Maria. She requested to switch to regular shipping to save some money.

Change the data value for "Chani"‘s shipping preference to False in our two-dimensional list to reflect the change.

"Chani's" information should be listed as the third element in customer_data (index 2).

Shipping information is the third item in each sublist (index 2). Because Chani does not want expedited shipping, the value at this location should be changed to False.”
6.

"Ben" reached out to Maria asking to remove his shipping option because he is not sure what type he wants.

Use the .remove() method to delete the shipping value from the sublist that contains ben’s data.

Note: We never explicitly went over how to use the .remove() method on a 2d list together. If you feel like you are struggling, take a look at the hint for some guidance.

To use the .remove() method on a two-dimensional list, call it on the sublist you are modifying and pass the value you want to remove in between the parenthesis ( ).
"""
practice_list = [["a"], ["b"], ["c"]]
practice_list[1].remove("b")

print(practice_list)
"""
Would output:

[["a"], [], ["c"]]

7.

Great job making it this far! One last thing, Maria received new customers, "Amit" and "Karim", the following 2d list contains their data:

[["Amit", "Large", True], ["Karim", "X-Large", False]]

Create a new variable customer_data_final. Combine our existing list customer_data with our new customer 2d list using + by adding it to the end of customer_data.

Print customer_data_final to see our final result.

To combine two lists using +, define a new variable and set it to the two lists we want to combine with + in between.

Here is an example:
"""
group_1 = [1, 2, 3]

group_2 = group_1 + [4, 5]
print(group_2)
"""
Would output:

[1, 2, 3, 4, 5]

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    If I have a list containing items, how can I empty or delete all the contents of the list?

Still have questions? View this exercise's thread in the Codecademy Forums.

"""
