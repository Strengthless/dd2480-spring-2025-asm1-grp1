from modules.types import Coordinate, Parameters

import numpy as np

def get_cmv(num_points: int, points: list[Coordinate], parameters: Parameters) -> list[bool]:
    # TODO: To be implemented
    return [False] * 15

def check_lic_10(points, parameters):
    """
    Inputs:
        points: List of coordinates of two-dimensional points
        parameters: Dictionary contains the parameters for the LIC and CMV

    Ouputs:
        Boolean: True if the condition is met, False otherwise

    """
    
    area1 = parameters["area1"]
    e_pts = parameters["e_pts"]
    f_pts = parameters["f_pts"]

    if len(points) < 5:                         # The condition is not met when the number of points is less than 5
        return False
    
    assert(e_pts >= 1)                          # e_pts must be greater than or equal to 1
    assert(f_pts >= 1)                          # f_pts must be greater than or equal to 1
    assert(e_pts + f_pts <= len(points) - 3)    # The sum of e_pts and f_pts must be less than or equal to the number of points - 3

    for i in range(len(points)-e_pts-f_pts-2):

        # Calculate the area of the triangle that is defined by the two vectors formed by the point i to the point i+e_pts+1 and i+f_pts+2 respectively

        vector_1 = [points[i+e_pts+1][0] - points[i][0], points[i+e_pts+1][1] - points[i][1]]
        vector_2 = [points[i+e_pts+f_pts+2][0] - points[i][0], points[i+e_pts+f_pts+2][1] - points[i][1]]

        calc_area = abs((1/2)*np.cross(vector_1, vector_2))

        if calc_area > area1:       # If the area is greater than the area1, the condition is met.
            return True

    return False