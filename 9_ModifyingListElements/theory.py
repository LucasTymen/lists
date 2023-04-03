"""
Introduction to Lists
Modifying List Elements

Let’s return to our garden.

garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]

Unfortunately, we forgot to water our cauliflower and we don’t think it is going to recover.

Thankfully our friend Jiho from Petal Power came to the rescue. Jiho gifted us some strawberry seeds. We will replace the cauliflower with our new seeds.

We will need to modify the list to accommodate the change to our garden list. To change a value in a list, reassign the value using the specific index.

garden[2] = "Strawberries"

print(garden)

Will output:

["Tomatoes", "Green Beans", "Strawberries", "Grapes"]

Negative indices will work as well.

garden[-1] = "Raspberries"

print(garden)

Will output:

["Tomatoes", "Green Beans", "Strawberries", "Raspberries"]

Instructions
1.

We have decided to start selling some of our garden produce. Word around our town has spread and people are interested in getting some of our delicious vegetables and fruit.

We decided to create a waitlist to make sure we can sell to all of our new customers!

Define a list called garden_waitlist and set the value to contain our customers (in order): "Jiho", "Adam", "Sonny", and "Alisha".

Remember the key components of a list:

    A list begins and ends with square brackets ( [ and ] ).

    Each item is separated by a comma ( , )

practice_list = ["String", 6, 0.5, True]

Make sure to double-check your spelling, capitalization, and element order. Check to make sure it matches the values provided from the checkpoint.
2.

"Adam" decided his fridge is too full at the moment and asked us to remove him from the waitlist and make space for one of our other townsfolk.

Replace "Adam" with our other interested customer "Calla" using the index method we used in the narrative.

Print garden_waitlist to see the change!

To change a value in a list, reassign the value using the specific index inside brackets [ ].

example_list = [1, 2, 3, 4]
example_list[2] = -1

print(example_list)

Would output:

[1, 2, -1, 4]

3.

Alisha realized she was already stocked with all the items we are selling. She asked us to replace her with her friend Alex who just ran out.

Replace Alisha with Alex using a negative index.

Print garden_waitlist again to see the change!

Your list output should look like this:

['Jiho', 'Calla', 'Sonny', 'Alex']

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums
Still have questions? View this exercise's thread in the Codecademy Forums.
"""
