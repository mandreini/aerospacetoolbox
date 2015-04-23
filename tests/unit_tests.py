# Tester file for the aerotbx.conversions python files.
# Simply calls the functions and checks that they give the correct output
# @author = Matt (matthew@andreini.us)

import aerotbx.unitconversions
import scipy as sp

# temperature conversions

deg_C = 25
deg_K = aerotbx.unitconversions.convert(deg_C, 'C', 'K')
deg_C_from_K = aerotbx.unitconversions.convert(deg_K, 'K', 'C')

displacements = sp.linspace(0, 30, num=5)
ft = aerotbx.unitconversions.convert(displacements, 'm', 'ft')
disp_from_ft = aerotbx.unitconversions.convert(ft, 'ft', 'm')

# notice: < 1 used as approximations with floats
assert deg_C - deg_C_from_K < 1, "convert failed on converting C to K (and/or back)"
assert all(abs(displacements - disp_from_ft) < 1), "convert failed on converting C to F (and back)"

print("All tests pass")  # passes