import math
from modules.types import Coordinate, Parameters
import numpy as np


# Helper functions
def check_lic_0(num_points, points: list[Coordinate], parameters: Parameters) -> bool:
    if num_points < 2 or parameters["length1"] <= 0:
        return False

    for i in range(num_points - 1):
        point_1 = points[i]
        point_2 = points[i + 1]

        distance_points = math.sqrt(
            (point_1["x"] - point_2["x"]) ** 2 + (point_1["y"] - point_2["y"]) ** 2
        )

        if distance_points > parameters["length1"]:
            return True
    return False


def check_lic_1() -> bool:
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


def check_lic_5(points: list[Coordinate]) -> bool:
    return any(p2["x"] - p1["x"] < 0 for p1, p2 in zip(points, points[1:]))


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


def check_lic_10(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    area1 = parameters["area1"]
    e_pts = parameters["e_pts"]
    f_pts = parameters["f_pts"]

    if num_points < 5:
        return False
    if e_pts < 1:
        return False
    if f_pts < 1:
        return False
    if e_pts + f_pts > num_points - 3:
        return False

    for i in range(num_points - e_pts - f_pts - 2):
        # Calculate the area of the triangle that is defined by the two
        # vectors formed by the point i to the point j and k respectively
        point_i = points[i]
        point_j = points[i + e_pts + 1]
        point_k = points[i + e_pts + f_pts + 2]

        vector_1 = [point_j["x"] - point_i["x"], point_j["y"] - point_i["y"]]
        vector_2 = [point_k["x"] - point_i["x"], point_k["y"] - point_i["y"]]

        calc_area = abs((1 / 2) * np.cross(vector_1, vector_2))

        if calc_area > area1:
            return True

    return False


def check_lic_11(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    g_pts = parameters["g_pts"]

    if num_points < 3:
        return False

    if not (1 <= g_pts <= num_points - 2):
        return False

    for i in range(num_points - g_pts - 1):
        if points[i + g_pts + 1]["x"] - points[i]["x"] < 0:
            return True

    return False


def check_lic_12(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    k_pts = parameters["k_pts"]
    length1 = parameters["length1"]
    length2 = parameters["length2"]

    if num_points < 3:
        return False
    if length2 < 0:
        return False

    flag_1 = False
    flag_2 = False

    for i in range(num_points - k_pts - 1):
        j = i + k_pts + 1
        coord1 = np.array([points[j]["x"], points[j]["y"]])
        coord2 = np.array([points[i]["x"], points[i]["y"]])
        # Calculate the distance between the two points
        length_calc = np.linalg.norm(coord1 - coord2)

        if length_calc > length1:
            flag_1 = True

        if length_calc < length2:
            flag_2 = True

        if flag_1 and flag_2:
            return True

    return False


def check_lic_13(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> bool:
    a_pts = parameters["a_pts"]
    b_pts = parameters["b_pts"]
    radius1 = parameters["radius1"]
    radius2 = parameters["radius2"]

    if (radius2 < 0) or (num_points < 5):
        return False

    flag_1 = False
    flag_2 = False

    for i in range(len(points) - a_pts - b_pts - 2):

        # Create the three vectors formed between the points i j and k respectively
        point_i = points[i]
        point_j = points[i + a_pts + 1]
        point_k = points[i + a_pts + b_pts + 2]

        centroid = [
            (point_i["x"] + point_j["x"] + point_k["x"]) / 3,
            (point_i["y"] + point_j["y"] + point_k["y"]) / 3,
        ]

        vector_1 = [point_i["x"] - centroid[0], point_i["y"] - centroid[0]]
        vector_2 = [point_j["x"] - centroid[0], point_j["y"] - centroid[0]]
        vector_3 = [point_k["x"] - centroid[0], point_k["y"] - centroid[0]]

        # Calculate the length of the vectors 1,2 and 3

        length1 = abs(np.linalg.norm(vector_1))
        length2 = abs(np.linalg.norm(vector_2))
        length3 = abs(np.linalg.norm(vector_3))

        max_radius = max(length1, length2, length3)

        if max_radius > radius1:
            flag_1 = True

        if max_radius < radius2:
            flag_2 = True

        if flag_1 and flag_2:
            return True

    return False


def check_lic_14() -> bool:
    # TODO: Update the function signature and implementation
    return False


# Main function
def get_cmv(
    num_points: int, points: list[Coordinate], parameters: Parameters
) -> list[bool]:
    return [
        check_lic_0(num_points, points, parameters),
        check_lic_1(),
        check_lic_2(),
        check_lic_3(),
        check_lic_4(),
        check_lic_5(points),
        check_lic_6(),
        check_lic_7(),
        check_lic_8(),
        check_lic_9(),
        check_lic_10(num_points, points, parameters),
        check_lic_11(num_points, points, parameters),
        check_lic_12(),
        check_lic_13(num_points, points, parameters),
        check_lic_14(),
    ]
