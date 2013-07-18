Aerospace Toolbox
================

The Aerospace Toolbox for Python contains functions intended for aerospace engineering analysis to develop and evaluate designs. The toolbox is developed (and currently only tested) in a Python 2.7.5 environment and requires Numpy/Scipy. The toolbox is designed to allow quick and robust evaluation of functions and to properly accept and handle multidimensional matrices/array's. Currently, the toolbox contains the following:


*Environment* (accepts multidimensional arrays as input)
- **stdatmos**: Evaluate any standard atmosphere (default=ISA) at a given geometrical, geopotential, absolute, pressure, temperature or density-altitude.
- **geoidheight**: Calculate the geoid height at any coordinate using the EGM96 Geopotential Model.

*Aerodynamics* (can convert multidimensional arrays from any property to another):
- **flowisentropic**: Isentropic relations with a given set of specific heat ratios and any one of the isentropic flow variables.
- **flownormalshock**: Normal shock relations with a given set of specific heat ratios and any one of the normal shock variables.
- **flowprandtlmeyer**: Prandtl-Meyer function for expansion waves.

*Unit Conversion* (can convert multidimensional arrays from any unit to another):
- **convert**: easy conversion of units, such as mass, pressure and density.


The Aerospace Toolbox for Python is created to (partially) look like the equivalent set of functions in the matlab aerospace toolbox: http://www.mathworks.nl/help/aerotbx/index.html
