load_file_in_context('script.py')
try:
 new_orders
except NameError:
 fail_tests('Did you remember to define `new_orders`?')
expected_checkpt1 = ["lilac", "iris"]
if (expected_checkpt1 != new_orders):
 fail_tests('Did you include "lilac" and "iris" in `new_orders`')
pass_tests()
