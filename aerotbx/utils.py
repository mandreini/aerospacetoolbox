"""Aerospace Toolbox / utils.py

Utility functions used by the entire package.

"""

import scipy as sp

class AerotbxValueError(Exception):
    def __init__(self, message):
        super(AerotbxValueError, self).__init__(message)

    def __repr__(self):
        return self.__name__

    def __str__(self):
        return "Custom error for passing an invalid flow argument."

def to_ndarray(item):
    """convert any item to a numpy ndarray"""
    
    return type(item), sp.array(item, sp.float64, ndmin=1)

def from_ndarray(itemtype, *items):
    """convert any numpy array back to its original item type"""

    if itemtype in [int, float]:
        val = tuple(i.flat[0] for i in items)
    elif itemtype == list:
        val = tuple(list(i) for i in items)
    elif itemtype == tuple:
        val = tuple(tuple(list(i)) for i in items)
    elif itemtype == sp.matrix:
        val = tuple(sp.matrix(i, copy=False) for i in items)
    else:
        val = tuple(i for i in items)
    return val if len(items) > 1 else val[0]
