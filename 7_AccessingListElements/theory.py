"""
Introduction to Lists
Accessing List Elements

We are interviewing candidates for a job. We will call each candidate in order, represented by a Python list:
"""
calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]
"""
First, we’ll call "Juan", then "Zofia", etc.

In Python, we call the location of an element in a list its index.

Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.

Here are the index numbers for the list calls:
Element 	Index
"Juan" 	0
"Zofia" 	1
"Amare" 	2
"Ezio" 	3
"Ananya" 	4

In this example, the element with index 2 is "Amare".

We can select a single element from a list by using square brackets ([]) and the index of the list item. If we wanted to select the third element from the list, we’d use calls[2]:
"""
print(calls[2])
"""
Will output:

Amare

Note: When accessing elements of a list, you must use an int as the index. If you use a float, you will get an error. This can be especially tricky when using division. For example print(calls[4/2]) will result in an error, because 4/2 gets evaluated to the float 2.0.

To solve this problem, you can force the result of your division to be an int by using the int() function. int() takes a number and cuts off the decimal point. For example, int(5.9) and int(5.0) will both become 5. Therefore, calls[int(4/2)] will result in the same value as calls[2], whereas calls[4/2] will result in an error.
Instructions
1.

Use square brackets ([ and ]) to select the 4th employee from the list employees. Save it to the variable employee_four.

Remember lists are zero-indexed. The first element of a list will start at zero. If we are trying to access the 3rd element, we are really trying to access the 2nd index.
"""
calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]

print(calls[2]) #Will access the third element (second index)
"""
Will output:

Amare

2.

Paste the following code into script.py:
"""
print(employees[8])
"""
What happens? Why?

When we try to access an element that is outside of the range of the list indexes, Python will return an IndexError.

IndexError: list index out of range

3.

Selecting an element that does not exist produces an IndexError.

In the line of code that you pasted, change 8 to an index that exists so that you don’t get an IndexError.

Run your code again!

Make sure you are selecting an element that exists in the list.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
"""
