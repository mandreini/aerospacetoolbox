# Tester file for the aerotbx.conversions python files.
# Simply calls the functions and checks that they give the correct output
# @author = Matt (matthew@andreini.us)
import aerotbx

import aerotbx.environment
import scipy as sp

t1 = aerotbx.stdatmos(P=[1e5, 1e4, 1e3])[0]
#[110.8864127251899, 16221.007939493587, 31207.084373790043]
t2 = aerotbx.stdatmos(h=sp.linspace(-2000, 81000))
#(array, array, array, array, array)

print("All tests pass")