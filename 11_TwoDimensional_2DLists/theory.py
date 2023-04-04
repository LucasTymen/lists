"""
Introduction to Lists
Two-Dimensional (2D) Lists

We’ve seen that the items in a list can be numbers or strings. Lists can contain other lists! We will commonly refer to these as two-dimensional (2D) lists.

Once more, let’s look at a class height example:

    Noelle is 61 inches tall
    Ava is 70 inches tall
    Sam is 67 inches tall
    Mia is 64 inches tall

Previously, we saw that we could create a list representing both Noelle’s name and height:
"""
noelle = ["Noelle", 61]
"""
We can put several of these lists into one list, such that each entry in the list represents a student and their height:
"""
heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]
"""
We will often find that a two-dimensional list is a very good structure for representing grids such as games like tic-tac-toe.
"""
#A 2d list with three lists in each of the indices.
tic_tac_toe = [
            ["X","O","X"],
            ["O","X","O"],
            ["O","O","X"]
]
"""
Let’s practice creating our own 2D list!
Instructions
1.

A new student named "Vik" has joined our class. Vik is 68 inches tall. Add a sublist to the end of the heights list that represents Vik and his height.

Your sublist should be ["Vik", 68].
2.

Create a two-dimensional list called ages where each sublist contains a student’s name and their age. Use the following data:

    "Aaron" is 15
    "Dhruti" is 16

Remember the key components of a two-dimensional list:

    A two-dimensional list begins and ends with square brackets ( [ and ] ). This is our “container” list that wraps all of our inner sublists.

    Any number of sublists within the “container” list. These are our inner lists.

    Each item is separated by a comma ( , ) both in the inner and outer lists.
"""
#Outermost "container" list
example_2d_list = [
  #Innermost sublists
  ["First Sublist", "Second Item"],
  ["Second Sublist", "Second Item"],
  ["Third Sublist", "Second Item"]
]

"""
Make sure to double-check your spelling, capitalization, and element order. Check to make sure it matches the values provided from the checkpoint.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Can a list variable contain items which are also lists of data?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""
