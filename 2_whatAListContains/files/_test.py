load_file_in_context('script.py')
try:
  added_string = ints_and_strings[5]
  if type(added_string) is not str:
    fail_tests("Is the sixth element of `ints_and_strings` a string?")
except NameError:
  fail_tests("Is the list `ints_and_strings` defined?")
except IndexError:
  fail_tests("Did you add a string to `ints_and_strings`?")

pass_tests()
