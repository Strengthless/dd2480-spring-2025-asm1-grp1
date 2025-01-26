import math
from modules.types import Coordinate, Parameters

def get_cmv(num_points: int, points: list[Coordinate], parameters: Parameters) -> list[bool]:
    # TODO: To be implemented
    return [False] * 15

def lic0(num_points, points, parameters):
    #The LIC evaluates to TRUE if there exists at least one set of two consecutive data points 
    #that are a distance greater than the length, LENGTH1, apart.

    if (num_points < 2 or parameters['length1'] < 0):
        return False

    for i in range(len(points)-1):
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