from modules.types import Coordinate, Parameters

import numpy as np

def get_cmv(num_points: int, points: list[Coordinate], parameters: Parameters) -> list[bool]:
    # TODO: To be implemented
    return [False] * 15

def check_lic_10(points, parameters):
    """
    Function to check if the LIC 10 is satisfied

    Inputs:
        points: List[tuple(float, float), ...]
            list of tuples
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

        vector_1 = [points[j][0] - points[i][0], points[j][1] - points[i][1]]
        vector_2 = [points[k][0] - points[i][0], points[k][1] - points[i][1]]

        calc_area = abs((1/2)*np.cross(vector_1, vector_2))

        if calc_area > area1:       
            return True

    return False