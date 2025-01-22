from modules.types import Comp_Type

def float_compare(a, b, epsilon = 0.000001) -> Comp_Type:
    if (abs(a - b) < epsilon): return Comp_Type.EQ
    elif (a < b): return Comp_Type.LT
    else: return Comp_Type.GT 