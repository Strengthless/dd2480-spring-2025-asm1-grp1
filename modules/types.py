# Imports
from enum import Enum
from typing import TypedDict

# Type declarations
class Connectors(Enum):
    ANDD = 1
    ORR = 2
    NOTUSED = 777

class Comp_Type(Enum):
    EQ = 1
    GT = 2
    LT = 1111

class Coordinate(TypedDict):
    x: float
    y: float

class Parameters(TypedDict):
    length1: float # Length in LICs 0, 7, 12
    radius1: float # Radius in LICs 1, 8, 13
    epsilon: float # Deviation from PI in LICs 2, 9
    area1: float # Area in LICs 3, 10, 14
    q_pts: int # No. of consecutive points in LIC 4
    quads: int # No. of quadrants in LIC 4
    dist: float # Distance in LIC 6
    n_pts: int # No. of consecutive points in LIC 6
    k_pts: int # No. of int. points in LICs 7, 12
    a_pts: int # No. of int. points in LICs 8, 13
    b_pts: int # No. of int. points in LICs 8, 13 # TODO: Double check! Why is there a duplicate?
    c_pts: int # No. of int. points in LICs 9 
    d_pts: int # No. of int. points in LICs 9 # TODO: Double check! Why is there a duplicate?
    e_pts: int # No. of int. points in LICs 10, 14
    f_pts: int # No. of int. points in LICs 10, 14 # TODO: Double check! Why is there a duplicate?
    g_pts: int  # No. of int. points in LIC 11
    length2: float # Maximum length in LIC 12
    radius2: float # Maximum radius in LIC 13
    area2: float # Maximum area in LIC 14
