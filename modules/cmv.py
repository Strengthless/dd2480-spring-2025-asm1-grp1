import math
from modules.types import Coordinate, Parameters
import numpy as np

# Helper functions
def check_lic_0(num_points ,points: list[Coordinate], parameters: Parameters):
    #The LIC evaluates to TRUE if there exists at least one set of two consecutive data points 
    #that are a distance greater than the length, LENGTH1, apart.

    if (num_points < 2 or parameters['length1'] <= 0):
        return False

    for i in range(num_points-1):
        #Point i
        point_i = points[i]
        x_point_i = point_i['x']
        y_point_i = point_i['y']

        #Point i+1 
        point_i_1 = points[i+1]
        x_point_i_1 = point_i_1['x']
        y_point_i_1 = point_i_1['y']

        distance_points = math.sqrt((x_point_i_1 - x_point_i)**2 + (y_point_i_1 - y_point_i)**2)

        if (distance_points > parameters['length1']):
            return True
    return False
  
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

def check_lic_11() -> bool:
    # TODO: Update the function signature and implementation
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
        check_lic_0(num_points, points, parameters),
        check_lic_1(),
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
