load_file_in_context('script.py')

expected = shopping_list[-1]
full_equality("last_element", expected, "compare")

pass_tests()
