# Tester file for the aerotbx.conversions python files.
# Simply calls the functions and checks that they give the correct output
# @author = Matt (matthew@andreini.us)

import aerotbx.aerodynamics
from aerotbx.utils import AerotbxValueError
import scipy as sp

t1 = aerotbx.aerodynamics.flowisentropic(M=3)
# should return: (3.0, 0.35714285714285715, 0.027223683703862824, 0.076226314370815895, 4.2345679012345689)
t2 = aerotbx.flowisentropic(gamma=1.4, sup=1.6)
# should return: (1.9352576078182122, 0.57174077399894296, 0.14131786852470815, 0.24717122680666009, 1.6000000000000001)
t3 = aerotbx.flowisentropic(T=sp.linspace(0, 1, 100))
# should return: (array, array, array, array, array)

try:
    err = aerotbx.aerodynamics.flowisentropic(M=3, gamma=0.75)  # only 1 input
except AerotbxValueError:
    print("All tests pass")
except:
    print("Error not handled properly")
