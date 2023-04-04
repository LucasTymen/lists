"""
Introduction to Lists
Accessing 2D Lists

Let’s return to our classroom heights example:
"""
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
"""
Two-dimensional lists can be accessed similar to their one-dimensional counterpart. Instead of providing a single pair of brackets [ ] we will use an additional set for each dimension past the first.

If we wanted to access "Noelle"‘s height:
"""
#Access the sublist at index 0, and then access the 1st index of that sublist.
noelles_height = heights[0][1]
print(noelles_height)
"""
Would output:

61

Here are the index numbers to access data for the list heights:
Element 	Index
"Noelle" 	heights[0][0]
61 	heights[0][1]
"Ali" 	heights[1][0]
70 	heights[1][1]
"Sam" 	heights[2][0]
67 	heights[2][1]

Let’s practice accessing data in a two-dimensional list.
Instructions
1.

We want to have a way to store all of our classroom test score data.

Using the provided table, create a two-dimensional list called class_name_test to represent the data. Each sublist in class_name_test should have one student’s name and their associated score.
Name 	Test Score
"Jenny" 	90
"Alexus" 	85.5
"Sam" 	83
"Ellie" 	101.5

Print class_name_test to see the result.

The first sublist in class_name_test should be ["Jenny", 90]. See if you can fill in the rest!
2.

Use double square brackets ([][]) to select Sam‘s test score from the list class_name_test.

Save it to the variable sams_score.

Print the variable sams_score to see the result.

When accessing a two-dimensional list, determine the index for both the inner and outer list.

Apply the indices inside a pair of double brackets [][].
"""
example_2d_list = [
  ["First Sublist"],
  ["Second Sublist"],
  ["Third Sublist"]
]
"""
Element 	Access Index
"First Sublist" 	example_2d_list[0][0]
"First Sublist" 	example_2d_list[1][0]
"First Sublist"" 	example_2d_list[2][0]
3.

Use double square brackets ([][]) to select Ellies test score from the list class_name_test. This time only use negative indices!

Save it to the variable ellies_score.

Print the variable ellies_score to see the result.

Negative indices in two-dimensional lists work the same as their one-dimensional counterpart.
"""
example_2d_list = [
  ["First Sublist", "Second Item"],
  ["Second Sublist", "Second Item Two"],
  ["Third Sublist", "Second Item Three"]
]
"""
Element 	Access Index
"Second Item" 	example_2d_list[-3][-1]
"Second Item Two" 	example_2d_list[-2][-1]
"Second Item Three" 	example_2d_list[-1][-1]
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
"""
