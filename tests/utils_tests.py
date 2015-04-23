# Tester file for the aerotbx.utils python files.
# Simply calls the functions and checks that they give the correct output
# @author = Matt (matthew@andreini.us)

import aerotbx.utils
import scipy as sp

# int test
integ = 2
integ_array = aerotbx.utils.to_ndarray(integ)
binteg = aerotbx.utils.from_ndarray(*integ_array)

# float test
flt = 5.0
flt_array = aerotbx.utils.to_ndarray(flt)
bflt = aerotbx.utils.from_ndarray(*flt_array)

# list test
lst = [1, 4, 5]
lst_array = aerotbx.utils.to_ndarray(lst)
blst = aerotbx.utils.from_ndarray(*lst_array)

# tuple test
tup = (9,8,7)
tup_array = aerotbx.utils.to_ndarray(tup)
btup = aerotbx.utils.from_ndarray(*tup_array)

# array test
arr = sp.array([2,4])
arr_array = aerotbx.utils.to_ndarray(arr)
barr = aerotbx.utils.from_ndarray(*arr_array)

assert binteg==integ, "function 'from_ndarray' failed on %s" % type(integ)
assert bflt==flt, "function 'from_ndarray' failed on %s" % type(flt)
assert blst==lst, "function 'from_ndarray' failed on %s" % type(lst)
assert btup==tup, "function 'from_ndarray' failed on %s" % type(tup)
assert sp.array_equal(arr, barr), "function 'from_ndarray' failed on %s" % type(arr)

print("All tests pass.")  # passes



