"""
Introduction to Lists
Modifying 2D Lists

Now that we know how to access two-dimensional lists, modifying the elements should come naturally.

Let’s return to a classroom example, but now instead of heights or test scores, our list stores the student’s favorite hobby!
"""
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
"""
"Jenny" changed their mind and is now more interested in "Meditation".

We will need to modify the list to accommodate the change to our class_name_hobbies list. To change a value in a two-dimensional list, reassign the value using the specific index.
"""
# The list of Jenny is at index 0. The hobby is at index 1.
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)
"""
Would output:

[["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

Negative indices will work as well.
"""
# The list of Grace is the last entry. The hobby is the last element.
class_name_hobbies[-1][-1] = "Football"
print(class_name_hobbies)
"""
Would output:

[["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Football"]]

Instructions
1.

Our school is expanding! We are welcoming a new set of students today from all over the world.

Using the provided table, create a two-dimensional list called incoming_class to represent the data. Each sublist in incoming_class should contain the name, nationality, and grade for a single student.
Name 	Nationality 	Grade Level
"Kenny" 	"American" 	9
"Tanya" 	"Ukrainian" 	9
"Madison" 	"Indian" 	7

Print incoming_class to see our list.

Remember the key components of a two-dimensional list:

    A two-dimensional list begins and ends with square brackets ( [ and ] ). This is our “container” list that wraps all of our inner sublists.

    Any number of sublists within the “container” list. These are our inner lists.

    Each item is separated by a comma ( , ) both in the inner and outer lists.

For our example, the first sublist would look like this:

[["Kenny", "American", 9]]

Make sure to double-check your spelling, capitalization, and element order. Check to make sure it matches the values provided from the checkpoint.
2.

"Madison" passed an exam to advance a grade. She will be pushed into 8th grade rather than her current 7th in our list.

Modify the list using double brackets [][] to make the change. Use positive indices.

Print incoming_class to see our change.

Given the list
"""
my_list = [["a","b"],["c","d"]],
"""
we could change the letter "b" to "z" using
"""
my_list[0][1] = "z"
print(my_list)
"""
Would output:

[["a","z"],["c","d"]]

3.

"Kenny" likes to be called by his nickname "Ken". Modify the list using double brackets [][] to accommodate the change but only using negative indices.

Print incoming_class to see our change.

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
