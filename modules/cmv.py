from modules.types import Coordinate, Parameters

def get_cmv(num_points: int, points: list[Coordinate], parameters: Parameters) -> list[bool]:
    CMV =  [False for i in range(15)]

    CMV[5] = check_LIC5(num_points, points, parameters)

    return CMV


def check_LIC5(num_points: int, points: list[Coordinate], parameters: Parameters) -> bool:
    return any(p2.x - p1.x < 0 for p1, p2 in zip(points, points[1:]))