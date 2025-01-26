from modules.types import Coordinate, Parameters
import numpy as np

# Helper functions
def check_clic_1() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_2() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_3() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_4() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_5() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_6() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_7() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_8() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_9() -> bool:
    # TODO: Update the function signature and implementation
    return False
  
def check_lic_10(points: list[Coordinate], parameters: Parameters):
    """
    Function to check if the LIC 10 is satisfied

    Inputs:
        points: List[{"x" : float, "y" : float}, ...]
            list of dict
        parameters: (Dict)
            dictionary containing the parameters for LIC and CMW

    Outputs:
        Boolean 
            True if the condition is met, False otherwise

    """
    
    area1 = parameters["area1"]
    e_pts = parameters["e_pts"]
    f_pts = parameters["f_pts"]

    if len(points) < 5:                         
        return False
    
    if (e_pts < 1):
        raise ValueError        
    if (f_pts < 1):
        raise ValueError
    if (e_pts + f_pts > len(points) - 3):
        raise ValueError                        

    for i in range(len(points)-e_pts-f_pts-2):

        # Calculate the area of the triangle that is defined by the two vectors formed by the point i to the point j and k respectively

        j = i+e_pts+1
        k = i+e_pts+f_pts+2

        coord_1 = points[i]
        coord_2 = points[j]
        coord_3 = points[k]

        vector_1 = [coord_2["x"] - coord_1["x"], coord_2["y"] - coord_1["y"]]
        vector_2 = [coord_3["x"] - coord_1["x"], coord_3["y"] - coord_1["y"]]

        calc_area = abs((1/2)*np.cross(vector_1, vector_2))

        if calc_area > area1:       
            return True

    return False

def check_lic_11(points: list[Coordinate], parameters: Parameters):
    """
    Function to check if the LIC 11 is satisfied

    Inputs:
        points: List[{"x" : float, "y" : float}, ...]
            list of dict
        parameters: (Dict)
            dictionary containing the parameters for LIC and CMW

    Outputs:
        Boolean 
            True if the condition is met, False otherwise

    """
    g_pts = parameters["g_pts"]

    if len(points) < 3:
        return False

    if not (1 <= g_pts <= len(points)-2):
        raise ValueError

    for i in range(len(points)-g_pts-1):

        if points[i+g_pts+1]["x"] - points[i]["x"] < 0:     # If the x-coordinate of the point i+g_pts+1 minus the x-coordinate of the point i is less than 0, the condition is met
            
            print(points[i]["x"], points[i+g_pts+1]["x"])
            return True
        
    return False

def check_lic_12() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_13() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_14() -> bool:
    # TODO: Update the function signature and implementation
    return False

def check_lic_14() -> bool:
    # TODO: Update the function signature and implementation
    return False

# Main function
def get_cmv(num_points: int, points: list[Coordinate], parameters: Parameters) -> list[bool]:
    return [
        check_clic_1(),
        check_lic_2(),
        check_lic_3(),
        check_lic_4(),
        check_lic_5(),
        check_lic_6(),
        check_lic_7(),
        check_lic_8(),
        check_lic_9(),
        check_lic_10(points, parameters),
        check_lic_11(),
        check_lic_12(),
        check_lic_13(),
        check_lic_14(),
    ]